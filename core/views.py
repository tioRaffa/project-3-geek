from django.shortcuts import render, redirect
from .forms import ContactForms, ProdutoModelForm
from django.contrib import messages
from .models import Produto
# Create your views here.


def index(request):
    prod = Produto.objects.all()

    context = {
        'produto': prod,
    }

    return render(request, 'pages/index.html', context=context)


def contact(request):

    if str(request.method) == 'POST':
        form = ContactForms(request.POST or None)

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
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                messages.success(request, 'Produto Salvo Com Sucesso!')
                form = ProdutoModelForm()  # limpa o formulario

            else:
                messages.error(
                    request, 'ERRO!!! Nao Foi Possivel Salvar o Produto.')

        else:
            form = ProdutoModelForm()

        context = {
            'form_vws': form,
        }

        return render(request, 'pages/product.html', context=context)

    else:
        return redirect('home')


def login(request):
    return render(request, 'pages/login.html')
