from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('url', 'product_name', 'product_count', 'size',
                  'color', 'address', 'description')
