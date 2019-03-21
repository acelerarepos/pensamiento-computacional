nombre = input("¿Cómo te llamas? ")
print("Hola, ", nombre)

strEdad = input("¿Cuantos años tienes? ")
strAnno = input("¿En que año estamos? ")
strMes = input("¿En qué mes estamos? ")
strDia = input("¿En qué día estamos? ")

edad = int(strEdad)
anno = int(strAnno)
mes = int(strMes)
dia = int(strDia)

transcurridos = 0

if mes == 1:
    transcurridos = transcurridos + dia
elif mes ==  2:
    transcurridos = transcurridos + 31 + dia
elif mes ==  3:
    transcurridos = transcurridos + 31 + 28 + dia
elif mes ==  4:
    transcurridos = transcurridos + 31 + 28 + 31 + dia
elif mes ==  5:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + dia
elif mes ==  6:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + dia
elif mes ==  7:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + 30 + dia
elif mes ==  8:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia
elif mes ==  9:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia
elif mes ==  10:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia
elif mes ==  11:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia
else:
    transcurridos = transcurridos + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia
    
prob = transcurridos / 365 * 100
nacimiento = anno - edad
    
print(nombre, "naciste en", nacimiento, "con una probabilidad de", prob)
print(" o en", nacimiento - 1, "con una probabilidad de", 100- prob)

