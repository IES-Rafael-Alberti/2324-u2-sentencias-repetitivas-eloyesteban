"""
Escribir un programa en el que se pregunte al usuario por una 
frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. 
"""

def contar_apariciones(frase, letra): #cuenta las apariciones de la letra en la frase
    conteo = 0
    for char in frase:
        if char == letra:
            conteo += 1
    return conteo

if __name__ == "__main__":

    #Entrada

    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    #Procesar

    resultado = contar_apariciones(frase, letra)

    #Salida 

    print(f"La letra '{letra}' aparece {resultado} veces en la frase.")

