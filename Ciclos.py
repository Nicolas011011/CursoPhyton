## Ciclos
## Iteracion que se repite depende la condicio
## Iteracion: Numero de veces que se repite el codigo

## range: sirve para declarar el valor maximo de iteraciones 
## El ciclo for repite las iteraciones que tu quieras, en este caso 4
for x in range(4):
  print(x)


##En este caso se creo una lista con cierto numero de elementos los cuales seran las iteraciones que realice el for 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

## Debugging corre el programa paso por paso 
## Ej
for x in range (10):
  print ("soy el numero",x*10)


##Ej suma de numeros de una lista
  
numeros = [1,2,3,4,5,6,7]

##Declarar una variable, crear un ciclo
suma = 0
for x in numeros:
  suma = x+suma 
  print (suma)

##Sumar la lista 
print (sum (numeros))