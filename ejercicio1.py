def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias):
    try:
        cantidad = int(copias)
        return cantidad >= 0 
    except ValueError:
        return False
    
def validar_prestamo(prestamos):
    try:
        cantidad = int(prestamos)
        return cantidad > 0
    except ValueError:
        return False
    
def mostrar_menu():
    print("\n------- Menu Principal --------")
    print("1. agregar libro")
    print("2. buscar libro")
    print("3. eliminar libro")
    print("4. actualizar disponibilidad")
    print("5. mostrar libros")
    print("6. salir")
    print("---------------------------------")

def leer_opcion():
    while True:
        try:
            opcion = int(input("seleccione una opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("opcion invalida. ingrese un numero entre el 1 y el 6.")
        except ValueError:
            print("debe ingrear un numero entero")

def agregar_libro(libros):
    titulo = input("ingrese el nombre del libro: ")
    copias = input("ingrese la cantidad de copias: ")
    prestamo = input("ingrese el periodo de presatamo del libro: ")
    if not validar_titulo(titulo):
        print("error: el nombre no pouede estar vacio ni ser solo espacios en blanco.")
        return
    if not validar_copias(copias):
        print("error: las copias deben ser un numero entero mayor o iogual a cero.")
        return
    if not validar_prestamo(prestamo):
        print("error: el periodo de prestamo debe ser un numero entero mayor que cero.")
        return

    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias),
        "prestamo": int(prestamo),
        "disponible": False
    }  
    libros.append(libro)
    print(f"Libro {titulo.strip()} agregado exitosamente.")

def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros [i]["titulo"].lower() == titulo.lower():
            return i
    return -1

def eliminar_libros(libros):
    titulo = input("ingrese el nombre del libro a eliminar: ")
    posicion = buscar_libro(libros, titulo)
    if posicion != -1:
        libros.pop(posicion)
        print(f"libro {titulo} eliminado correctamente.")
    else:
        print(f"el libro {titulo} no se encuentra registrado")

def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
           libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(libros):
    actualizar_disponibilidad(libros)
    if len(libros) == 0:
        print("no hay libros registrados. ")
        return
    print("\n---- Lista de Libros ----")
    for libro in libros:
        print(f"titulo: {libro['titulo']}")
        print(f"copias: {libro['copias']}")
        print(f"prestamo: {libro['prestamo']}")
        if libro["disponible"]:
            print("estado: Disponible")
        else:
            print("estado: No Copias")
        print("---------------------------------")

libros = []
menu = True
while menu:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        titulo = input("ingrese el nombre del libro a buscar: ")
        posicion = buscar_libro (libros, titulo)
        if posicion != -1:
            print(f"libro encontrado en la posicion {posicion}")
            print(f"titulo: {libros[posicion]['titulo']}")
            print(f"copias: {libros[posicion]['copias']}")
            print(f"prestamo: {libros[posicion]['prestamo']}")
            if libros[posicion]["disponible"]:
                print("estado: Disponible")
            else:
                print("estado: Sin Copias")
            
    
        else:
             print(f"el libro '{titulo}' no se encuentra registrado")

    elif opcion == 3:
        eliminar_libros(libros)
    
    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("disponibilidad actualizada correctamente.")

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema.")
        menu = False