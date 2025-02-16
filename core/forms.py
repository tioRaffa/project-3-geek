from django import forms
from django.core.mail.message import EmailMessage


class ContactForms(forms.Form):
    name = forms.CharField(max_length=20, label='Nome')
    email = forms.EmailField(max_length=100, label='E-mail')
    subject = forms.CharField(max_length=100, label='Assunto')
    message = forms.CharField(
        max_length=200, widget=forms.Textarea(), label='Mensagem')

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\nE-mail: {email}\nSubject: {subject}\nMessage: {message}'

        success = f'\033[31mE-mail sent succescfully!\033[m'

        mail = EmailMessage(
            subject=success,
            body=content,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )

        mail.send()
