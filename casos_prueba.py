# ==============================
# CONSTANTES DEL SISTEMA
# ==============================

DIAS_PERIODO = 30
HORAS_POR_DIA = 8
PORC_SALUD = 0.04
PORC_PENSION = 0.04
RECARGO_DIURNO = 1.25
RECARGO_NOCTURNO = 1.75
PORC_INCAPACIDAD = 0.66


# ==============================
# FUNCIONES DE VALIDACIÓN
# ==============================

def validar_entradas(salario_base, dias_trabajados, dias_incapacidad,
                     horas_extra, deducciones_adicionales):
    
    if salario_base < 0:
        raise ValueError("El salario no puede ser negativo")

    if dias_trabajados < 0 or dias_incapacidad < 0:
        raise ValueError("Los días no pueden ser negativos")

    if dias_trabajados > DIAS_PERIODO:
        raise ValueError("Los días trabajados no pueden superar 30")

    if dias_trabajados + dias_incapacidad > DIAS_PERIODO:
        raise ValueError("La suma de días trabajados e incapacidad supera el período")

    if horas_extra < 0:
        raise ValueError("Las horas extra no pueden ser negativas")

    if deducciones_adicionales < 0:
        raise ValueError("Las deducciones adicionales no pueden ser negativas")


# ==============================
# FUNCIONES DE CÁLCULO
# ==============================

def salario_diario(salario_base):
    return salario_base / DIAS_PERIODO


def salario_por_hora(salario_base):
    return salario_base / (DIAS_PERIODO * HORAS_POR_DIA)


def calcular_valor_hora_extra(salario_base, tipo_extra):
    valor_hora = salario_base / (DIAS_PERIODO * HORAS_POR_DIA)

    if tipo_extra == "D":
        return valor_hora * RECARGO_DIURNO
    elif tipo_extra == "N":
        return valor_hora * RECARGO_NOCTURNO
    else:
        return 0


def calcular_nomina(salario_base, dias_trabajados, dias_incapacidad,
                    horas_extra, tipo_extra, auxilio,
                    bonificaciones, deducciones_adicionales):

    validar_entradas(
        salario_base, dias_trabajados,
        dias_incapacidad, horas_extra,
        deducciones_adicionales
    )

    s_diario = salario_diario(salario_base)

    pago_dias = s_diario * dias_trabajados
    pago_incapacidad = s_diario * dias_incapacidad * PORC_INCAPACIDAD

    valor_extra = calcular_valor_hora_extra(salario_base, tipo_extra)
    total_extras = valor_extra * horas_extra

    total_devengado = (
        pago_dias +
        pago_incapacidad +
        total_extras +
        auxilio +
        bonificaciones
    )

    salud = total_devengado * PORC_SALUD
    pension = total_devengado * PORC_PENSION

    total_deducciones = salud + pension + deducciones_adicionales
    neto = total_devengado - total_deducciones

    return {
        "Total Devengado": total_devengado,
        "Total Deducciones": total_deducciones,
        "Neto a Pagar": neto
    }


# ==============================
# CASOS DE PRUEBA
# ==============================

def ejecutar_casos():
    casos = [
        # CASOS NORMALES
        ("Caso Normal", 1500000, 30, 2, 10, "D", 162000, 0, 0),
        ("Caso Normal 2", 2000000, 30, 0, 5, "D", 0, 0, 50000),
        ("Caso Normal 3", 1800000, 28, 0, 8, "N", 162000, 0, 20000),

        # EXTRAORDINARIOS
        ("Muchas horas extra", 1500000, 30, 0, 40, "D", 162000, 0, 0),
        ("Pocos días trabajados", 1500000, 10, 0, 0, "D", 0, 0, 0),
        ("Deducciones muy altas", 2500000, 30, 0, 0, "D", 0, 0, 500000),

        # INCAPACIDAD ALTA
        ("Incapacidad 20 días", 1500000, 10, 20, 0, "D", 0, 0, 0),
        ("Incapacidad total", 1800000, 0, 30, 0, "D", 0, 0, 0),

        # CASOS DE ERROR
        ("Salario negativo", -1500000, 30, 0, 5, "D", 162000, 0, 0),
        ("Horas extra negativas", 1500000, 30, 0, -4, "D", 162000, 0, 0),
    ]

    for caso in casos:
        nombre = caso[0]
        print(f"\n--- {nombre} ---")

        try:
            resultado = calcular_nomina(*caso[1:])
            for clave, valor in resultado.items():
                print(f"{clave}: {round(valor, 2)}")
        except ValueError as e:
            print(f"ERROR: {e}")


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    ejecutar_casos()
