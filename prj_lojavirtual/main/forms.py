from django import forms
from lojavirtual import settings
from django.core.mail import send_mail
class FormFaleConosco(forms.Form):
    nome = forms.CharField(label='nome', max_length=80, required= True)
    email_origem = forms.EmailField(label='Entre com o seu email', required=True)
    mensagem = forms.CharField(label='mensagem', required=True, widget=forms.Textarea)

    def enviar_mensagem_por_email(self):
        send_mail('FALE CONOSCO: mensagem recebida.', self.data['mensagem'], self.data['email_origem'], [settings.EMAIL_FALE_CONOSCO], fail_silently=False)