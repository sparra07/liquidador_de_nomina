# Liquidador de Nómina

Proyecto académico desarrollado en Python para la materia **Código Limpio**.
La aplicación permite liquidar la nómina de un trabajador dependiente en Colombia, calculando devengados, deducciones legales y el valor neto a pagar, incorporando reglas básicas de incapacidades y validaciones.

---

##  Autores

* Manolo Restrepo Gil
* Juan David Idarraga Porras
* Hans Schoonewolff Otero

---

##  Requisitos

* Python 3.x instalado en el sistema

---

## Ejecución de la aplicación (Interfaz de Consola)

Siga los siguientes pasos para ejecutar el proyecto:

1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/repositorio.git
```

2. Ingresar al directorio del proyecto:

```bash
cd liquidador_de_nomina
```

3. Ejecutar la aplicación en consola:

```bash
python main.py
```

> Nota: Si el archivo principal tiene otro nombre, reemplácelo en el comando anterior.

---

##  Ejecución de pruebas unitarias

Para ejecutar las pruebas unitarias del proyecto:

1. Asegúrese de estar en la carpeta del proyecto.

2. Ejecute el siguiente comando:

```bash
python -m unittest
```

> Nota: Si las pruebas están organizadas en una carpeta (por ejemplo, `tests/`), utilice:

```bash
python -m unittest discover
```

---

## Uso de la aplicación

Al ejecutar el programa, el sistema solicitará los datos necesarios para realizar la liquidación de la nómina.

El usuario debe ingresar la información en el siguiente orden:

1. Salario base mensual
2. Días del periodo (por defecto 30 si no se ingresa)
3. Días trabajados
4. Días de incapacidad
5. Horas extra trabajadas
6. Tipo de horas extra (día o noche)
7. Auxilio de transporte (si aplica)
8. Bonificaciones u otros ingresos
9. Deducciones adicionales

Una vez ingresados los datos, el sistema procesará la información automáticamente y mostrará en pantalla:

* Total devengado
* Total deducciones
* Neto a pagar

---

##  Ejemplo de ejecución

```text
Ingrese salario base: 1300000
Ingrese días del periodo: 30
Ingrese días trabajados: 30
Ingrese días de incapacidad: 0
Ingrese horas extra: 5
Ingrese tipo de horas extra: dia
Ingrese auxilio de transporte: si
Ingrese bonificaciones: 0
Ingrese deducciones adicionales: 0
```

```text
Total devengado: $1.450.000
Total deducciones: $116.000
Neto a pagar: $1.334.000
```

---

##  Parámetros del sistema

```python
dias_periodo = 30
horas_por_dia = 8

recargo_diurno = 1.25
recargo_nocturno = 1.75

porc_incapacidad = 0.66
porc_salud = 0.04
porc_pension = 0.04
```

---

##  Entradas del sistema

* Salario base mensual
* Días del periodo (por defecto 30)
* Días trabajados
* Días de incapacidad
* Horas extra trabajadas
* Lapso del día de horas extra (día o noche)
* Auxilio de transporte (si aplica)
* Bonificaciones u otros ingresos
* Deducciones adicionales

---

##  Procesos

### 1. Cálculo del salario proporcional

* Valor día = salario_base / días_periodo
* Pago por días trabajados
* Cálculo de horas extra
* Ajuste por incapacidades

### 2. Gestión de incapacidades

* Días 1 y 2: 100% del salario
* Desde el día 3: 66.66%
* Validación: los días de incapacidad no pueden superar el periodo

### 3. Auxilio de transporte

* Aplica hasta 2 salarios mínimos
* Se liquida de forma proporcional

### 4. Deducciones

* Salud: 4%
* Pensión: 4%
* Fondo de solidaridad: 1% desde 4 SMMLV (opcional)

### 5. Cálculo final

* Total devengado
* Total deducciones
* Neto a pagar

---

##  Salidas

* Total devengado
* Total deducciones
* Neto a pagar

---

##  Consideraciones

* Los días de incapacidad no pueden superar los días del periodo.
* El auxilio de transporte solo aplica para salarios hasta 2 SMMLV.
* El fondo de solidaridad aplica únicamente para salarios superiores a 4 SMMLV.





