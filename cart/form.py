from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


#  This allows the user to select a quantity between one and 20. You
# use a TypedChoiceField field with coerce=int to convert the input into
# an integer.
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=_('Quantity'), choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False,
                                  widget=forms.HiddenInput)
