class Persona:
    hijos = 2 #Atributo de clase desprotegido
    __mascotas = 1 #Atributo de clase protegido

    def __init__(self,nombre, apellido):
        self.nombre = nombre #Atributo de instancia desprotegido
        self.__apellido = apellido  #Atributo de instancia protegido

    def correr(self): #Método público
        print(self.nombre, "corre")

    def __caminar(self): #Método privado
        print(self.nombre, "camina")

    def dar_un_paso(self): #Método público
        self.__caminar() #Método accesible desde el interior

    def devolver_mascotas(self): #Método público
        return self.__mascotas #Atributo accesible desde el interior

    def devolver_apellido(self): #Método público
        return self.__apellido #Atributo accesible desde el interior

#Programa principal
persona1 = Persona("Juan", "Pérez")

#Accedemos a atributos y métodos de clase comunes
print("Nombre:", persona1.nombre) #Imprimimos un atributo de instancia
print("Hijos:", persona1.hijos) #Imprimimos un atributo de clase
persona1.correr() #Llamamos a un método público

#Intentamos acceder a atributos y métodos encapsulados
# print(persona1.__mascotas) #No podemos acceder al atributo de clase encapsulado
# print(persona1.__apellido) #No podemos acceder al atributo de instancia encapsulado
# persona1.__caminar() #No podemos acceder al método encapsulado

#Accedemos a atributos y métodos no protegidos que acceden a los atributos y métodos encapsulados
# persona1.dar_un_paso()
# print("Mascotas:", persona1.devolver_mascotas())
# print("Apellido:", persona1.devolver_apellido())

#Accedemos en atributos y métodos de otra manera (nombre de la clase como "llave de acceso"), no es buena práctica:
# print("Atributo Mascotas:",persona1._Persona__mascotas)
# print("Atributo Apellido:",persona1._Persona__apellido)
# persona1._Persona__caminar()