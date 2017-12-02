from django import forms


class CartAddProductfForm(forms.Form):
    units=forms.IntegerField()
    update_units=forms.BooleanField(widget=forms.HiddenInput())
