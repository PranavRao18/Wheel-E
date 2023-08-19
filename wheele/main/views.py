from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accountConfig.models import User
import json
from main.models import Offers
from django.db.models import F, FloatField
from math import radians,  sin, cos


@login_required
def dashboard_view(request):

    user = User.objects.get(email=request.user)
    firstname = user.first_name
    profile = {"first_name": firstname}
    if user.is_driver:
        print("Hello driver")
        offers = Offers.objects.filter(is_active = True, is_accepted = False)
        profile = [{'price': obj.final_price, 'distance': obj.distance} for obj in offers]
        return render(request, 'registration/driver_dashboard.html', {'profile':{'first_name':firstname},'items': profile})
    return render(request, 'registration/dashboard.html', {'profile': profile})


def landing_view(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, "about_us.html")


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
                scooter = str((float(distance)-2)*7)
                auto = str((float(distance)-2)*10)
                mini = str((float(distance)-2)*13)
                sedan = str((float(distance)-2)*15)
            if distance is not None:
                # Save the distance to the database
                Offers.objects.create(
                    distance=distance, fromCoordinatesLat=latA, fromCoordinatesLong=lonA)
                return JsonResponse({'message': 'Distance data saved successfully.', "data": {"scooter": scooter, "auto": auto, "mini": mini, "sedan": sedan}})

        if data.get('type') == 'book':
            offer = Offers.objects.get(requestId=data.get('requestId'))
            offer.is_active = True
            offer.user_id = data.get('user_id')
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

        if data.get('type') == 'get-offers':
            latA = float(data.get('latA'))
            lonA = float(data.get('lonA'))

            # Define the Earth's radius (mean radius in kilometers)
            earth_radius_km = 6371.0

            # Define the distance threshold in kilometers (1 kilometer in this case).
            distance_threshold_km = 1.0

            # Convert driver's latitude and longitude to radians.
            latA_rad = radians(latA)
            lonA_rad = radians(lonA)

            # Calculate the difference in latitude and longitude (in radians) for filtering.
            lat_diff = F('fromCoordinatesLat') - latA_rad
            lon_diff = F('fromCoordinatesLong') - lonA_rad

            # Filter offers within the distance threshold, is_active=True, and is_accepted=False.
            try:
                offers = Offers.objects.filter(
                    fromCoordinatesLat__isnull=False,
                    fromCoordinatesLong__isnull=False,
                    lat_diff__range=(lat_diff - (0.5 * distance_threshold_km / earth_radius_km),
                                     lat_diff + (0.5 * distance_threshold_km / earth_radius_km)),
                    lon_diff__range=(lon_diff - (0.5 * distance_threshold_km / earth_radius_km),
                                     lon_diff + (0.5 * distance_threshold_km / earth_radius_km)),
                    is_active=True,
                    is_accepted=False
                ).annotate(
                    distance_km=(sin(lat_diff / 2) ** 2 + cos(latA_rad) * cos(
                        F('fromCoordinatesLat')) * sin(lon_diff / 2) ** 2) ** 0.5 * 2 * earth_radius_km,
                    output_field=FloatField()
                ).filter(
                    distance_km__lte=distance_threshold_km
                )
            except Exception as e:
                print(f"Error occured {str(e)}")
            print([item for item in offers])
            return JsonResponse({'message': 'hi'})

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
