# ----------------------------------------------------------------------------------

# Trabajo Integrador -- Programación 1
# Alumnos: Franco Detarsio y Agustin Pieve

# ----------------------------------------------------------------------------------

# inicializacion de variables

opcion_menu = ""

# Definición de funciones

def verificar_inputs(opcion):
    """

    Verifica si el input ingresado sea un número entero

    Args:
        Dato: opcion ingresada por el usuario

    Return:
        Valor en número entero

    """

    while not(opcion.isdigit()):
        print("El valor ingresado no corresponde con un número entero")
        opcion = input("Ingrese nuevamente el valor deseado: ")

    if opcion.isdigit():
        opcion = int(opcion)

    return opcion

def lectura_csv(lista):
    """

    obtiene la información de "Base_de_Datos.csv"

    Args:
        Dato: Archivo.csv

    Returns:
        lista de diccionarios con el contenido del archivo.csv
    """

    with open("Base_de_Datos.csv", "r") as archivo:
        lineas = archivo.readlines() # .readlines() lee todas las líneas del archivo y las guarda en una lista de strings
        for linea in lineas[1:]: # [1:] con esto evitamos el encabezado del archivo.csv
            fila = linea.strip().split(',')
            lista.append({"nombre": fila[0], "poblacion": fila[1], "superficie": fila[2], "continente": fila[3]},)

def filtro_continente(lista, continente):
    """

    Filtra la lista en base al continente ingresado y avisa en caso de error

    Args:
        Datos: lista actualizada del archivo.csv y continente filtro ingresado por el usuario

    Returns:
        Lista filtrada de paises por continente o notifica si no se encuentra

    """

    bandera = False

    for i in lista:
        if i["continente"] == continente:
            print(f"• País: {i["nombre"]} | Población: {i["poblacion"]} | Superficie: {i["superficie"]}km²")
            bandera = True

    if bandera == False:
        print("El continente ingresado no se encuentra en la lista")

def filtro_rango_pob(lista, rango1, rango2):
    """

    Filtra la lista en base a un rango de población fijado por el usuario y verifica cual es el rango mínimo y cual es el rango máximo

    Args:
        Datos: lista actualizada del archivo.csv, rangos ingresados por el usuario

    Returns:
        Lista Filtrada por rango de población, notifica si no se encuentra o si los rangos son iguales

    """
    rango1 = int(rango1)
    rango2 = int(rango2) 

    if rango1 != rango2:# verifica que los rangos no sean iguales
        if rango1 > rango2: # nos aseguramos que rango es el minimo y cual es el maximo
            min = rango2
            max = rango1
        else:
            min = rango1
            max = rango2

        bandera = False

        for i in lista:
            poblacion = int(i["poblacion"]) # pasamos el valor a entero para evaluar

            if (poblacion >= min) and (poblacion <= max):
                print(f"• País: {i["nombre"]} | Población: {i["poblacion"]} | Superficie: {i["superficie"]}km² | Continente: {i["continente"]}")
                bandera = True

        if bandera == False:
            print("El continente ingresado no se encuentra en la lista")
    else:
        print("Los rangos ingresados son iguales\nIntente nuevamente con un rango mínimo y un rango máximo distintos.")



# Aclaraciones
# A lo largo del programa se usara "i" como iterador y marcador de indice
# Se utilizará .strip() y .capitalize() para asegurarnos que las entradas tengan la misma escritura que la lista

# ----- Programa Principal -----

print("¡Bienvenido/a al Gestor Informático de Países")
print("Navegue por nuestro menú ingresando el número corrrespondiente.\n")


# Bucle principal que mostrará un menú gráfico hasta que el usuaio decida salir
while opcion_menu != '5':

    lista_paises = [] # Reiniciamos la lista para evitar duplicación de datos, y trabajar siempre en base al archivo.csv original

    # Menú Gráfico
    print("======== Gestor Informático de Países ========")
    print("|                                            |")
    print("|           1. Buscar País                   |")
    print("|           2. Filtrar países                |")
    print("|           3. Ordenar Países                |")
    print("|           4. Mostrar estadísticas          |")
    print("|           5. Salir                         |")
    print("|                                            |")
    print("==============================================\n")

    opcion_menu = input("_ ").strip()
    print("")

    match opcion_menu:
        case '1':
            pais = input("Ingrese el nombre del país que desea buscar: ").strip().capitalize()
            lectura_csv(lista_paises) # obtenemos los datos desde la funcion

            bandera = False # usamos bandera para mostrar mensaje al usuario en caso de no encontrar el país ingresado
            for i in lista_paises:
                if i["nombre"] == pais:
                    print(f"{i["nombre"]} cuenta con una población de {i["poblacion"]}, una superficie de {i["superficie"]}km² y esta ubicado en el continente de {i["continente"]}")
                    bandera = True

            if bandera == False:
                print("El país ingresado no se encuentra en la lista")

        case '2':
            print("Ingrese el número corresponidente al filtro que desea aplicar.")
            opcion = input("1 - Continente\n2 - Rango de Población\n3 - Rango de Superficie\n_").strip()
            opcion = verificar_inputs(opcion) # nos aseguramos que el iinput sea un numero entero
            lectura_csv(lista_paises)
            
            match opcion:
                case 1:
                    continente = input("Ingrese el nombre del continente que desea filtrar: ").strip().capitalize()
                    filtro_continente(lista_paises, continente)
                    print("")

                case 2:
                    rango1 = input("Ingrese el primer valor correspondiente al rango mínimo: ")
                    verificar_inputs(rango1)
                    print("")
                    rango2 = input("Ingrese el segundo valor correspondiente al rango máximo: ")
                    verificar_inputs(rango2)
                    

                    filtro_rango_pob(lista_paises, rango1, rango2)


                case 3:
                    pass



                case _:
                    print("El número ingresado no corresponde con las opciones\nIntente nuevamente.")

        case '3':
            pass

        case '4':
            pass

        case '5':
            print("================== Salir ==================")
            print("¡Gracias por usar el Gestor Informático de Países!\nHasta Luego.")

        case _:
            print("Opción invalida, intente nuevamente\nRecuerde usar un número (1 - 5)")
    
    print("") # salto de linea luego de cada iteración