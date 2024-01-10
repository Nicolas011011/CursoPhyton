##Para llamar una lista e imprimirla, solamente se ocupa print
numeros = [1,2,3,7,10]
print (numeros)

##Para llamar un dato especifico de la lista se ocupa crear otra variable que tenga el valor de la lista con su respectivo dato que queremos mosstrar
elemento = numeros [0]
print (elemento)

##Para un rango de datos de una lista igual se crea otra variable y se ocupan los "dos puntos" para definir el rango
elementos = numeros [1:3]
print (elementos)

## pop: borra elementos de una lista con una posicion dada
delete = numeros.pop (2)
print (delete)
print (numeros)

## Para eliminar un elemento de una lista se utiliza remove y el elemento que deseamos borrar (un solo valor)
cars = ["Ford","Volvo", "Volvo", "BMW"]
print (cars)
cars.remove("Volvo")
print(cars)

