from django.contrib import admin
from hlohlo_main.forms import LotAddForm, LotUpdateForm
from .models import Lot, Photo, Collection, Category, Region, City, CityDistrict


class LotAdmin(admin.ModelAdmin):

    form = LotUpdateForm
    add_form = LotAddForm

    list_display = ('name',
                    'description',
                    'type_auction',
                    'time_life',
                    'author',
                    'price')
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Lot Info', {'fields': [
                            'description',
                            'type_auction',
                            'time_life',
                            'price',
                            'category']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Lot, LotAdmin)
admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(CityDistrict)
