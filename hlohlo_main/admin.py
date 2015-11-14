from django.contrib import admin
from .models import Lot, Photo, Collection, Category, Region, City, CityDistrict

admin.site.register(Lot)
admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(CityDistrict)