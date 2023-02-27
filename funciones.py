"""
Definición de funciones
"""

A = "manzana"

# Retorna la longitud de un elemento
LONGITUDVARIABLE = len(A)
print(LONGITUDVARIABLE)

# Retorna el tipo de una variable
TipoVariable = type(A)
print(TipoVariable)

B = 2
C = 4
# Retorna el valor de calcular a elevado a b, equivalente a escribir a**b
ResultadoPotencia = pow(B, C)
print(ResultadoPotencia)

# Retorna el valor absoluto de un número
D = -500
ValorAbsoluto = abs(D)
print(ValorAbsoluto)

# Definición de funciones
def sumar_numeros(valor1, valor2):
    """Funcion que recibe 2 valores como parámetros y retorna como resultado la suma de ambos"""
    Resultado = valor1 + valor2
    return Resultado

NUM1 = 10
NUM2 = 15
print("El resultado de sumar ", NUM1, " + ", NUM2, " es igual a: ", sumar_numeros(NUM1, NUM2))
