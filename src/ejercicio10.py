"""
Escribir un programa que pida al usuario un número entero y muestre 
por pantalla si es un número primo o no. 
"""
def comprobacion(numero):
    if numero < 2:
        return 0  
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return 0  # Consideraremos 0 como "no es primo"
    return 1  # Consideraremos 1 como "es primo"

if __name__ == "__main__":

    #Entrada 

    numero= int(input("Introduce un numero entero positivo mayor que 2: "))
   

    #Procesar

    if comprobacion(numero) == 1:
        solucion = str(numero) + " es primo"
    else:
        solucion = str(numero) + " no es primo"
    #Salida

    print(solucion)
