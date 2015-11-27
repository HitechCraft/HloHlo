from django import forms
from multiupload.fields import MultiFileField
from .models import Lot, Category, Collection, Photo


class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=5, max_file_size=1024*1024*5)


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
        widget=forms.CheckboxInput(attrs={'class': 'form-control'}),
        required=False
    )

    time_life = forms.IntegerField(
        label="Время жизни вашей блядь (в днях)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    price = forms.FloatField(
        label="Цена аукциона",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    price_buy_now = forms.FloatField(
        label="Цена 'купить сейчас'",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )

    """category = forms.CharField(
        label="Категория",
        widget=forms.SelectMultiple(choices=Category.objects.values_list('id', 'name'))
    )"""

    attachments = MultiFileField(label="Выберите до 5ти фото", min_num=1, max_num=3, max_file_size=1024*1024*5)

    class Meta:
        model = Lot
        fields = ('name', 'description', 'type_auction', 'time_life', 'price', 'price_buy_now', 'category')


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
        fields = ('name', 'description', 'type_auction', 'time_life', 'price', 'price_buy_now', 'category',)


class CollectionForm(forms.ModelForm):
    name = forms.CharField(
        label="Название",
        widget=forms.TextInput,
        max_length=255
    )

    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea,
        max_length=1500
    )

    class Meta:
        model = Collection
        fields = ('name', 'description', 'lots',)
