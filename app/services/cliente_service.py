from ..models import Cliente

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco, cpf=cliente.cpf,
                           data_nascimento=cliente.data_nascimento, profissao=cliente.profissao)

def listar_clientes():
    return Cliente.objects.all()

def listar_cliente_id(id):
    return Cliente.objects.get(id=id)