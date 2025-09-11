from django import forms
from .models import Organizadores

class OrganizadoresForm(forms.ModelForm):
    class Meta:
        model = Organizadores
        fields = '__all__'