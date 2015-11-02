from django import forms
from .models import Lot


class AddLotForm(forms.ModelForm):

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
        fields = '__all__'
