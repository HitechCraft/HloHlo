from django import forms
from django.shortcuts import redirect
from .models import Lot, Category


class LotAddForm(forms.ModelForm):
    name = forms.CharField(
        label="Наименование",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=1500
    )
    type_auction = forms.BooleanField(
        label="Купить сейчас",
        widget=forms.CheckboxInput(attrs={'class': 'form-control'})
    )

    time_life = forms.IntegerField(
        label="Время жизни вашей блядь (в днях)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    price = forms.FloatField(
        label="Цена",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    """category = forms.CharField(
        label="Категория",
        widget=forms.SelectMultiple(choices=Category.objects.values_list('id', 'name'))
    )"""

    class Meta:
        model = Lot
        fields = ('name', 'description', 'type_auction', 'time_life', 'price', 'category',)


class LotUpdateForm(forms.ModelForm):
    name = forms.CharField(
        label="Наименование",
        widget=forms.TextInput,
        max_length=255
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea,
        max_length=1500
    )

    class Meta:
        model = Lot
        fields = 'name', 'description', 'type_auction', 'time_life', 'price', 'category',
