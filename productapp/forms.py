from django import forms
from views import *

# a form for creating
# new products

class ProductFrom(forms.ModelForm):

    class Meta: # data/ info configuration details for the class
        model = Product
        fieilds = ('name', 'details', 'price')