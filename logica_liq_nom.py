dias_trabajados = 30
horas_por_dia = 8

recargo_diurno = 1.25
recargo_nocturno = 1.75

PORCENTAJE_INCAPACIDAD = 0.66
PORCENTAJE_SALUD = 0.04
PORCENTAJE_PENSION = 0.04


class MuchosDias(Exception):
    """Se dispara cuando los días trabajados son mayores a 30"""
    pass


class SalarioBaseError(Exception):
    """Se dispara cuando el salario base es negativo"""
    pass


class HorasExtraError(Exception):
    """Se dispara cuando las horas extra son negativas"""
    pass


class DeduccionesExcedenNetoError(Exception):
    """Se dispara cuando las deducciones son mayores al total devengado"""
    pass


class ResultadoNomina:
    def __init__(self, total_devengado, total_deducciones, neto):
        self.total_devengado = total_devengado
        self.total_deducciones = total_deducciones
        self.neto = neto


def calcular_nomina(salario_base, dias_trabajados, dias_incapacidad,
                    horas_extra, tipo_extra, auxilio,
                    bonificaciones, deducciones_adicionales):

    # ===== VALIDACIONES INICIALES =====
    if salario_base < 0:
        raise SalarioBaseError("ERROR: El salario base no puede ser negativo")

    if dias_trabajados > DIAS_PERIODO:
        raise MuchosDias("ERROR: Los días trabajados deben ser máximo 30")

    if horas_extra < 0:
        raise HorasExtraError("ERROR: Las horas extra no pueden ser negativas")

    # ===== CÁLCULOS BASE =====
    salario_diario = salario_base / DIAS_PERIODO
    salario_hora = salario_base / (DIAS_PERIODO * HORAS_POR_DIA)

    pago_dias = salario_diario * dias_trabajados
    pago_incapacidad = salario_diario * dias_incapacidad * PORCENTAJE_INCAPACIDAD

    # ===== HORAS EXTRA =====
    if tipo_extra == "D":
        valor_extra = salario_hora * RECARGO_DIURNO
    elif tipo_extra == "N":
        valor_extra = salario_hora * RECARGO_NOCTURNO
    else:
        valor_extra = 0

    total_extras = valor_extra * horas_extra
#D = DIURNA  , N = NOCTURNA
                        
    # ===== TOTAL DEVENGADO =====
    total_devengado = (
        pago_dias +
        pago_incapacidad +
        total_extras +
        auxilio +
        bonificaciones
    )

    # ===== TOTAL DEDUCCIONES =====
    total_deducciones = (
        total_devengado * PORCENTAJE_SALUD +
        total_devengado * PORCENTAJE_PENSION +
        deducciones_adicionales
    )

    # Validación después de calcular
    if total_deducciones > total_devengado:
        raise DeduccionesExcedenNetoError(
            "ERROR: Las deducciones superan el total devengado"
        )

    # ===== NETO =====
    neto = total_devengado - total_deducciones

    return ResultadoNomina(total_devengado, total_deducciones, neto)
