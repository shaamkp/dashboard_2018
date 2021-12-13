from django import forms
from django.db.models import fields
from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import Select, TextInput, Textarea
from product.models import Product, Category
from django.forms.widgets import DateInput
from django.utils.translation import ugettext_lazy as _


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    image = forms.ImageField()

    class Meta:
        model = Product
        exclude = ('unit_sold',)
        widgets = {
            "exp_date" : DateInput(attrs={'type': 'date'})
        }
        error_messages = {
            'product_name' : {
                'required' : _("product_name field is required."),
            },
            'in_stock' : {
                'required' : _("in_stock field is required."),
            },
            'description' : {
                'required' : _("description field is required."),
            },
            'exp_date' : {
                'required' : _("exp_date field is required."),
            },
            'category' : {
                'required' : _("category field is required."),
            },
            'category' : {
                'required' : _("category field is required."),
            },
            'image' : {
                'required' : _("image field is required."),
            },
        }
                
