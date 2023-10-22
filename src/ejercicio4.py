"""
Escribir un programa que pida al usuario un número entero positivo y muestre 
por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
"""

def cuenta_atras(numero):
    numero_str = ""
    for i in range(numero, -1, -1):
        numero_str += str(i) + ", "
    return numero_str[:-2]

if __name__=="__main__":

    #Entrada

    numero = int(input("Introduce un número entero: "))

    #Procesar

    resultado = cuenta_atras(numero)

    #Salida

    print(resultado)
