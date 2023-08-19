from django.contrib import admin
from .models import Offers  # Import the Offers model from your app

class OffersAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'distance', 'fromCoordinatesLat', 'fromCoordinatesLong')
    list_filter = ('is_active',)
    search_fields = ('distance', 'fromCoordinatesLat', 'fromCoordinatesLong')
    
    # Customize other admin options if needed

# Register the Offers model with its admin class
admin.site.register(Offers, OffersAdmin)
