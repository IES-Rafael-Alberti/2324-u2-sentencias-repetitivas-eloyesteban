"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. 
"""

def tablas():
    tabla = ""
    for i in range(1,11):
        tabla += f"\nTabla del {i}:\n"
        for j in range(1,11):
            tabla += f"{i} x {j} = {i * j}\n"
    return tabla

if __name__ == "__main__":

    #Entrada

    #Procesar

    resultado = tablas()

    #Salida

    print(resultado)