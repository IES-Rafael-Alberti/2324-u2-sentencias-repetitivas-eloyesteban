def piramide(numero):
    piramide_str = ""
    for i in range(1, numero+1):
        for j in range(i, 0, -1):
            piramide_str += str(j) + ""
        piramide_str += "\n"
    return piramide_str

if __name__ == "__main__":

    #Entrada

    numero = int(input("Introduce un entero: "))

    #Procesar

    figura = piramide(numero)

    #Salida

    print(figura)

