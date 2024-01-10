## Condicionales

num = 5
bool1 = False

##Para los valores condicionales se usa esta sintaxis depende cual sea mas util

##Simbologia == (Pra declarar igualdad)
##             <= menor o igual
##             >= mayot o igual 

## Sintaxis 1:      if + variable + signo + valor condicional + :       (Utilidad numerica)
if num >= 5: 
    print ("soy mayor a 5")
if num < 5: 
    print ("soy menor a 5")

##Sintaxis 2:     if or else // misma sintaxis 
if num > 5: 
    print ("soy mayor a 5")
else:
    print ("soy igual 5")

##Sintaxis 3:  if or elif ( else if )      Si no se cumple el primer if se lee elif, si tampoco se cumple, se muestra else   //misma sintaxis
if num == 5: 
    print ("soy igual a 5")
elif num == 10: 
    print ("soy igual a 10")
else:
    print ("no se cumple ninguna condicion")

##Sintaxis 4 Booleano 
if bool1 == True:
    print ("verdadero")
else:
    print ("falso")

## Sintaxis 4 resumida (Primero el if para booleanos evalua siempre True y despues False)
if bool1:
    print ("falso")
else:
    print ("verdadero")

