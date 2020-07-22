from django.shortcuts import render, redirect
from ..forms import pet_forms
from ..entidades import pet
from ..services import pet_service, cliente_service, consulta_service

def inserir_pet(request, id):
    if request.method == "POST":
        form_pet = pet_forms.PetForm(request.POST)
        dono = cliente_service.listar_cliente_id(id)
        if form_pet.is_valid():
            nome = form_pet.cleaned_data["nome"]
            nascimento = form_pet.cleaned_data["nascimento"]
            categoria = form_pet.cleaned_data["categoria"]
            cor = form_pet.cleaned_data["cor"]
            pet_novo = pet.Pet(dono=dono, nome=nome, nascimento=nascimento, categoria=categoria,
                                        cor=cor)
            pet_service.cadastrar_pet(pet_novo)
            return redirect('listar_clientes')
    else:
        form_pet = pet_forms.PetForm()
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})

def listar_pet_id(request, id):
    pet = pet_service.listar_pet_id(id)
    consultas = consulta_service.listar_consultas(id)
    return render(request, 'pets/lista_pet.html', {'pet': pet, 'consultas': consultas})

def editar_pet(request, id):
    pet_antigo = pet_service.listar_pet_id(id)
    form_pet = pet_forms.PetForm(request.POST or None, instance=pet_antigo)
    if form_pet.is_valid():
        dono = form_pet.cleaned_data["dono"]
        nome = form_pet.cleaned_data["nome"]
        cor = form_pet.cleaned_data["cor"]
        nascimento = form_pet.cleaned_data["nascimento"]
        categoria = form_pet.cleaned_data["categoria"]
        pet_novo = pet.Pet(dono=dono, nome=nome, cor=cor, nascimento=nascimento,
                                    categoria=categoria)
        pet_service.editar_pet(pet_antigo, pet_novo)
        return redirect('listar_pets')
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})