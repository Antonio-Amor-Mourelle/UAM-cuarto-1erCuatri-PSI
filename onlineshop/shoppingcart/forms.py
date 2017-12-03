from django import forms


class CartAddProductForm(forms.Form):
    choices = ((str(i), str(i)) for i in range(1,11))
    units=forms.IntegerField(widget=forms.Select(choices=choices), min_value=1, max_value=10, initial=1)
    update=forms.BooleanField(widget=forms.HiddenInput(), required=False)
