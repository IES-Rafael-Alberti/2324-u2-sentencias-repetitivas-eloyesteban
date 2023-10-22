"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido.  
"""

def triangulo(altura):
    altura_str = ""
    for i in range(1, altura + 1):
        altura_str += "*" * i + "\n"
    return altura_str


if __name__ == "__main__":

    #Entrada

    altura = int(input("Introduce un número entero: "))

    #Procesar

    figura_final = triangulo(altura)

    #Salida

    print(figura_final)