class Cliente():
    def __init__(self, nome, email, cpf, data_nascimento, profissao, endereco):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__profissao = profissao
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
