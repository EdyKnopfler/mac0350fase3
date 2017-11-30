from analise_de_requisitos.models import AnaliseDeRequisitos
from django.forms import ModelForm, TextInput, Textarea


class AnaliseDeRequisitosForm(ModelForm):
    class Meta:
        model = AnaliseDeRequisitos
        fields = ['nome', 'descricao']
        widgets = {'nome': TextInput(attrs={'class': 'form-control'}),
                   'descricao': Textarea(attrs={'class': 'form-control'})}
