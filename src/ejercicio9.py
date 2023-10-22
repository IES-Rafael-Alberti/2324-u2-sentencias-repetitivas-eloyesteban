"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 
"""

def verificar_contraseña(contraseña):
    llave = "contraseña"
    while contraseña != llave:
        contraseña = input("Introduce la contraseña: ")
    return "Contraseña correcta"

if __name__ == "__main__":

    #Entrada

    contraseña = input("Introdcue la contraseña: ")

    #Procesar

    verificacion = verificar_contraseña(contraseña)

    #Salida

    print(verificacion)
