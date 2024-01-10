##Para declarar variables se coloca la varieble y el valor 

##Variable tipo numerica 
numero = 20
numero2 = 25

##Variable tipo string
cadena = "Nicolas"
cadena2 = "Gonzalez"

##Boleanoos
bool1 = False 
bool2 = True 

##Alfanumericas combinacion de numeros y string

coche = "el coche rojo es de 1999"

## Declaracion de listas, se usan llaves ( Se puede acceder a la informacion y  modificar )
lista = [10, 14, 23, 25]
 ##Declaracion de Tupla, se usan parentesis ( No se puede acceder a la informacion y  modificar )
tupla = (10, 14, 23, 25)





##Para declaracion de variable:
print (numero)

##Para suma, combinacion y declaracion de variable de diferente tipo:
print (numero+numero2)

## print (numero+cadena) : no se puede combinar por ser tipo numerico y string

##Para poder combinar diferentes tipos se usa coma en caso de numerico y string
print (numero, cadena) 

## Para el espacio se usa comillas y se suma
print (cadena+" "+cadena2)

##Forma de declarar y combinar variables 
## Declarar variable 
##Tamplate strings
combinar = f"hola me llamo {cadena} tengo {numero} años"
print (combinar)

##Funcion .upper() se utiliza para cambiar todas las letras a mayusculas
mayusculas = combinar.upper()
print (mayusculas)

##Funcion .lower() se utiliza para cambiar todas las letras a mayusculas 
minusculas = combinar.lower()
print (minusculas)