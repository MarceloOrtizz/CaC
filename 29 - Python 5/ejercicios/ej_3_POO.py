'''
3. Crear una clase que represente una Materia de la universidad. Definir como atributos su nombre, carrera, duración en meses y un atributo de clase booleano para definir que todas las materias no son promocionables. Desarrollar un método __init__ para incializarlos. Crear un método para imprimir los datos del objeto, luego sustituirlo por el método __str__(). Crear dos objetos. Eliminar uno de ellos a través del método __del__().
'''

class Materia:

    promocionable = False #Atributo de clase

    #nuevo método constructor
    def __init__(self, nombre, carrera, duracion):
        self.nombre = nombre
        self.carrera = carrera
        self.duracion = duracion

    def imprimir(self):
        print(f"Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuración: {self.duracion} años\nPromocionable: {self.promocionable}")

    def __str__(self):
        return f"Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuración: {self.duracion} años\nPromocionable: {self.promocionable}"
    
    def __del__(self): #Elimina un objeto
        print(f"{self.nombre} ha sido eliminado.")


#Programa Principal
materia1 = Materia("introd a python", "ing en informática", 4)
#materia1.imprimir()
print(materia1)
print()

materia2 = Materia("inteligencia artificial", "ing en informática", 6)
materia2.promocionable = True
print(materia2)
print()