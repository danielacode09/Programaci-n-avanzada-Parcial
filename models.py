class Estudiante:
    def __init__(self, nombre, edad, nota1, nota2, nota3, genero, actividades, email):
        self.nombre = nombre
        self.edad = int(edad)
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
        self.genero = genero
        self.actividades = actividades
        self.email = email

    @property
    def promedio(self):
        return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

    @property
    def estado(self):
        return "Aprobado" if self.promedio >= 3.0 else "Reprobado"
