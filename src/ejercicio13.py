"""
Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará. 
"""

def eco_hasta_salir():
    entrada = ""
    
    while entrada.lower() != "salir":  
        entrada = input("Introduce algo (escribe 'salir' para terminar): ")
        
        if entrada.lower() != "salir":
            print(entrada)  # Muestra el eco de lo que el usuario introdujo

    return entrada  # Devuelve la última entrada (que en este caso sería "salir")


if __name__ == "__main__":

    #Entrada

    #Procesar

    resultado = eco_hasta_salir()

    #Salida
    print(f"Terminaste con la entrada: {resultado}")
