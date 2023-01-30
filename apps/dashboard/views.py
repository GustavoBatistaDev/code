from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import AvaliacaoForm, AlertaDeCriseForm, AnotacaoForm
from .models import Avaliacao, Anotacao
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from django.core.mail import send_mail

DASHBOARD_URL = 'dashboard:dashboard'
CRISE_URL = 'dashboard:crise'


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard/index.html')


@login_required(login_url='account:login')
def lista_avaliacoes(request: HttpRequest) -> HttpResponse:
    avaliacoes = Avaliacao.objects.filter(user=request.user).order_by('-data')

    return render(
        request,
        'dashboard/avaliacoes.html',
        context={
            'title': 'avaliacoes',
            'avaliacoes': avaliacoes,
        },
    )


@login_required(login_url='account:login')
def cadastro_avaliacao(request: HttpRequest) -> HttpResponse:
    # sourcery skip: extract-method
    if request.method != 'POST':
        return redirect(DASHBOARD_URL)

    form = AvaliacaoForm(request.POST)

    form_anotacao_factory = inlineformset_factory(
        Avaliacao, Anotacao, form=AnotacaoForm
    )
    form_anotacao = form_anotacao_factory(request.POST)
    if form.is_valid() and form_anotacao.is_valid():
        form.save(commit=False)
        form.instance.user = request.user
        avaliacao = form.save()

        form_anotacao.instance = avaliacao
        form_anotacao.save()

        messages.success(request, 'Avaliação salva com sucesso!')
        return redirect(DASHBOARD_URL)

    messages.error(request, 'Verifique os dados digitados.')
    return redirect(DASHBOARD_URL)


@login_required(login_url='account:login')
def editar_avaliacao(request: HttpRequest, id: int) -> HttpResponse:
    # sourcery skip: extract-method
    if request.method != 'POST':
        return redirect(DASHBOARD_URL)

    obj = Avaliacao.objects.filter(id=id).first()

    if obj is None:
        return redirect(DASHBOARD_URL)

    form = AvaliacaoForm(request.POST, instance=obj)

    form_anotacao_factory = inlineformset_factory(
        Avaliacao, Anotacao, form=AnotacaoForm
    )
    form_anotacao = form_anotacao_factory(request.POST, instance=obj)
    if form.is_valid() and form_anotacao.is_valid():
        form.save(commit=False)
        form.instance.user = request.user
        avaliacao = form.save()

        form_anotacao.save(commit=False)
        form_anotacao.instance.avaliacao = avaliacao
        form_anotacao.save()

        # __import__('ipdb').set_trace()
        messages.success(request, 'Avaliação atualizada com sucesso!')
        return redirect(DASHBOARD_URL)

    messages.error(request, 'Erro ao atualizar avaliacao!')
    return redirect(DASHBOARD_URL)


@login_required(login_url='account:login')
def deletar_avaliacao(request: HttpRequest, id: int) -> HttpResponse:
    # sourcery skip: extract-method
    if request.method != 'GET':
        return redirect(DASHBOARD_URL)

    obj = Avaliacao.objects.filter(id=id).first()

    if obj is None:
        messages.success(request, 'Avaliação não existe')
        return redirect(DASHBOARD_URL)

    obj.delete()

    messages.success(request, 'Avaliação deletada com sucesso!')
    return redirect(DASHBOARD_URL)


@login_required(login_url='account:login')
def form_avaliacao(request):
    if request.method != 'GET':
        return redirect(DASHBOARD_URL)

    form_avaliacao = AvaliacaoForm()

    form_anotacao_factory = inlineformset_factory(
        Avaliacao, Anotacao, form=AnotacaoForm, extra=1
    )

    id_avaliacao = request.GET.get('id', None)
    if not id_avaliacao:
        form_anotacao = form_anotacao_factory()
        context = {
            'form_avaliacao': form_avaliacao,
            'form_anotacao': form_anotacao,
        }
        return render(request, 'dashboard/partials/_form_avaliacao.html', context)

    obj = Avaliacao.objects.filter(id=id_avaliacao).first()

    if obj is None:
        return redirect(DASHBOARD_URL)

    form_avaliacao = AvaliacaoForm(instance=obj)
    form_anotacao_factory = inlineformset_factory(
        Avaliacao, Anotacao, form=AnotacaoForm, extra=1
    )
    form_anotacao = form_anotacao_factory(instance=obj)

    context = {
        'form_avaliacao': form_avaliacao,
        'form_anotacao': form_anotacao,
    }
    return render(request, 'dashboard/partials/_form_avaliacao.html', context)


@login_required(login_url='account:login')
def cadastro_alerta_de_crise(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return redirect(DASHBOARD_URL)

    form = AlertaDeCriseForm(request.POST)
    if form.is_valid():
        form.save(commit=False)
        form.instance.user = request.user
        form.save()

        messages.success(request, 'Crise salva com sucesso!')
        return redirect(CRISE_URL)

    messages.error(request, 'Verifique os dados digitados.')
    return redirect(CRISE_URL)


@login_required(login_url='account:login')
def crise(request):
    return render(request, 'dashboard/crisi.html')


@login_required(login_url='account:login')
def contato(request):
    return render(request, 'dashboard/contact.html')


@login_required(login_url='account:login')
def ajuda(request):
    if contatos := request.user.contatoajuda_set.all():
        for contato in contatos:
            message = f'URGENTE! A PESSOA CHAMADA [{request.user.first_name.upper()}] SOLICITOU AJUDA URGENTE!!'
            send_mail(
                'AJUDA URGENTE',
                message,
                contato.email,
                ['to@example.com'],
                fail_silently=False,
            )
    messages.success(
        request, 'SOLICITAÇÃO DE AJUDA ENVIADA PARA TODOS OS CONTATOS!'
    )
    return redirect(DASHBOARD_URL)
