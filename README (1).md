# Gestor de Estudiantes (Python + VS Code)

Este proyecto replica los requisitos del parcial pero en **Python**.

## Funcionalidades
- Registro de estudiantes (nombre, edad, notas, género, actividades).
- Cálculo de promedio y estado (Aprobado/Reprobado).
- Visualización en tabla y lista.
- Guardado y carga de datos en CSV (módulo `csv_serializer.py`).
- Envío de correos (usando `smtplib`).
- Validación de email y dominio (en `helpers.py`).

## Estructura
- `main.py` → Ventana principal (GUI con tkinter).
- `models.py` → Clase `Estudiante`.
- `helpers.py` → Validaciones y utilidades.
- `csv_serializer.py` → Lectura y escritura de CSV.
- `estudiantes.csv` → Archivo de ejemplo.
- `resources/` → Imágenes de aprobado/reprobado.

## Requisitos
Instalar dependencias con:
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python main.py
```

## Notas
- Para pruebas de correo usar un servidor como [smtp4dev](https://github.com/rnwood/smtp4dev).
- No incluyas credenciales reales en el código.
