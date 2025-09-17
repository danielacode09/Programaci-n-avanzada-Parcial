import re

def validar_email(email):
    patron = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
    return re.match(patron, email) is not None

def dominio_permitido(email, lista_blanca):
    if not validar_email(email):
        return False
    dominio = email.split('@')[-1].lower()
    return dominio in [d.lower() for d in lista_blanca]
