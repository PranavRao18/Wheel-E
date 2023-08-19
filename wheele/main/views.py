from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accountConfig.models import User
import json
from main.models import Offers
from django.db.models import F, FloatField
import uuid


@login_required
def dashboard_view(request):

    user = User.objects.get(email=request.user)
    firstname = user.first_name
    id = user.id
    profile = {"first_name": firstname,'user_id':id}
    if user.is_driver:
        print("Hello driver")
        offers = Offers.objects.filter(is_active = True, is_accepted = False)
        profile = [{'price': obj.final_price, 'distance': obj.distance,'lat':obj.fromCoordinatesLat,'lon':obj.fromCoordinatesLong,'requestId':obj.request_id} for obj in offers]
        return render(request, 'registration/driver_dashboard.html', {'profile':{'first_name':firstname,'id':id},'items': profile})
    return render(request, 'registration/dashboard.html', {'profile': profile})


def landing_view(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, "about_us.html")

@login_required
def load(request):
    return render(request,'registration/loading.html')

@login_required
def user_profile(request):
    user = User.objects.get(email=request.user)
    full_name = user.username
    email = user.email
    phone = user.phone_number
    return render(request,"registration/user_profile.html",{'profile':{'first_name':full_name,'email':email,'phone':phone}})

def handle_request(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if data.get('type') == 'coordinates':
            distance = data.get('distance')
            latA = data.get('latA')
            lonA = data.get('lonA')
            if distance < 2 and not None:
                scooter = "30"
                auto = "30"
                mini = "30"
                sedan = "30"
            if distance > 2:
                scooter = round((float(distance)-2)*7,2)
                auto = round((float(distance)-2)*10,2)
                mini = round((float(distance)-2)*13,2)
                sedan = round((float(distance)-2)*15,2)
            if distance is not None:
                # Save the distance to the database
                random_uuid = uuid.uuid4()
                Offers.objects.create(
                    distance=distance, fromCoordinatesLat=latA, fromCoordinatesLong=lonA, request_id = random_uuid)
                return JsonResponse({'message': 'Distance data saved successfully.', "data": {"scooter": scooter, "auto": auto, "mini": mini, "sedan": sedan,"requestId":random_uuid}})

        if data.get('type') == 'book':
            offer = Offers.objects.get(request_id=data.get('requestId'))
            offer.final_price = data.get('price')
            offer.is_active = True
            offer.user_id = data.get('user_id')
            offer.save()
            return JsonResponse({'message': 'Success.'})
        
        if data.get('type') == 'accept':
            offer = Offers.objects.get(request_id=data.get('requestId'))
            offer.is_accepted = True
            offer.save()
            return JsonResponse({'message': 'Success.'})

        if data.get('type') == 'fetch-driver':
            offer = Offers.objects.get(requestId=data.get('requestId'))
            if offer.is_accepted:
                driverid = offer.driver_id
                driver = User.objects.get(id=driverid)
                message = {
                    'success': 'True',
                    'name': driver.first_name,
                    'phoneNo': driver.phone_number,
                    'license': driver.license_number
                }
            else:
                message = {
                    'success': 'False'}
            return JsonResponse({'message': message})



        if data.get('type') == 'fetch-rides':
            offer = Offers.objects.get(user_id=data.get(
                'user_id'), is_active=True, is_accepted=True)
            driverid = offer.driver_id
            driver = User.objects.get(id=driverid)
            if offer is None:
                return JsonResponse({'message': 'none'})
            message = {
                'success': 'True',
                'name': driver.first_name,
                'phoneNo': driver.phone_number,
                'license': driver.license_number,
                'requestId': offer.request_id
            }
            return JsonResponse({'message': message})

        if data.get('type') == 'end-ride':
            offer = Offers.objects.get(requestId=data.get('requestId'))
            offer.is_active = False
            return JsonResponse({'message': "success"})
    return JsonResponse({'message': 'Invalid request.'}, status=400)
