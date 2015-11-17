from django import forms
from django.shortcuts import redirect
from .models import Lot


class LotAddForm(forms.ModelForm):

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