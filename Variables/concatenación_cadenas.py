# Concatenación de Cadenas.
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + ' ' + cadena2
print(concatenacion)

# Utilizando el metodo str.join
concatenacion = "".join(
    [cadena1, ' ', cadena2])  # Agregar un espacio en blanco mediante la inclusion de corchetes simples separados.
print(concatenacion)
