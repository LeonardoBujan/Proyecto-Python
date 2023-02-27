class Persona:
  def __init__(variable, nombre, edad, altura):
    variable.nombre = nombre
    variable.edad = edad
    variable.altura = altura

persona1 = Persona("Leonardo", 36, 1.72)

print(persona1.nombre)
print(persona1.edad)
print(persona1.altura)