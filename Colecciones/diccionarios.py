cuentas = {"Leonardo Bujan":3000, "Alberto Castillo": 1500, "María Gomez": 670.25}
print(cuentas)

# Incrementa el valor de la clave especificada
cuentas["Leonardo Bujan"] += 5000
print(cuentas)

# Elimina el elemento especificado del diccionario
cuentas.pop("María Gomez")
print(cuentas)

# Obtiene la longitud del diccionario
print(len(cuentas))
