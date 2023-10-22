"""
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es que se 
ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el 
usuario fueron números pares. 
"""

def suma_digitos(n):
    """Devuelve la suma de los dígitos de n."""
    return sum(int(digito) for digito in str(n))

def procesar_numeros():
    contador_pares = 0  # Contador para números pares
    numero = 0  # Inicializamos con un valor que permita entrar al bucle
    
    while numero != -1: 
        numero = int(input("Ingrese un número entero positivo (-1 para terminar): "))

        # Verificar que el número es positivo o -1, si no, mostrar mensaje y solicitar nuevamente
        if numero < -1:
            print("Por favor, ingrese un número positivo o -1 para terminar.")
            continue

        # No procesamos el -1
        if numero == -1:
            continue

        # Mostrar suma de dígitos
        print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

        # Verificar si el número es par y aumentar el contador
        if numero % 2 == 0:
            contador_pares += 1

    return contador_pares

if __name__ == "__main__":

    #Entrada

    #Procesar

    total_pares = procesar_numeros()

    #Salida
    
    print(f"Ingresó {total_pares} números pares.")
