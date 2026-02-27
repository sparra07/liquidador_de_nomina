import logica_liq_nom

"""
Interfaz de usuario para el cálculo de nómina.
Se encarga de capturar los datos de entrada, invocar la lógica
y mostrar los resultados o errores al usuario.
"""

print("--- Sistema de Liquidación de Nómina ---")
print("Ingrese los datos del empleado para calcular su pago mensual.\n")

try:
    # Captura de datos básicos
    salario_base = float(input("Salario base mensual ($): "))
    dias_trabajados = int(input("Días efectivamente trabajados: "))
    dias_incapacidad = int(input("Días de incapacidad (si aplica, sino 0): "))
    
    # Datos de horas extra
    print("\nInformación de Horas Extra:")
    horas_extra = float(input("  Cantidad de horas extra: "))
    tipo_extra = input("  Tipo de hora extra (D para Diurna / N para Nocturna): ").upper()
    
    # Otros conceptos
    print("\nOtros conceptos:")
    auxilio = float(input("  Auxilio de transporte/otros ($): "))
    bonificaciones = float(input("  Bonificaciones adicionales ($): "))
    deducciones_adicionales = float(input("  Otras deducciones (prestamos, otros) ($): "))

    # Invocación de la lógica
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

    # Presentación de resultados
    print("\n" + "="*30)
    print("      RESUMEN DE NÓMINA")
    print("="*30)
    print(f"Total Devengado:    ${resultado.total_devengado:,.2f}")
    print(f"Total Deducciones:  ${resultado.total_deducciones:,.2f}")
    print("-" * 30)
    print(f"NETO A PAGAR:       ${resultado.neto:,.2f}")
    print("="*30)

    # Validación lógica adicional (como en tus pruebas)
    if resultado.neto < 0:
        print("\n¡ALERTA!: El neto es negativo. Las deducciones superan los ingresos.")

except ValueError:
    print("\nERROR: Por favor ingrese solo valores numéricos en los campos correspondientes.")
except Exception as err:
    print(f"\nNo se pudo calcular la nómina.")
    print(f"Detalle del error: {err}")
