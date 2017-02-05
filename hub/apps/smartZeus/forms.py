# -*- coding: utf-8 -*-
from django import forms


class IdentificarPonto_form(forms.Form):
    placeholder = 'Informe seu nome de usuário no ZeuS, data e horário de saída do ponto que você deseja fechar.'
    corpo_texto = forms.CharField(widget=forms.Textarea(attrs={'placeholder':placeholder}))

    def __init__(self, *args, **kwargs):
        super(IdentificarPonto_form, self).__init__(*args, **kwargs)
        self.fields['corpo_texto'].label = ''
