'''
Ejercicio 3: La universidad requiere un programa para organizar las aulas para los alumnos de primer año, de acuerdo al número de día, sabiendo que 1 es lunes y 6 es sábado.
Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los días cuyo número de orden son pares los alumnos cursan en el aula A-300, mientras que aquellos días impares cursan en el aula A-315.
Además se requiere un programa que otorgue un descuento especial del 25% en el valor de la cuota a aquellos alumnos que deseen cursar en el turno Tarde y se inscriban a más de 3 materias, para el resto de los casos el descuento será de un 5%. El programa debe imprimir el valor de la cuota con descuento de acuerdo al caso.
También se requiere que el programa asigne un costo diario de estacionamiento de $ 300 a aquellos alumnos que vengan en auto o en moto y de $ 50 si vienen en bicicleta.
'''

# print("================ Listado de Aulas ================")
# dia = int(input("Ingrese el número del día (1 Lunes a 6 Sábado): "))

# if dia % 2 == 0:
#     aula = "A-300"
# else:
#     aula = "A-315"

# print("Aula: ", aula)

print()
print("================ Descuentos y Estacionamiento ================")
turno = input("Ingrese el turno (Mañana/Tarde/Noche): ").upper()
materias = int(input("Ingrese la cantidad de materias: "))
vehiculo = input("Ingrese el vehículo en el que se moviliza (Auto/Moto/Bicicleta): ").upper()
cuota = 10000

if turno == "TARDE" and materias > 3:
    cuota = cuota - (cuota * 0.25)
else:
    cuota = cuota - (cuota * 0.05)
print(f"El valor de la cuota es: {cuota}")


if vehiculo == "AUTO" or vehiculo == "MOTO":
    costo_estacionamiento = 300
else:
    costo_estacionamiento = 50
print(f"El costo de estacionamiento para {vehiculo} es de ${costo_estacionamiento}")