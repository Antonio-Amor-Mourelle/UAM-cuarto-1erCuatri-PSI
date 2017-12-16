from django import forms
from models import Order


class OrderCreateForm(forms.ModelForm):
    """
    Formulario que pide los datos necesarios al usuario para realizar el pedido
    Autor: Antonio Amor
    """
    firstName=forms.CharField(max_length=50, help_text="First name", required=True)
    familyName=forms.CharField(max_length=50, help_text="Family name", required=True)
    email=forms.EmailField(help_text="e-mail", required=True)
    address=forms.CharField(max_length=50, help_text="Address", required=True)
    zip=forms.CharField(max_length=20, help_text="Zip code", required=True)
    city=forms.CharField(max_length=50, help_text="City", required=True)
    
    class Meta():
        model=Order
        fields = ('firstName', 'familyName', 'email', 'address', 
                  'zip', 'city',)