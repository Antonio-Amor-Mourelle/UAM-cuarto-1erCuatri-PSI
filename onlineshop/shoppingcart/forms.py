from django import forms


class CartAddProductForm(forms.Form):
    """
    Formulario para annadir un producto al carro o modificar sus unidades
    Autor: Esther Lopez Ramos
    """
    choices = ((i, str(i)) for i in range(1,11))
    units=forms.IntegerField(widget=forms.Select(choices=choices), min_value=1, max_value=10, initial=1)
    update=forms.BooleanField(widget=forms.HiddenInput(), required=False, initial=False)
