# Liquidador de nomina

Proyecto académico en Python para la materia Código Limpio.
La aplicación liquida la nómina de un trabajador dependiente en Colombia, calculando devengados, deducciones legales y el valor neto a pagar, incorporando reglas básicas de incapacidades y validaciones.
## Autores 
-Manolo Restrepo Gil
-Juan David Idarraga Porras
-Hans Schoonewolff Otero
## ENTRADAS DEL SISTEMA
- Salario base mensual
- Días del periodo (por defecto 30)
- Días trabajados
- Días de incapacidad
- Horas extra trabajadas
- Lapso del dia de horas extra (Dia o noche)
- Auxilio de transporte (si aplica)
- Bonificaciones u otros ingresos
- Deducciones adicionales
## PROCESOS
### 1. Cálculo del salario proporcional
- Valor día = salario_base / días_periodo
- Horas extra
- Pago por días trabajados
- Ajuste por incapacidades
### 2. Gestión de incapacidades
- Días 1 y 2: 100%
- Desde el día 3: 66.66%
- Validación: los días de incapacidad no pueden superar el periodo
### 3. Auxilio de transporte
- Aplica hasta 2 salarios mínimos
- Se prorratea
### 4. Deducciones
- Salud: 4%
- Pensión: 4%
- Fondo solidaridad: 1% desde 4 SMMLV (opcional)
### 5. Cálculo final
- Total devengado
- Total deducciones
- Neto a pagar
### SALIDAS
- Total devengado
- Total deducciones
- Neto a pagar

