from django import forms
from .models import Route, Airport

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['airport', 'position', 'duration']
        widgets = {
            'position': forms.NumberInput(attrs={'min': 1}),
            'duration': forms.NumberInput(attrs={'min': 1}),
        }