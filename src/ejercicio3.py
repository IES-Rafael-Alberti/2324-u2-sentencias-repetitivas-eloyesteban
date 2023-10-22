"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""

def numero_impar(numero):
    numero_str = ""
    for i in range (1,numero+1,2):
        numero_str += str(i) +  ", "
    return numero_str[:-2] #Con [:-2] eliminamos la ultima coma y espacio
    


if __name__ == "__main__":

    #Entrada

    numero = int(input("Introduce un número entero: "))

    #Procesas

    impar = numero_impar(numero)

    #Salida

    print(impar)

