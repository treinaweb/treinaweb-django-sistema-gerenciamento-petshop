from django import forms
from ..models import ConsultaPet

class ConsultaPetForm(forms.ModelForm):
    class Meta:
        model = ConsultaPet
        fields = '__all__'
        exclude = ['pet', 'data']