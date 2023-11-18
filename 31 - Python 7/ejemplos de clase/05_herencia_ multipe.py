#Herencia múltiple

class Padre(): #Superclase
    def __init__(self):
        self.apellido = "Pérez"

    def llevar(self):
        print(f"Mi papá me lleva al colegio.")

    
    def programar(self):
        print(f"Papá programa en JAVA.")


class Madre(): #"Superclase"
    def __init__(self):
        self.apellido = "Osorio"

    def retirar(self):
        print(f"Mamá me retira del colegio")
    
    def programar(self):
        print(f"Mamá programa en Python.")


class Hijo(Madre, Padre):
    nombre = ""


    def jugar(self):
        print(f"Soy {self.nombre} {self.apellido} y juego al voley.")

#Programa Principal
hijo1 = Hijo()
hijo1.nombre = "Fernando"
hijo1.jugar()
hijo1.llevar()
hijo1.retirar()
hijo1.programar()
