from ..models import ConsultaPet

def cadastar_consulta(consulta):
    consulta_bd = ConsultaPet.objects.create(pet=consulta.pet, motivo_consulta=consulta.motivo_consulta,
                                             peso_atual=consulta.peso_atual,
                                             medicamento_atual=consulta.medicamento_atual,
                                             medicamentos_prescritos=consulta.medicamentos_prescritos,
                                             exames_prescritos=consulta.exames_prescritos)

    consulta_bd.save()