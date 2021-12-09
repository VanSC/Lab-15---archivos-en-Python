def list_students(estudiantes):
    print("Lista de estudiantes")
    print(estudiantes)
   
def students(estudiantes, nombre, nota1, nota2, promedio, aprobado):
    
    registro = {
        'nombre': nombre,
        'nota1': nota1,
        'nota2': nota2,
        'Promedio': promedio,
        'Aprobado': aprobado,
    }

    estudiantes.append(registro)
    print("----- Estudiante registrado -----")
    return estudiantes
