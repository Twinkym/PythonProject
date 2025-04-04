# Este programa solicitará el nombre de una receta de cocina a elaborar
# a continuación los campos a solicitar o ingresar serán los siguientes:
# Nombre de la receta, Ingredientes, Tiempo de preparación(en minutos), Dificultad("Facil, Media, Alta")

# Pedir al usuario que introduzca los valores necesarios para inscribir la receta.
titulo_receta = input('Ingrese titulo de la Receta: ')
ingredientes = input('Ingrese los Ingredientes de la receta: ')
tiempo_preparacion = int(input('Ingrese el tiempo de preparación en minutos: '))
dificultad = input('Ingrese la dificultad (Facil, Media, Dificil): ')
instrucciones = input('Describa los pasos a seguir para realizar la receta: ')

# Imprimir los inputs del usuario
print(f'*** {titulo_receta} ***')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo_de_preparación: {tiempo_preparacion} min')
print(f'Dificultad: {dificultad}')
print(f'instrucciones: {instrucciones}')
