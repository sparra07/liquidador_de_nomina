# Calculadora de Nómina

Aplicación de liquidación de nómina desarrollada en Python.  
Incluye:
- Interfaz gráfica con Kivy
- Interfaz por consola
- Pruebas unitarias

---

## Estructura del proyecto

liquidador_nomina/
│
├── src/
│   ├── Logica/
│   │   └── logica_liq_nom.py
│   │
│   ├── Consola/
│   │   └── main.py
│   │
│   └── GUI/
│       └── app.py
│
├── tests/
│   └── test_nomina.py
│
├── buildozer.spec
└── README.md

---

## Requisitos

- Python 3.10 o superior
- pip
- (Para Android) Linux o WSL

---

## Instalación de dependencias

pip install kivy

---

## Ejecutar la interfaz gráfica (GUI)

Desde la carpeta raíz del proyecto:

python src/GUI/app.py

---

## Ejecutar la interfaz de consola

python src/Consola/main.py

---

## Ejecutar las pruebas unitarias

python -m unittest discover tests

---

## Compilar APK para Android

Este proceso requiere Linux o WSL (Windows Subsystem for Linux).

---

### 1. Instalar WSL en Windows

Abrir PowerShell como administrador y ejecutar:

wsl --install Ubuntu-22.04

Reiniciar el equipo cuando se solicite.  
Luego abrir Ubuntu y crear usuario.

---

### 2. Instalar dependencias en Ubuntu/WSL

sudo apt update  
sudo apt -y upgrade  
sudo apt install -y python3-pip  

pip3 install --user --upgrade buildozer  
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev  
pip3 install --user --upgrade Cython==0.29.33 virtualenv  

Agregar al final de ~/.bashrc:

export PATH=$PATH:~/.local/bin/

Luego ejecutar:

source ~/.bashrc

---

### 3. Clonar el repositorio en WSL

IMPORTANTE: hacerlo dentro de Linux, no en disco de Windows

git clone https://github.com/usuario/repositorio.git  
cd repositorio  

---

### 4. Compilar APK

buildozer -v android debug

---

### 5. Ubicación del APK

El archivo generado estará en:

bin/

---

### 6. Copiar APK a Windows

cp bin/*.apk /mnt/c/Users/TU_USUARIO/Desktop

---

## Notas importantes

- La lógica está en src/Logica/logica_liq_nom.py y es compartida por GUI, consola y tests.
- No ejecutar buildozer dentro de entornos virtuales.
- La primera compilación puede tardar entre 20 y 40 minutos.
- Las carpetas build/, dist/ y bin/ no deben subirse al repositorio.

---

## Funcionalidades

- Cálculo de salario proporcional
- Horas extra diurnas y nocturnas
- Deducciones (salud y pensión)
- Validación de errores
- Interfaz gráfica
- Pruebas automatizadas

---

## Consideraciones

- Los días trabajados no pueden ser mayores a 30
- El salario base no puede ser negativo
- Las deducciones no pueden exceder el total devengado