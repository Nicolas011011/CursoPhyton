## el diccionario nos permite meter distintos elementos en un orden, el cual a la hora de imprimirlo 
##podemos obtener el objeto que queramos siempre y cuando se especifique la posicion y el orden
              
diccionario = {"1":"enero",
              "2":"febrero",
              "3":"marzo",
              "4":"abril",
              "lista": [1,2,3,4,5],
              "arreglo":{"listas": [8,9,10,11], "palabras": "hola", "letras": "a,b,c"} 
              }

elemento = diccionario ["1"] 
elemento2 = diccionario ["lista"]
elemento3 = diccionario ["arreglo"] ["listas"][1]
print (elemento)
print (elemento2)
print (elemento3)

##EJ

ejer = {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": True,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
"Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}

elemento4 = ejer ["members"][2]["powers"][3]
print (elemento4)