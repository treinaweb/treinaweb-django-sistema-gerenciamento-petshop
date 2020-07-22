import datetime

from django.shortcuts import render, redirect

from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoClienteForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service, pet_service, consulta_service

def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    pets = pet_service.listar_pets(id)
    consultas = consulta_service.listar_consultas_pets(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente, 'pets': pets, 'consultas': consultas})


def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    endereco = endereco_service.listar_endereco_id(cliente.endereco.id)
    if request.method == "POST":
        cliente_service.remover_cliente(cliente)
        endereco_service.remover_endereco(endereco)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})


def cadastrar_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            email = form_cliente.cleaned_data["email"]
            cpf = form_cliente.cleaned_data["cpf"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            profissao = form_cliente.cleaned_data["profissao"]
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
                return redirect('listar_clientes')
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})

def editar_cliente(request, id):
    cliente_editar = cliente_service.listar_cliente_id(id)
    cliente_editar.data_nascimento = cliente_editar.data_nascimento.strftime('%Y-%m-%d')
    form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)
    endereco_editar = endereco_service.listar_endereco_id(cliente_editar.endereco.id)
    form_endereco = EnderecoClienteForm(request.POST or None, instance=endereco_editar)
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data["nome"]
        email = form_cliente.cleaned_data["email"]
        cpf = form_cliente.cleaned_data["cpf"]
        data_nascimento = form_cliente.cleaned_data["data_nascimento"]
        profissao = form_cliente.cleaned_data["profissao"]
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_editado = endereco_service.editar_endereco(endereco_editar, endereco_novo)
            cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_editado)
            cliente_service.editar_cliente(cliente_editar, cliente_novo)
            return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente ,'form_endereco': form_endereco})
