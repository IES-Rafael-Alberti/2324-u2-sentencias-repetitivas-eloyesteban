"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el 
interés anual y el número de años, y muestre por pantalla el capital obtenido 
en la inversión cada año que dura la inversión.
"""
def calculadora_inversion(amount,interest,años):
    for i in range(años):
        amount *= 1 + interest/100
        amount_str = "Tras " + str(i+1) + " años, el capital es: " + str(round(amount, 2))
    return amount_str
    


if __name__=="__main__":

    #Entrada

    amount = float(input("Cantidad a invertir: "))   #Cantidad anual a invertir (amount)
    interest = float(input("Introduce el interes anual: "))
    años = int(input("Introduce la duración en años de la inversion(por ejemplo: '2' ): "))

    #Procesar

    capital_obtenido = calculadora_inversion(amount, interest, años)

    #Salida

    print(capital_obtenido)
    