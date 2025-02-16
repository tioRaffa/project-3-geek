from django.shortcuts import render
from .forms import ContactForms
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    form = ContactForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContactForms()

        else:
            messages.error(request, 'Erro ao enviar o E-mail!')

    context = {
        'form_vws': form,
    }

    return render(request, 'pages/contact.html', context)


def prodruct(request):
    return render(request, 'pages/product.html')
