'''
Ejercicio 1: Crear un programa que permita registrar las inscripciones de los alumnos de una universidad privada. Debe incluir un título principal, pedir los datos personales (nombre, edad, fecha de nacimiento). Crear una variable que muestre True o False si posee título secundario (ese dato no se pide al usuario, se escribe en el programa).
Además se deberá ingresar el monto de matrícula y calcular la primer cuota (valor de la matrícula + $ 20000 de cuota).
Finalmente se deberán imprimir todos los datos pedidos.
'''

nombre_completo = input("Ingrese su nombre: ") #string
edad = int(input("Ingrese su edad: ")) #int
fec_nac = input("ingrese fecha de nacimiento: ")
titulo = False #boolean

matricula = float(input("Ingrese el monto de la matrícula: ")) #float
cuota = 20000
primer_cuota = matricula + cuota


#Mostramos los datos
print()
print("=======================================================")
print("======== Universidad de Python - Inscripciones ========")
print("=======================================================")
print()
print("DATOS DE INGRESO:")
print("Nombre completo:", nombre_completo)
print("Fecha de Nacimiento:", fec_nac)
print("Edad:", edad)
print("Posee título?:", titulo)
print("Primer cuota a abonar (cuota + matrícula): $", primer_cuota)
print("Valor de cuotas restantes: $", cuota)