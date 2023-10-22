"""
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la 
sumatoria de todos los números ingresados. 
"""

def sumatoria_numeros(numero):
    suma = 0  

    while numero != 0:  # Mientras el número ingresado no sea 0
        suma += numero  # Sumamos el número ingresado a la variable suma
        numero = int(input("Ingrese otro número entero (0 para terminar): "))  

    return suma  

if __name__ == "__main__":

    #Entrada

    numero = int(input("Ingrese un número entero (0 para terminar): ")) 

    #Procesar

    resultado = sumatoria_numeros(numero)

    #Salida

    print("La sumatoria de los números ingresados es:", resultado)


