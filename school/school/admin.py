from django.contrib import admin
from school.models import City, School

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'coutry_code', 'district_code', 'comm_code')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_code', 'city', 'street', 'street_nr', 'telephone', 'site')

