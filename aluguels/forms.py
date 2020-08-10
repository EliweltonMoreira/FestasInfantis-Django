from django import forms
from .models import Aluguel


class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = (
            'dataFesta', 'horarioInicio', 'horarioTermino', 'valorCobrado',
            'endereco', 'complemento', 'cidade', 'uf', 'tema'
        )
