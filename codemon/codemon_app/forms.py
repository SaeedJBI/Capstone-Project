from django import forms
from .models import TechCodemon

class CodemonForm(forms.ModelForm):
    class Meta:
        model = TechCodemon
        fields = ['name', 'tech_track', 'skills', 'difficulty', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Codemon name',
            }),
            'tech_track': forms.Select(attrs={
                'class': 'form-select',
            }),
            'skills': forms.SelectMultiple(attrs={
                'class': 'form-multiselect',
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-select',
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional image URL',
            }),
        }