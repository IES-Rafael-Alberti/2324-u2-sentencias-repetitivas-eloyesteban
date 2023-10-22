"""
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución. 
"""
def buscar_letra_en_frase():
    # Solicitamos al usuario la frase y la letra
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")

    # Nos aseguramos de que la letra ingresada sea un solo carácter
    if len(letra) != 1:
        print("Por favor, ingrese solamente un carácter como letra.")
        return

    # Recorremos la frase buscando la letra
    for indice, caracter in enumerate(frase):
        if caracter == letra:
            print(f"Se encontró la letra '{letra}' en la posición {indice}.")
            return  # Finalizamos la ejecución una vez encontrada la letra
        else:
            print(f"No hay coincidencia en la posición {indice}.")

    print(f"La letra '{letra}' no se encontró en la frase.")

if __name__ == "__main__":
    buscar_letra_en_frase()
