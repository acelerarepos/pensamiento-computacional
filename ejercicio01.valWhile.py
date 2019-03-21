# Entrada de datos
strNumero01 = input("Introduzca un número: ")

isvalidN01 = False
while not isvalidN01:
    if strNumero01.isdigit():
        numero01 = int(strNumero01)
        isvalidN01 = True
    elif strNumero01 != '' and strNumero01[0] == '-' and strNumero01[1:].isdigit():
        numero01 = int(strNumero01)
        isvalidN01 = True
    else:
        print(strNumero01, "debe ser un entero")
        strNumero01 = input("Introduzca un número: ")

strNumero02 = input("Introduzca otro número: ")

isvalidN02 = False
while not isvalidN02:
    if strNumero02.isdigit():
        numero02 = int(strNumero02)
        isvalidN02 = True
    elif strNumero02 != '' and strNumero02[0] == '-' and strNumero02[1:].isdigit():
        numero02 = int(strNumero02)
        isvalidN02 = True
    else:
        print(strNumero02, "debe ser un entero")
        strNumero02 = input("Introduzca otro número: ")
        
    
# Procesamiento de datos
numero02 = int(strNumero02)
    
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

