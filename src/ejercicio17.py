"""
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen. 
"""

def suma_digitos(numero):

    str_numero = str(numero)
    suma = 0

    for i in str_numero:
        suma += int(i)
    return suma

if __name__ == "__main__":

    #Entrada

    numero = int(input("Ingrese un número entero positivo: "))
    
    while numero < 0:
        print("El número debe ser positivo.")
        numero = int(input("Ingrese un número entero positivo: "))

    #Procesar
    
    resultado = suma_digitos(numero)

    #Salida
    
    print(f"La suma de los dígitos de {numero} es: {resultado}")
