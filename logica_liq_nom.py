DIAS_PERIODO = 30
HORAS_POR_DIA = 8

RECARGO_DIURNO = 1.25
RECARGO_NOCTURNO = 1.75

PORC_INCAPACIDAD = 0.66
PORC_SALUD = 0.04
PORC_PENSION = 0.04

class MuchosDias(Exception):
    """se dispara cuando los dias trabajados son mayores a 30 """
class DiasTrabajadosError(Exception): 
    """se dispara cuando el salario neto es negativo"""
class HorasExtraError(Exception):         
    """se dispara cuando las horas extra son negativas"""
class DeduccionesExcedenNetoError(Exception):
        """se dispara cuando las deducciones son mayores al salario neto""" 

class ResultadoNomina:
    def __init__(self, total_devengado, total_deducciones, neto):
        self.total_devengado = total_devengado
        self.total_deducciones = total_deducciones
        self.neto = neto


def calcular_nomina(salario_base, dias_trabajados, dias_incapacidad,
                    horas_extra, tipo_extra, auxilio,
                    bonificaciones, deducciones_adicionales):

    salario_diario = salario_base / DIAS_PERIODO
    salario_hora = salario_base / (DIAS_PERIODO * HORAS_POR_DIA)

    # M
    pago_dias = salario_diario * dias_trabajados

    # N (66%)
    pago_incapacidad = salario_diario * dias_incapacidad * PORC_INCAPACIDAD

    # Valor hora extra
    if tipo_extra == "D":
        valor_extra = salario_hora * RECARGO_DIURNO
    elif tipo_extra == "N":
        valor_extra = salario_hora * RECARGO_NOCTURNO
    else:
        valor_extra = 0

    # P
    total_extras = valor_extra * horas_extra

    if horas_extra < 0:
        raise HorasExtraError("ERROR: No se pueden descontar horas extra")
    if dias_trabajados > 30:
        raise MuchosDias("ERROR: los dias trabajados deben ser maximo 30")
    if total_deducciones > total_devengado:
        raise DeduccionesExcedenNetoError("ERROR: Las deduciones son mayores al salario neto")
    if salario_base < 0:
        raise DiasTrabajadosError("ERROR: el salario base no puede ser negativo")
    # Q
    total_devengado = (
        pago_dias +
        pago_incapacidad +
        total_extras +
        auxilio +
        bonificaciones
    )

    # R
    total_deducciones = (
        total_devengado * PORC_SALUD +
        total_devengado * PORC_PENSION +
        deducciones_adicionales
    )

    neto = total_devengado - total_deducciones

    return ResultadoNomina(total_devengado, total_deducciones, neto)
