a = "manzana"

# Retorna la longitud de un elemento
longitudVariable = len(a)
print(longitudVariable)

# Retorna el tipo de una variable
tipoVariable = type(a)
print(tipoVariable)

b = 2
c = 4
# Retorna el valor de calcular a elevado a b, equivalente a escribir a**b
resultadoPotencia = pow(b, c)
print(resultadoPotencia)

# Retorna el valor absoluto de un número
d = -500
valorAbsoluto = abs(d)
print(valorAbsoluto)

# Definición de funciones
def sumarNumeros(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

num1 = 10
num2 = 15
print("El resultado de sumar ", num1, " + ", num2, " es igual a: ", sumarNumeros(num1, num2))

