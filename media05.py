notas = (2, 4, 6, 8)

def contenido(lista, indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None
        
    return resultado

# Calcular la media
indice = 0
suma = 0
while contenido(notas, indice) != None:
    suma = suma + notas[indice]
    indice = indice + 1
    
media = suma / indice

# Presentar la media
print("Numero de items: ", indice)
print("Nota Total.....: ", suma)
print("Nota Media.....: ", media)
