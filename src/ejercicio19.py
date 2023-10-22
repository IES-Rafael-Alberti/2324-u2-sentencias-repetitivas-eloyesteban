"""
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, 
informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver 
a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la 
impresión del menú y el programa finalizará.Mostrar un menú con tres opciones: 1- comenzar programa, 
2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una 
opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar 
luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un
texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará. 
"""

def mostrar_menu():
    print("1- Comenzar programa")
    print("2- Imprimir listado")
    print("3- Finalizar programa")

def comenzar_programa():
    print("El programa ha comenzado.\n")

def imprimir_listado():
    print("Listado impreso.\n")

def general():
    opcion = 0  
    
    while opcion != 3:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1, 2 ó 3): "))

            if opcion == 1:
                comenzar_programa()
            elif opcion == 2:
                imprimir_listado()
            elif opcion == 3:
                print("Finalizando programa...")
            else:
                print("Opción incorrecta. Por favor, seleccione una opción válida.")
                
        except ValueError:
            print("Error. Por favor, ingrese un número válido.")

    print("¡Hasta pronto!")

if __name__ == "__main__":
    general()
