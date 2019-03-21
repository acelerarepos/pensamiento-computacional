def validacion(mensaje):
    strNumero = input(mensaje)

    isvalid = False
    while not isvalid:
        if strNumero.isdigit():
            numero = int(strNumero)
            isvalid = True
        elif strNumero != '' and strNumero[0] == '-' and strNumero[1:].isdigit():
            numero = int(strNumero)
            isvalidN = True
        else:
            print(strNumero, "debe ser un entero")
            strNumero = input(mensaje)
    
    return strNumero

strNumero01 = validacion("Introduzca un número: ")

strNumero02 = validacion("Introduzca otro número: ")

strNumero03 = validacion("Y el tercer número, por favor: ")
    
# Procesamiento de datos
numero01 = int(strNumero01)
numero02 = int(strNumero02)
numero03 = int(strNumero03)
    
numero01 = numero01/10
numero02 = numero02/10

suma = round(numero01 + numero02, 2)
resta = numero01 - numero02
resta = round(resta, 2)
producto = round(numero01 * numero02, 2)
division = round(numero01 / numero02, 2)

# Salida de resultados 
print(numero01, "+", numero02, "=", suma)
print(numero01, "-", numero02, "=", resta)
print(numero01, "·", numero02, "=", producto)
print(numero01, "/", numero02, "=", division)
print("El tercer valor", numero03, "no se usa para nada, jajaja!")

