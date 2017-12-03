from atividade.models import Atividade
from django.forms import ModelForm, Textarea, DateInput


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao', 'data_inicio', 'data_fim', 'prazo']
        exclude = ['dev_id', 'req_id']
        widgets = {'descricao': Textarea(attrs={'class': 'form-control'}),
                   'data_inicio': DateInput(attrs={'class': 'form-control', 'placeholder': 'exemplo: 30/12/2017', 'required': False}),
                   'data_fim': DateInput(attrs={'class': 'form-control', 'placeholder': 'exemplo: 30/12/2017', 'required': False}),
                   'prazo': DateInput(attrs={'class': 'form-control', 'placeholder': 'exemplo: 30/12/2017', 'required': False})}
