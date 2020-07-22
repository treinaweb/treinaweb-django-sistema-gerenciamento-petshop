from django import forms
from django.forms import DateInput

from ..models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'nascimento', 'cargo']
        widgets = {
            'nascimento': DateInput(
                attrs={'type': "date"}
            )
        }