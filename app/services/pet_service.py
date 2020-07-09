from ..models import Pet

def cadastrar_pet(pet):
    pet_bd = Pet.objects.create(nome=pet.nome, nascimento=pet.nascimento, categoria=pet.categoria,
                                cor=pet.cor, dono=pet.dono)
    pet_bd.save()


def listar_pets(id):
    pets = Pet.objects.filter(dono=id).all()
    return pets

def editar_pet(pet, pet_novo):
    pet.dono = pet_novo.dono
    pet.nome = pet_novo.nome
    pet.nascimento = pet_novo.nascimento
    pet.categoria = pet_novo.categoria
    pet.cor = pet_novo.cor
    pet.save(force_update=True)

def listar_pet_id(id):
    pet = Pet.objects.get(id=id)
    return pet
