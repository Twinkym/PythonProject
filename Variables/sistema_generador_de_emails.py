# Sistema Generador de Emails
import re


def validar_dominio(dominio):
    # Usamos una expresión simple para validar que el dominio tiene un formato adecuado.
    patron = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, dominio) is not None


print('*** Sistema Generador de Emails ***')


# Función para generar el email.
def generar_email():
    # Solicitar datos del usuario.
    nombre = input('Ingresa el nombre: ').strip().lower()
    apellidos = input('Ingresa los apellidos: ').strip().lower()

    # Solicitar si tiene dominio
    dominio = input('¿Tienes un dominio de correo (sí/no)?').strip().lower()

    if dominio == 'sí' or dominio == 'si':
        dominio_usuario = input('Ingresa tu dominio (por ejemplo, gmail.com): ').strip()
        # Validar dominio.
        if validar_dominio(dominio_usuario):
            email = f'{nombre}.{apellidos}@{dominio_usuario}'
            print(f'Dominio válido: {email}')
        else:
            # Ofrecer dominio predeterminado
            dominio_usuario = 'gmail.com'
            # Generar el correo electrónico
            email = f'{nombre}.{apellidos}@{dominio_usuario}'
            print(f'Dominio no válido. Se asignará un dominio predeterminado: {email}')
    else:
        # Ofrecer dominio predeterminado
        dominio_predeterminado = 'gmail.com'
        # Generar el correo electrónico
        email = f'{nombre}.{apellidos}@{dominio_predeterminado}'
        print(f'Dominio no válido. Se asignará un dominio predeterminado: {dominio_predeterminado}')

    print(f'Tu correo generado es: {email}')


# Ejecutar la función.
generar_email()
