#3.	Mediante un programa en Python lea el archivo creado previamente.
archivo = open ("file1.txt" , "a")
anotes = input("Ingresa una texto: ")
archivo.write (anotes)
archivo.close()
texto = open ("file1.txt" , "r")
print(texto.read())
archivo.close()