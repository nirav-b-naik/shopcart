from django import forms

from .models import Mobile


class MobileForm(forms.ModelForm):

    class Meta:
        model = Mobile
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"style": "color: blue; font-weight: bold;"}),
            "brand": forms.TextInput(attrs={"style": "color: green;"}),
            "price": forms.NumberInput(attrs={"style": "color: red;"}),
            "offer": forms.CheckboxInput(attrs={"style": "margin-left: 10px;"}),
        }
