#2.	Crear un programa en Pyhon que lea tu nombre, curso, 
# 2 notas, calcule el promedio y la condicion. Posterior 
# a él que imprima la fecha actual de registro, el nombre
#  y la condición además que se guarden en un archivo de 
# texto la fecha actual, el nombre, curso, promedio y condición.


name = input("Enter your name: ")
first_note = int(input("Enter first note: "))
Second_note = int(input("Enter second note: "))

average = (first_note + Second_note)/2

approved = False

if average >= 13:
    approved = True

#Save on the file "notas.txt"

file = open("notas.txt", "w")
file.write("Name: " + name +"\n")
file.write("First_note: " + str(first_note) +"\n")
file.write("Second_name: " + str(Second_note) +"\n")
file.write("Average: " + str(average) +"\n")
file.write("Approved: " + str(approved) +"\n")

file.close()