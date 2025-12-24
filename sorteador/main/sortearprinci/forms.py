from django import forms
from .models import Numbers

class NumbersForm(forms.ModelForm):
    class Meta:
        model = Numbers
        fields = ['inicio', 'fim', 'quantidade']
        widgets = {
            'inicio': forms.NumberInput(attrs={
                'min': 0,
                'value': 0
            }),
            'fim': forms.NumberInput(attrs={
                'min': 1,
                'value': 1
            }),
            'quantidade': forms.NumberInput(attrs={
                'min': 1,
                'value': 1
            }),
        }