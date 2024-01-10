import math
import os



while True:
    os.system("cls")
    menu = """ Calculadora\n 
    Opcion 1: sumar
    Opcion 2: restar
    Opcion 3: multiplicar
    Opcion 4: dividir
    Opcion 5: potencia cuadrada
    Opcion 6: logaritmica
    Opcion 7: raiz cuadrada
    Opcion 8: salir
    """
    print (menu)

    opcion = input("Selecciona una opcion: \n")

    os.system("cls")

    if opcion== "1":
        print ("Ha seleccionado la opcion sumar\n")
        numero1 = int(input ("Escriba un numero:\n"))
        numero2 = int(input ("Escriba otro numero\n"))
        suma = numero1+numero2 
        print ("El resultado es", suma)
        input ("Presiona una tecla para continuar") 
    elif opcion== "2":
        print ("Ha seleccionado la opcion restar")
        numero1 = int(input ("Escriba un numero:\n"))
        numero2 = int(input ("Escriba otro numero\n"))
        resta = numero1-numero2
        print ("El resultado es", resta)
        input ("Presiona una tecla para continuar") 
    elif opcion== "3":
        print ("Ha seleccionado la opcion multiplicar")
        numero1 = int(input ("Escriba un numero:\n"))
        numero2 = int(input ("Escriba otro numero\n"))
        mult = numero1*numero2
        print ("El resultado es", mult)
        input ("Presiona una tecla para continuar") 
    elif opcion== "4":
        print ("Ha seleccionado la opcion dividir")
        numero1 = int(input ("Escriba un numero:\n"))
        numero2 = int(input ("Escriba otro numero\n"))
        div = numero1/numero2
        print ("El resultado es", div)
        input ("Presiona una tecla para continuar") 
    elif opcion== "5":
        print ("Ha seleccionado la opcion potencia cuadrada")
        numero1 = int(input ("Escriba un numero:\n"))
        pot = numero1*numero1
        print ("El resultado es", pot)
        input ("Presiona una tecla para continuar") 

    elif opcion== "6":

        print ("Ha seleccionado la opcion logaritmica")
        x = int(input ("Escriba un numero:\n"))
        b = int(input ("Escriba la base del logaritmo que desea\n"))
        loga = math.log (x,b)
        print ("El resultado es", loga)
        input ("Presiona un atecla para continuar")

    elif opcion== "7":
        print ("Ha seleccionado la opcion raiz cuadrada")
        numero1 = int(input ("Escriba un numero:\n"))
        raiz = numero1**.5
        print ("El resultado es", raiz)
        input ("Presiona una tecla para continuar") 
    elif opcion== "8":
        break
    else:
        print ("Seleccione una opcion correcta")
        input ("Presiona una tecla para continuar") 
