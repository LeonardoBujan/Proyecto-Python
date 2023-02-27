listaNombres = ["Leonardo", "Rubén", "María", "Pablo"]
print(listaNombres[2])

# Cambia el valor de la posición 2
listaNombres[2] = "Roberto"
print(listaNombres[2])

listaNombres.append("Martín") # Agrega un valor nuevo a la lista en la última posición
listaNombres.insert(0, "Florencia") # Inserta un valor nuevo en la lista en una posición especificada como parámetro

print(listaNombres)

# Imprime el último item
print(listaNombres[-1])

# Accede a un rango de la lista, desde la segunda posición a la tercera
print(listaNombres[1:3])

# Accede a la lista hasta de la segunda posicion
print(listaNombres[:2])

# Accede al índice de la lista a través del valor almacenado
print(listaNombres.index("Leonardo"))

listaNombresNuevos = ["Franco", "Celeste", "Romina"]

# Concatena dos listas
listaNombres.extend(listaNombresNuevos)
print(listaNombres)

# Longitud de la lista
print(len(listaNombres))

# El método remove() elimina el elemento especificado
listaNombres.remove("Leonardo")
print(listaNombres)

# El método pop() elimina el índice especificado de la lista
listaNombresNuevos.pop(1)
print(listaNombresNuevos)

# Si no se especifica el índice, el método pop() elimina el último item de la lista
listaNombres.pop()
print(listaNombres)

# La palabra clave del también elimina el índice especificado
del listaNombres[0]
print(listaNombres)

# La palabra clave del también puede eliminar la lista por completo
listaApellidos = ["Rodriguez", "Mendez", "Bravo"]
print(listaApellidos)
del listaApellidos

# El método clear() vacía la lista
listaNombresNuevos.clear()
print(listaNombresNuevos)
