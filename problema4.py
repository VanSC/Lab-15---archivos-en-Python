#4.	Gestione el proceso de registro y lectura 
# (los dos últimos ejemplos) mediante un menú.
import funcion

estudiantes = []


while True:
    print("----------------------Menu de Registros-----------------------")
    print("*"*62)
    print("Opciones:")
    print("1) Mostrar estudiante")
    print("2) Registrar estudiante")
    print("3) Salir")
    opcion = input("Ingrese una opcion: ")
    print("*"*62)
    
    if opcion == "1":
            funcion.list_students(estudiantes)
    if opcion == "2":
        nombre = input("Ingrese Nombre: ")
        nota1 = int(input("Ingrese Primera nota: "))
        nota2 = int(input("Ingrese Segunda nota: "))
        promedio = (nota1+nota2)/2
        
        if promedio >= 13:
         print("estas aprobado con: ",promedio)
         average = True
        else:
             print("estas desaprobado con: ",promedio)
             average = False
        
        archivo = open("estudiantes.txt", "w")
        archivo.write("Nombre: " + nombre + "\n")
        archivo.write("Nota 1: " + str(nota1) + "\n")
        archivo.write("Nota 2: " + str(nota2) + "\n")
        archivo.write("Promedio: " + str(promedio) + "\n")
        archivo.write("Aprobado: " + str(average) + "\n")
        print("*"*62)

        funcion.students.append(estudiantes, nombre, nota1, nota2,promedio,)
        print("*"*62)
    if opcion == "3":
        print("Hasta luego, nos vemos pronto!")
        break