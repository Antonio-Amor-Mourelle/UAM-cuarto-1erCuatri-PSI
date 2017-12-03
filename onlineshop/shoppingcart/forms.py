from django import forms


class CartAddProductForm(forms.Form):
    units=forms.IntegerField(min_value=1, max_value=10, initial=1)
    update=forms.BooleanField(widget=forms.HiddenInput(), required=False)
