from django import forms
from .models import Movel

class MovelForm(forms.ModelForm):
    class Meta:
        model = Movel
        fields = ['nome', 'comodo', 'preco', 'data_compra']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'comodo': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'nome': 'Nome do Móvel',
            'comodo': 'Cômodo',
            'preco': 'Preço',
            'data_compra': 'Data da Compra',
        }