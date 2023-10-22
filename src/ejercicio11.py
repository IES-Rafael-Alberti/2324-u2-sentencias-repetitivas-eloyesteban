"""
Escribir un programa que pida al usuario una palabra y 
luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última. 
"""

def invertir_palabra(palabra):
    palabra_invertida = ""
    for i in range(len(palabra)-1, -1, -1):
        palabra_invertida += palabra[i] + "\n"
    return palabra_invertida

if __name__ == "__main__":

    #Entrada

    palabra = input("Introduce una palabra: ")

    #Procesar

    resultado = invertir_palabra(palabra)

    #Salida

    print(resultado)    