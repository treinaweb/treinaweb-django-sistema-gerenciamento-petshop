class ConsultaPet():
    def __init__(self, pet, motivo_consulta, peso_atual, medicamento_atual, medicamentos_prescritos,
                 exames_prescritos, data=""):
        self.__pet = pet
        self.__motivo_consulta = motivo_consulta
        self.__peso_atual = peso_atual
        self.__medicamento_atual = medicamento_atual
        self.__medicamentos_prescritos = medicamentos_prescritos
        self.__exames_prescritos = exames_prescritos
        self.__data = data

    @property
    def pet(self):
        return self.__pet

    @pet.setter
    def pet(self, pet):
        self.__pet = pet

    @property
    def motivo_consulta(self):
        return self.__motivo_consulta

    @motivo_consulta.setter
    def motivo_consulta(self, motivo_consulta):
        self.__motivo_consulta = motivo_consulta

    @property
    def peso_atual(self):
        return self.__peso_atual

    @peso_atual.setter
    def peso_atual(self, peso_atual):
        self.__peso_atual = peso_atual

    @property
    def medicamento_atual(self):
        return self.__medicamento_atual

    @medicamento_atual.setter
    def medicamento_atual(self, medicamento_atual):
        self.__medicamento_atual = medicamento_atual

    @property
    def medicamentos_prescritos(self):
        return self.__medicamentos_prescritos

    @medicamentos_prescritos.setter
    def medicamentos_prescritos(self, medicamentos_prescritos):
        self.__medicamentos_prescritos = medicamentos_prescritos

    @property
    def exames_prescritos(self):
        return self.__exames_prescritos

    @exames_prescritos.setter
    def exames_prescritos(self, exames_prescritos):
        self.__exames_prescritos = exames_prescritos

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data