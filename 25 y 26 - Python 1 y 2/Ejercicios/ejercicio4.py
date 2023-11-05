'''
Ejercicio 4: La universidad ha decidido desarrollar un programa que muestre en dos columnas el número de día y el aula, de acuerdo al número de día par o impar desarrollado en el ejercicio anterior. Imprimir el listado como el siguiente:
Día Aula
1   A-315
2   A-300
...
5   A-315
6   A-300
Además se desea mejorar el sistema de carga de edades, validando que correspondan a mayores de edad. Desarrollar un programa que solicite edades válidas e imprima la edad ingresada y cuántas cargas erróneas se realizaron.

También se requiere cargar las notas de 5 alumnos y obtener el promedio (for). Nota: Al usar for probar cómo se podría plantear el ejercicio usando 1, 2 o 3 parámetros.

Finalmente se desea imprimir el costo del comedor. La cuota vale $ 1250 por día y se desea imprimir un informe que muestre la cantidad de días (de 1 a 6) y el costo total (for). Por ejemplo: 1 día cuesta $ 1250, 2 días cuestan $ 2500...

'''

print("============== Listado de Aulas =============")
print("Día\tAula")

cont = 1
while cont <= 6:
    print(cont, end='')

    if cont % 2 == 0:
        print("\tA-300")
    else:
        print("\tA-315")
    cont+=1


print()
print("================== Carga de Datos ==================")

edad = int(input("Ingrese una edad mayor o igual a 18: "))

cont_carga_erronea = 0
while edad < 18:
    cont_carga_erronea +=1 #contador
    edad = int(input("Error!. Ingrese una edad mayor o igual a 18: "))
print(f"La edad ingresada es: {edad}")
print(f"Se ha ingresado la edad de manera errónea {cont_carga_erronea} veces")


print()
print("================== Promedio de Notas ==================")

suma = 0
for i in range(5):
    nota = float(input("Ingrese la nota: "))
    suma = suma + nota #Acumulador suma += nota

promedio = suma / (i+1)
print(f"El promedio de notas es {promedio}")


print()
print("================== Costo del Comedor ==================")

costo_diario = 1250

print("Día\tCosto")
for i in range(6):
    print(i+1,"\t$", (i+1)*costo_diario)