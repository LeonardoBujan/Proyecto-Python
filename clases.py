"""
Definición de Clases
"""
class Persona:
    """Clase Persona"""
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

persona1 = Persona("Leonardo", 36, 1.72)

print(persona1.nombre)
print(persona1.edad)
print(persona1.altura)
