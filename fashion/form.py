from django import forms
from fashion.models import Shirt


class ShirtForm(forms.ModelForm):

    class Meta:
        model = Shirt
        fields = "__all__"
