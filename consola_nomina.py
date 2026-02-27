import logica_liq_nom

"""
Interfaz de usuario para el cálculo de nómina.
Captura datos, invoca la lógica y muestra resultados.
"""

print("--- Sistema de Liquidación de Nómina ---")
print("Ingrese los datos del empleado para calcular su pago mensual.\n")

try:
    # ===== DATOS BÁSICOS =====
    salario_base = float(input("Salario base mensual ($): "))
    dias_trabajados = int(input("Días efectivamente trabajados: "))
    dias_incapacidad = int(input("Días de incapacidad (si aplica, sino 0): "))

    # ===== HORAS EXTRA =====
    print("\nInformación de Horas Extra:")
    horas_extra = float(input("  Cantidad de horas extra: "))
    tipo_extra = input("  Tipo de hora extra (D para Diurna / N para Nocturna): ").upper()

    # ===== OTROS CONCEPTOS =====
    print("\nOtros conceptos:")
    auxilio = float(input("  Auxilio de transporte/otros ($): "))
    bonificaciones = float(input("  Bonificaciones adicionales ($): "))
    deducciones_adicionales = float(input("  Otras deducciones (préstamos, otros) ($): "))

    # ===== LLAMADO A LA LÓGICA =====
    resultado = logica_liq_nom.calcular_nomina(
        salario_base,
        dias_trabajados,
        dias_incapacidad,
        horas_extra,
        tipo_extra,
        auxilio,
        bonificaciones,
        deducciones_adicionales
    )

    # ===== RESULTADOS =====
    print("\n" + "=" * 35)
    print("         RESUMEN DE NÓMINA")
    print("=" * 35)
    print(f"Total Devengado:    ${resultado.total_devengado:,.2f}")
    print(f"Total Deducciones:  ${resultado.total_deducciones:,.2f}")
    print("-" * 35)
    print(f"NETO A PAGAR:       ${resultado.neto:,.2f}")
    print("=" * 35)

    if resultado.neto < 0:
        print("\nALERTA: El neto es negativo.")

# ===== MANEJO DE ERRORES =====
except ValueError:
    print("\nERROR: Ingrese únicamente valores numéricos válidos.")

except logica_liq_nom.MuchosDias as e:
    print(f"\n{e}")

except logica_liq_nom.SalarioBaseError as e:
    print(f"\n{e}")

except logica_liq_nom.HorasExtraError as e:
    print(f"\n{e}")

except logica_liq_nom.DeduccionesExcedenNetoError as e:
    print(f"\n{e}")

except Exception as err:
    print("\nNo se pudo calcular la nómina.")
    print(f"Detalle del error: {err}")
