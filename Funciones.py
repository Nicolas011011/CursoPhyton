
##Para crear una funcion se utiliza def y el nombre de la funcion que quieres crear con la cantidad de variables que quieres ingresar 
def sumar(a,b): 
    ##Posteriormente se realiza la funcion para lo que la vamos a utilizar y se imprime 
    suma= a+b
    print (suma)

##Aqui estamos mandando llamar la funcion anteriormente creada y colocando valores a las variables
##sumar(5,10)
##sumar (34,23)
##Como solo creamos dos variables, solo podemos meter 2 datos 

##Ej programa con base en el numero dado regrese su tabla de multiplicar 

def tabla (a):
        a= str(a)
        validar = a.isnumeric()
        if validar==True:
            for x in range (11):
                multi = int(a)*x
                print (multi)
        else:
            print ("No se puede multiplicar")
        
        
##tabla ("2")

    
def mult(a,b):
     multip = a*b
     ## El return ejecuta la funcion y guarda el resultado para usarlo en otra parte en el codigo, regresa (return) el dato
     return multip

mult1 = mult (6,2)
print (mult1*10)