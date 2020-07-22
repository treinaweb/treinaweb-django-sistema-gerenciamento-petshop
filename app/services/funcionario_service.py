from ..models import Funcionario


def listar_funcionarios():
    funcionarios = Funcionario.objects.all()
    return funcionarios


def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, nascimento=funcionario.nascimento,
                               cargo=funcionario.cargo)
