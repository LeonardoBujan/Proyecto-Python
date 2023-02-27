# Operaciones entre variables int devuelve un float
a = 10
b = 3
c = a/b
print(c)

# Operaciones entre una variable int y un float devuelve un float
a = 7.5
b = 3
c = a/b
print(c)

# Typecasting para forzar la conversión de una variable en un tipo bien definido
a = 14.0 # a es una variable de tipo float
a = int(a) # es es una variable de tipo int
print(a) 

a = 14  # a es una variable de tipo int
a = float(a)  # es es una variable de tipo float
print(a)

# Concatenar cadenas de texto con el símbolo "+"
primerTexto = "El día está nublado"
segundoTexto = "no podemos tomar sol"
fraseCompleta = primerTexto + " y " + segundoTexto
print(fraseCompleta)

# Concatenar variables númericas en una cadena de texto str(int)
mensaje = "El equipo más goleador de la fecha hizo "
goles = 5
fraseFinal = mensaje + str(goles) + " goles"
print(fraseFinal)