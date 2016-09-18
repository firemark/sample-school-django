from django.contrib import admin
from school.models import City, School

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('name', 'country_code', 'district_code', 'comm_code')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('name', 'school_code', 'city', 'street', 'street_nr', 'telephone', 'site')

