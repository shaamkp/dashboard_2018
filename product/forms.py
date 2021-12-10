from django import forms
from django.db.models import fields
from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import Select, TextInput, Textarea
from product.models import Product, Category
from django.forms.widgets import DateInput


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Product
        exclude = ('unit_sold',)

        widgets = {
            "exp_date" : DateInput(attrs={'type': 'date'})
        }
        