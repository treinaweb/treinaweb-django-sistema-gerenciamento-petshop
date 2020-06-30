from ..models import EnderecoCliente

def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)