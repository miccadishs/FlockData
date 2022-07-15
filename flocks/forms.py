from .models import *
from django import forms

class RecordsForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

        widgets = {
            'flock': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'deaths_mortality': forms.TextInput(attrs={'class': 'form-control'}),
            'deaths_culls': forms.TextInput(attrs={'class': 'form-control'}),
            'body_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'body_uniformity': forms.Select(attrs={'class': 'form-control'}),
            'feed_consumed': forms.TextInput(attrs={'class': 'form-control'}),
            'feed_delivered': forms.TextInput(attrs={'class': 'form-control'}),
            'feed_formula': forms.TextInput(attrs={'class': 'form-control'}),
            'water_consumed': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature_outside': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature_inside': forms.TextInput(attrs={'class': 'form-control'}),
            'eggs_broken': forms.TextInput(attrs={'class': 'form-control'}),
            'eggs_sold': forms.TextInput(attrs={'class': 'form-control'}),
            'egg_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),

        }


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination

        fields = '__all__'

        widgets = {
            'flock':forms.Select(attrs={'class':'form-control'}),
            'vaccine': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'date_expiration': forms.DateInput(attrs={'class': 'form-control'}),
        }


class FlockForm(forms.ModelForm):
    class Meta:
        model = Flock

        fields = '__all__'

        widgets = {
            'house':forms.Select(attrs={'class':'form-control'}),
            'breed':forms.Select(attrs={'class':'form-control'}),
            'flock_id': forms.TextInput(attrs={'class': 'form-control'}),
            'stage': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_hatched': forms.DateInput(attrs={'class': 'form-control'}),
            'date_in': forms.DateInput(attrs={'class': 'form-control'}),
            'date_out': forms.DateInput(attrs={'class': 'form-control'}),
            'birds_placed': forms.TextInput(attrs={'class': 'form-control'}),


        }