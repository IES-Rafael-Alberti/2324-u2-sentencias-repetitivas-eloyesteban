"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados. 
"""

def sumatoria_numeros_positivos(numero):
    suma = 0  

    while numero != 0:  # Mientras el número ingresado no sea 0
        if numero > 0:  # Solo sumamos si el número es positivo
            suma += numero  
        numero = int(input("Ingrese otro número entero (0 para terminar): ")) 

    return suma  
if __name__ == "__main__":

    #Entrada

    numero = int(input("Ingrese un número entero (0 para terminar): "))

    #Procesar

    resultado = sumatoria_numeros_positivos(numero)

    #Salida

    print("La sumatoria de los números positivos ingresados es:", resultado)
