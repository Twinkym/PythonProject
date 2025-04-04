# Programa para generar un ID unico
# Importar las librerias necesarias
import random


def generar_id_unico():
    # Título de la aplicación
    print('*** Sistema Generador de ID Unico ***')
    # solicitar los datos al usuario.
    nombre = input('Ingresa tu Nombre: ')
    apellido = input('Ingresa tu Apellido: ')
    anio_de_nacimiento = input('Ingresa tu año de nacimiento (yyyy): ')

    # Validar que el año de nacimiento tenga 4 dígitos.
    if len(anio_de_nacimiento) != 4 or not anio_de_nacimiento.isdigit():
        print('Pro favor, ingresa un año de nacimiento válido.')
        return

    # Obtener las dos primeras letras de nombre y apellido, y los dos últimos dígitos del año de nacimiento.
    parte_nombre = nombre[:2].upper()  # Primeras dos letras del nombre.
    parte_apellido = apellido[:2].upper()
    parte_anio = anio_de_nacimiento[-2:]  # Ultimos dos dígitos del año de nacimiento.

    # Generar un número aleatorio de 4 dígitos
    numero_aleatorio = random.randint(1000, 9999)

    # Generar el ID único
    id_unico = f'{parte_nombre}{parte_apellido}{parte_anio}{numero_aleatorio}'

    # Mostrar el ID único generado
    print(f'''Hola tu nuevo número de identificación (ID) único generado por el sistema es:
{id_unico}
Felicidades!!! ''')


# Ejecutar la función
generar_id_unico()
