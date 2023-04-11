from django import forms
from .models import Livros


class CadastroLivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ('nome', 'autor', 'co_autor',
                  'data_cadastro', 'emprestado', 'categoria')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'co_autor': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'data_cadastro': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'emprestimo': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'})
        }
