## Para recibir datos del usuario se usa input() es la manera en la que se llaman a las funciones
coche = input("Escribe el modelo de tu coche\n")
print (coche)


##Ejemplo con if,operadores aritmeticos e input

datos = input("ingresa un numero\n")
## La funcion para identificar un dato numerico es:  .isnumeric() 
##La valiable validar fue creada para corroborar que los datos solicitados sean numericos
validar = datos.isnumeric()
##print (validar)
## No olvidar despues de True o False los "dos puntos"
if validar==True:
    mult = int(datos)*10
    print (mult)
else:
    print ("Esto no es un valor numerico")
