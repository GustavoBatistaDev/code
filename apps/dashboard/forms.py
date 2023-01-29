from django.forms import ModelForm
from .models import Avaliacao, Anotacao, AlertaDeCrise
from django import forms


class AvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        exclude = ('user',)

        widgets = {
            'data': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'
            ),
        }


class AnotacaoForm(ModelForm):
    class Meta:
        model = Anotacao
        exclude = ('avaliacao',)


class AlertaDeCriseForm(ModelForm):
    class Meta:
        model = AlertaDeCrise
        fields = '__all__'
