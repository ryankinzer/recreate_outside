from django import forms
from .models import Menu, MenuItems

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'description', 'meal', 'category', 'directions', 'special_equipment', 'image1')
   
class MenuItemsForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = ('item', 'amount', 'unit', 'refridgerated')