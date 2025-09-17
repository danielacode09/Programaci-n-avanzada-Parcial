import csv
from models import Estudiante

def leer_csv(ruta):
    estudiantes = []
    with open(ruta, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for row in lector:
            e = Estudiante(
                row['Nombre'], row['Edad'],
                row['Nota1'], row['Nota2'], row['Nota3'],
                row['Genero'], row['Actividades'], row['Email']
            )
            estudiantes.append(e)
    return estudiantes

def escribir_csv(ruta, estudiantes):
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        campos = ['Nombre','Edad','Nota1','Nota2','Nota3','Genero','Actividades','Email']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for e in estudiantes:
            escritor.writerow({
                'Nombre': e.nombre,
                'Edad': e.edad,
                'Nota1': e.nota1,
                'Nota2': e.nota2,
                'Nota3': e.nota3,
                'Genero': e.genero,
                'Actividades': e.actividades,
                'Email': e.email
            })
