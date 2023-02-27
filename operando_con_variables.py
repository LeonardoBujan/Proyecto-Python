"""
Operaciones con Variables
"""

# Operaciones entre variables int devuelve un float
A = 10
B = 3
C = A/B
print(C)

# Operaciones entre una variable int y un float devuelve un float
A = 7.5
B = 3
C = A/B
print(C)

# Typecasting para forzar la conversión de una variable en un tipo bien definido
A = 14.0 # a es una variable de tipo float
A = int(A) # es es una variable de tipo int
print(A)

A = 14  # a es una variable de tipo int
A = float(A)  # es es una variable de tipo float
print(A)

# Concatenar cadenas de texto con el símbolo "+"
PRIMERTEXTO = "El día está nublado"
SEGUNDOTEXTO = "no podemos tomar sol"
FRASECOMPLETA = PRIMERTEXTO + " y " + SEGUNDOTEXTO
print(FRASECOMPLETA)

# Concatenar variables númericas en una cadena de texto str(int)
MENSAJE = "El equipo más goleador de la fecha hizo "
GOLES = 5
FRASEFINAL = MENSAJE + str(GOLES) + " goles"
print(FRASEFINAL)
