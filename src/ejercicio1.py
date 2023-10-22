"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def repeticion(palabra):
    resultado = ""
    for i in range(10):
        resultado += palabra + "\n"
    return resultado.strip()  # strip() elimina el último salto de línea.
    
   

if __name__ == "__main__":

#Entrada

    palabra = input("Introduce una palabra: ")

    

#Procesar
    
    bucle = repeticion(palabra)

#Salida

    print(bucle)