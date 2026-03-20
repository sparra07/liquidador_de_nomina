# Constantes
DIAS_trabajados = 30
horas_por_dia = 8

recargo_diurno = 1.25
recargo_nocturno = 1.75

porcentaje_incapacidad = 0.66
porcentaje_salud = 0.04
Porcentaje_pension = 0.04


# ===== EXCEPCIONES =====

class MuchosDias(Exception):
    """Se dispara cuando los días trabajados son mayores a 30"""
    def __init__(self):
        super().__init__("Los días trabajados no pueden ser mayores a 30")


class SalarioBaseError(Exception):
    """Se dispara cuando el salario base es negativo"""
    def __init__(self):
        super().__init__("El salario base no puede ser negativo")


class HorasExtraError(Exception):
    """Se dispara cuando las horas extra son negativas"""
    def __init__(self):
        super().__init__("Las horas extra no pueden ser negativas")


class DeduccionesExcedenNetoError(Exception):
    """Se dispara cuando las deducciones son mayores al total devengado"""
    def __init__(self):
        super().__init__("Las deducciones no pueden superar el total devengado")


# ===== CLASE DE DOMINIO =====

class Nomina:
    """Representa los datos de entrada para el cálculo de nómina"""

    def __init__(self, salario_base, dias_trabajados, dias_incapacidad,
                 horas_extra, tipo_extra, auxilio,
                 bonificaciones, deducciones_adicionales):

        self.salario_base = salario_base
        self.dias_trabajados = dias_trabajados
        self.dias_incapacidad = dias_incapacidad
        self.horas_extra = horas_extra
        self.tipo_extra = tipo_extra
        self.auxilio = auxilio
        self.bonificaciones = bonificaciones
        self.deducciones_adicionales = deducciones_adicionales


class ResultadoNomina:
    """Representa el resultado del cálculo"""

    def __init__(self, total_devengado, total_deducciones, neto):
        self.total_devengado = total_devengado
        self.total_deducciones = total_deducciones
        self.neto = neto


# ===== CLASE DE LÓGICA =====

class NominaCalculator:
    """
    Clase para realizar el cálculo de nómina
    """

    def calcular_nomina(nomina: Nomina):
        """
        Calcula los valores de nómina

        Returns
        -------
        ResultadoNomina
        """

        # Validaciones
        NominaCalculator.check_salario(nomina.salario_base)
        NominaCalculator.check_dias(nomina.dias_trabajados)
        NominaCalculator.check_horas_extra(nomina.horas_extra)

        # ===== CÁLCULOS =====
        salario_diario = nomina.salario_base / DIAS_trabajados
        salario_hora = nomina.salario_base / (DIAS_trabajados * horas_por_dia)

        pago_dias = salario_diario * nomina.dias_trabajados
        pago_incapacidad = salario_diario * nomina.dias_incapacidad * porcentaje_incapacidad

        # Horas extra
        if nomina.tipo_extra == "D":
            valor_extra = salario_hora * recargo_diurno
        elif nomina.tipo_extra == "N":
            valor_extra = salario_hora * recargo_nocturno
        else:
            valor_extra = 0

        total_extras = valor_extra * nomina.horas_extra
        # D=DIURNO , N=NOCTURNO 
        # Total devengado
        total_devengado = (
            pago_dias +
            pago_incapacidad +
            total_extras +
            nomina.auxilio +
            nomina.bonificaciones
        )

        # Deducciones
        total_deducciones = (
            total_devengado * porcentaje_salud +
            total_devengado * Pporcentaje_pension +
            nomina.deducciones_adicionales
        )

        # Validación final
        if total_deducciones > total_devengado:
            raise DeduccionesExcedenNetoError()

        # Neto
        neto = total_devengado - total_deducciones

        return ResultadoNomina(total_devengado, total_deducciones, neto)

    # ===== MÉTODOS DE VALIDACIÓN =====

    def check_salario(salario):
        if salario < 0:
            raise SalarioBaseError()

    def check_dias(dias):
        if dias > DIAS_trabajados:
            raise MuchosDias()

    def check_horas_extra(horas):
        if horas < 0:
            raise HorasExtraError()
