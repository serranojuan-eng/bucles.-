#4.2fundamentos de programacion 

cantidad= int(input("ingrese la cantidad de estudiantes:"))
aprobados = 0
reprobados = 0
suma_notas = 0

for i in range (cantidad):
    codigo = input("ingrese el codigo del estudiante:")
    nota = float (input("ingrese la nota del estudiante:"))

suma_notas += nota

if nota >= 3.0:
    aprobados += 1
else:
    reprobados += 1

promedio = suma_notas/ cantidad

print("resulatdos del grupo")
print("estudiantes aprobados", aprobados)
print("estudiantes reprobados", reprobados)
print("promedio general del grupo", promedio)



