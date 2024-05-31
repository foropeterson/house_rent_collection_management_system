from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'address', 'rent', 'description', 'image', 'landlord_contact']