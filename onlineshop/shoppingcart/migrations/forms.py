from django import forms


class CartAddProductForm(forms.Form):
    units=forms.IntegerField()
    update_inits=forms.BooleanField(default=False)
