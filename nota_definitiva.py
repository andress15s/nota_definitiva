print("------------------")
print("--notas semestre--")
print("------------------")


#Entrada 
cod = int(input("Ingrese el codigo del estudiante "))
nombre = input("ingrese el nombre del estudiante: ")


if cod != 0:
  not1 = int(input("Ingrese nota 1 "))
  not2 = int(input("Ingrese nota 2 "))
  not3 = int(input("Ingrese nota 3 "))

else: 
  print("Fin de los datos de entrada.")

#procesamiento
reprobados = 0

while cod != 0:
    Nfin = (not1 + not2 + not3)/3
    print("El estudiante de codigo : ", str(cod) + ", cuyo nombre es" + nombre + "obtuvo una nota definitiva de " + str(Nfin))
    print("La nota final es: ", str(Nfin))

    if Nfin < 3 :
      reprobados = reprobados + 1

  # entrada
    cod = int(input("Ingrese el codigo del estudiante "))
    nombre = input("ingrese el nombre del estudiante: ")

    if cod != 0:
      not1 = float(input("Ingrese nota 1 "))
      not2 = float(input("Ingrese nota 2 "))
      not3 = float(input("Ingrese nota 3 "))

    else:
      print("FIN  de los datos de entrada.")

#salida
print("cantidad de estudiantes reprobados: "+ str(reprobados))