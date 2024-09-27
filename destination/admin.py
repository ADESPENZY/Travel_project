from django.contrib import admin
from .models import Destination, Country


# Register your models here.
admin.site.register(Country)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'location_name', 'price', 'image', 'created_at', 'slug')
    list_display_links = ('id', 'country')
    search_fields = ('id', 'country', 'location_name')
    prepopulated_fields = {'slug': ('location_name',)}
    list_filter = ('country',)