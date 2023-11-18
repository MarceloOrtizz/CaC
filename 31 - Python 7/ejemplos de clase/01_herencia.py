class Padre(): #Superclase
    def __init__(self):
        self.apellido = "Argento"

    def hacer_deporte(self):
        print(f"Estoy haciendo deporte.")


class Hijo(Padre): #subclase
    nombre = ""

    def jugar(self):
        print(f"Soy {self.nombre} y estoy jugando al fútbol.")


#Programa principal

hijo1 = Hijo()
hijo1.nombre = "coqui"
hijo1.hacer_deporte() #método del padre
hijo1.jugar() #método propio

#Imprimimos artibutos heredados del padre y propios
print(f"El hijo se llama {hijo1.nombre} {hijo1.apellido}")