from requisito.models import Requisito
from django.forms import ModelForm, ChoiceField, TextInput, Textarea, RadioSelect, CharField


class RequisitoForm(ModelForm):
    class Meta:
        model = Requisito
        fields = ['tipo', 'nome', 'detalhes']
        widgets = {'tipo': RadioSelect(),
                   'nome': TextInput(attrs={'class': 'form-control'}),
                   'detalhes': Textarea(attrs={'class': 'form-control'})
                   }
        exclude = ['ar_id']
