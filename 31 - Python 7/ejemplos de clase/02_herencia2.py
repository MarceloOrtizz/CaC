class Vehiculo(): #Superclase
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}"
    
    def andar(self):
        print(f"Estoy andando en {self.ruedas} ruedas.")


class Transporte(Vehiculo):
    def __init__(self, color, ruedas, velocidad, modelo, tipo):
        Vehiculo.__init__(self, color, ruedas) #atributos heredados
        self.velocidad = velocidad
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + f"\nTipo: {self.tipo.upper()}\nVelocidad: {self.velocidad} km/h\nModelo: {self.modelo}"
    
#programa Principal
vehiculo1 = Vehiculo("Rojo", 2) #Instancia del padre
print(vehiculo1)
print()

auto1= Transporte("Azul", 4, 150,"Ford", "Auto")
print(auto1)