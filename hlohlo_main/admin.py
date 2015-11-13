from django.contrib import admin
from .models import Lot, Lots,Category, Region, City, CityDistrict

admin.site.register(Lot)
admin.site.register(Lots)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(CityDistrict)