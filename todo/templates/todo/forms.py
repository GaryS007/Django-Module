from django import forms
from .models import item_name


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']