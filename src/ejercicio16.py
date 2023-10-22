"""
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado. 
"""

def mayor_numero_ingresado(numero):
    mayor = -1  # Inicializamos con un valor negativo para garantizar que cualquier número positivo ingresado será mayor

    while numero != 0:
        # Si el número ingresado es negativo, informar al usuario y solicitar de nuevo
        if numero < 0:
            print("Por favor, ingrese números positivos.")
        else:
            # Si el número ingresado es mayor que el valor actual de "mayor", actualizamos "mayor"
            if numero > mayor:
                mayor = numero

        numero = int(input("Ingrese otro número entero positivo (0 para terminar): "))  # Pedimos otro número al usuario

    # Verificamos si el usuario ingresó algún número positivo o no
    if mayor == -1:
        return None  
    else:
        return mayor

if __name__ == "__main__":

    #Entrada

    numero = int(input("Ingrese un número entero positivo (0 para terminar): "))

    #Procesar
    resultado = mayor_numero_ingresado(numero)

    #Salida

    if resultado:
        print("El mayor número ingresado fue:", resultado)
    else:
        print("No se ingresaron números positivos.")
