"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). 
"""

def repeticion(edad):
    años_str = ""
    for i in range(1, edad + 1):
        años_str += str(i) + "\n"
    return años_str.strip()


if __name__ == "__main__":

    #Entrada
    
    edad = int(input("Introduce tu edad: "))

    #Procesar

    while edad <=0:
        edad = int(input("Introduce tu edad: "))

    años_cumplidos = repeticion(edad)

    #Salida

    print(años_cumplidos)
