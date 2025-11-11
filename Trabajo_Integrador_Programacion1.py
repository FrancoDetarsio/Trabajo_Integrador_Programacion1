# ----------------------------------------------------------------------------------

# Trabajo Integrador -- Programación 1
# Alumnos: Franco Detarsio y Agustín Pieve

# ----------------------------------------------------------------------------------


# inicializacion de variables

opcion_menu = ""

# Bloque -- Definición de funciones


# Funciones de verificación

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
        opcion = input("Ingrese nuevamente el valor deseado.\n► ")

    if opcion.isdigit():
        opcion = int(opcion)

    return opcion

def verificar_duplicado(lista, pais):
    """

    Verifica si el país existe en la lista

    Args:
        Datos: País que ingresa el usuario

    Returns:
        Si existe devolvera True, de lo contrario devolverá False

    """

    existe = False

    for i in lista:
        if pais in i["nombre"]:
            existe = True

    return existe



# Funciones de Lectura y escritura de Datos

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

def agregar_pais(pais):
    """

    permite al usuario añadir un pais y los demas datos correspondientes a este al archivo.csv
    se asegura que no se ingresen datos incorrectos o vacios

    Args:
    Datos: 
        de entrada - país
        dentro de la función - población, superficie, continente

    Returns:
        Se añadirá al archivo.csv la información dada y se mostrará una confirmación

    """
    
    poblacion = input(f"Ingrese la población correspondiente a {pais}\n► ").strip()
    poblacion = verificar_inputs(poblacion)

    # nos aseguramos que no ingrese un valor vacío
    while poblacion == 0:
        poblacion = input("El valor ingresado para población no puede ser '0'\nIngrese el valor nuevamente\n► ").strip()
        poblacion = verificar_inputs(poblacion)

    superficie = input(f"Ingrese la superficie correspondiente a {pais} (km²)\n► ").strip()
    superficie = verificar_inputs(superficie)

    # nos aseguramos que no ingrese un valor vacío
    while superficie == 0:
        superficie = input("El valor ingresado para superficie no puede ser '0'\nIngrese el valor nuevamente\n► ").strip()
        superficie = verificar_inputs(superficie)

    continente = input(f"Ingrese el continente correspondiente a {pais}\n► ")

    while not(continente.isalpha()):
        continente = input("El valor que ingresó para continente no es válido\nIngreselo nuevamente\n► ").strip()

    # Agregamos los datos juntados al archivo.csv
    with open("Base_de_Datos.csv", "a") as archivo:
        archivo.write(f"{pais},{poblacion},{superficie},{continente}\n")
    
    print("País guardado Exitosamente")

def agregar_pob_sup(lista, pais):
    """

    Permite actualizar los valores de poblacion y superficie de un país existente en el archivo.csv
    verifica que no se ingresen valores vacíos

    Datos: 
        lista actualizada del archivo.csv y país que se  desea actualizar

    Returns:
        país en el archivo.csv actualizado
        mensaje de confirmación al usuario

    """

    poblacion = input(f"Ingrese la población actualizada para {pais}\n► ").strip()
    poblacion = verificar_inputs(poblacion)

    # nos aseguramos que no ingrese un valor vacío
    while poblacion == 0:
        poblacion = input("El valor ingresado para población no puede ser '0'\nIngrese el valor nuevamente\n► ").strip()
        poblacion = verificar_inputs(poblacion)

    superficie = input(f"Ingrese la superficie actualizada para {pais} (km²)\n► ").strip()
    superficie = verificar_inputs(superficie)

    # nos aseguramos que no ingrese un valor vacío
    while superficie == 0:
        superficie = input("El valor ingresado para superficie no puede ser '0'\nIngrese el valor nuevamente\n► ").strip()
        superficie = verificar_inputs(superficie)

    # reescribimos el archivo.csv para actualizar los datos necesarios
    with open("Base_de_Datos.csv", "w") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n") # encabezado de archivo.csv
        
        for i in lista:
            if i["nombre"] == pais: # si la fila coincide con el país la actualizamos
                i["poblacion"] = poblacion
                i["superficie"] = superficie
            
            # vamos cargando los datos al archivo.csv
            archivo.write(f"{i["nombre"]},{i["poblacion"]},{i["superficie"]},{i["continente"]}\n")

    print("Datos actualizados exitosamente.")



# Funciones de Filtro

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
            print("No hay países que se encuentren dentro del rango de población ingresado")
    else:
        print("Los rangos ingresados son iguales\nIntente nuevamente con un rango mínimo y un rango máximo distintos.")

def filtro_rango_sup(lista, rango1, rango2):
    """

    Filtra la lista en base a un rango de superficie fijado por el usuario y verifica cual es el rango mínimo y cual es el rango máximo

    Args:
        Datos: lista actualizada del archivo.csv, rangos ingresados por el usuario

    Returns:
        Lista Filtrada por rango de población, notifica si no se encuentra o si los rangos son iguales

    """

    if rango1 != rango2:# verifica que los rangos no sean iguales
        if rango1 > rango2: # nos aseguramos que rango es el minimo y cual es el maximo
            min = rango2
            max = rango1
        else:
            min = rango1
            max = rango2

        bandera = False

        for i in lista:
            superficie = int(i["superficie"]) # pasamos el valor a entero para evaluar

            if (superficie >= min) and (superficie <= max):
                print(f"• País: {i["nombre"]} | Población: {i["poblacion"]} | Superficie: {i["superficie"]}km² | Continente: {i["continente"]}")
                bandera = True

        if bandera == False:
            print("No hay países que se encuentren dentro del rango de población ingresado")
    else:
        print("Los rangos ingresados son iguales\nIntente nuevamente con un rango mínimo y un rango máximo distintos.")



# Funciones de Ordenamiento

def ordenar_por_nombre(lista, opcion):
    """
    Ordena la lista de países por nombre, ascendente o descendente.
    
    Args:
        Datos: lista actualizada del archivo.csv y opcion elegida por el usuario

    Returns:
        si la opcion = '1' → lista ascendente por nombre
        si la opcion = '2' → lista descendente por nombre

    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            nombre_i = lista[i]["nombre"].lower()
            nombre_j = lista[j]["nombre"].lower()

            if opcion == '1':  # ascendente
                if nombre_i > nombre_j:
                    lista[i], lista[j] = lista[j], lista[i]
            elif opcion == '2':  # descendente
                if nombre_i < nombre_j:
                    lista[i], lista[j] = lista[j], lista[i]

    # Mostramos el resultado en pantalla
    if opcion == '1':
        print("\nPaíses ordenados por nombre ascendente:")
        for pais in lista:
            print(f"• País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² |  Continente: {pais['continente']}")
    elif opcion == '2':
        print("\nPaíses ordenados por nombre descendente:")
        for pais in lista:
            print(f"• País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² |  Continente: {pais['continente']}")
    else:
        print("\nPor favor, ingrese un número válido del menú para ordenar ascendente o descendentemente.")   

def ordenar_por_poblacion(lista, opcion):
    """
    Ordena la lista de países por población, ascendente o descendente.
    
    Args:
        Datos: lista actualizada del archivo.csv y opcion elegida por el usuario

    Returns:
        si la opcion = '1' → lista ascendente por población
        si la opcion = '2' → lista descendente por población

    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            # Convertimos los valores a enteros para comparar correctamente
            poblacion_i = int(lista[i]["poblacion"])
            poblacion_j = int(lista[j]["poblacion"])

            if opcion == '1':  # ascendente
                if poblacion_i > poblacion_j:
                    lista[i], lista[j] = lista[j], lista[i]
            elif opcion == '2':  # descendente
                if poblacion_i < poblacion_j:
                    lista[i], lista[j] = lista[j], lista[i]

    # Mostramos el resultado ordenado
    if opcion == '1':
        print("\nPaíses ordenados por población:")
        for pais in lista:
            print(f"• País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")  
    elif opcion == '2':
        print("\nPaíses ordenados por población:")
        for pais in lista:
            print(f"• País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")  
    else:
        print("Por favor, ingrese un número válido del menú para ordenar ascendente o descendentemente.")

def ordenar_por_superficie(lista, opcion):
    """
    Ordena la lista de países por Superficie, ascendente o descendente.
    
    Args:
        Datos: lista actualizada del archivo.csv y opcion elegida por el usuario

    Returns:
        si la opcion = '1' → lista ascendente por superficie
        si la opcion = '2' → lista descendente por superficie
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            # Convertimos los valores a enteros para comparar correctamente
            superficie_i = int(lista[i]["superficie"])
            superficie_j = int(lista[j]["superficie"])

            if opcion == '1':  # ascendente
                if superficie_i > superficie_j:
                    lista[i], lista[j] = lista[j], lista[i]
            elif opcion == '2':  # descendente
                if superficie_i < superficie_j:
                    lista[i], lista[j] = lista[j], lista[i]

    # Mostramos el resultado ordenado
    if opcion == '1':
        print("\nPaíses ordenados por superficie:")
        for pais in lista:
            print(f"• País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")  
    elif opcion == '2':
        print("\nPaíses ordenados por población:")
        for pais in lista:
            print(f"• País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")  
    else:
        print("Por favor, ingrese un número válido del menú para ordenar ascendente o descendentemente.")



#  Funciones de Estadística

def mayor_menor_pob(lista):
    """

    Búsca y muestra por pantalla los países de menor y mayor población

    Args:
        Dato: Lista
    
    Returns:
        Print país con mayor y menor población

    """

    # Definimos variables con valores superiores a los presentes en la lista a las que les asignaremos que país mostrar
    mayor = float("-inf")
    menor = float("inf")

    for i in lista:
        poblacion = int(i["poblacion"]) # Pasamos el valor a entero para poder comparar

        if poblacion < menor:
            menor = poblacion # dejamos registrado cual fue el valor menor para la siguiente iteracion

            # registramos en 4 variables los valores de la fila actual
            men1, men2, men3, men4 = i["nombre"], i["poblacion"], i["superficie"], i["continente"]

        if poblacion > mayor:
            mayor = poblacion # dejamos registrado cual fue el valor mayor para la siguiente iteracion

            # registramos en 4 variables los valores de la fila actual
            may1, may2, may3, may4 = i["nombre"], i["poblacion"], i["superficie"], i["continente"]

    # Mostramos resultados
    print("Los países con Mayor y Menor Población son:\n")
    print(f"• Menor → País: {men1} | Población: {men2} | Superficie: {men3}km² | Continente: {men4}\n")
    print(f"• Mayor → País: {may1} | Población: {may2} | Superficie: {may3}km² | Continente: {may4}")

def promedio_poblacion(lista):
    """

    Múestra el promedio de población de los países dentro del archivo.csv

    Args:
        Dato: lista actualizada del archivo.csv
    
    Returns:
        promedio de población

    """
    # iniciamos variables que servirán de apoyo a la función
    contador = 0
    suma = 0

    for i in lista:
        contador += 1 # cuenta la cantidad de países en la lista para hacer promedio
        poblacion = int(i["poblacion"]) # pasamos la poblacion a entero para luego sumar el total
        suma += poblacion

    # calculamos el promedio de poblacion
    promedio = int(suma / contador) # int para obtener la parte entera

    return promedio

def promedio_superficie(lista):
    """

    Múestra el promedio de superficie de los países dentro del archivo.csv

    Args:
        Dato: lista actualizada del archivo.csv
    
    Returns:
        promedio de superficie

    """
    # iniciamos variables que servirán de apoyo a la función
    contador = 0
    suma = 0

    for i in lista:
        contador += 1 # cuenta la cantidad de países en la lista para hacer promedio
        superficie = int(i["superficie"]) # pasamos la superficie a entero para luego sumar el total
        suma += superficie

    # calculamos el promedio de superficie
    promedio = int(suma / contador) # int para obtener la parte entera

    return promedio

def pais_por_continente(lista, continente):
    """

    Cuenta la cantidad de países que pertenecen a el continente que ingresa el usuario utilizando archivo.csv

    Args:
        Datos: lista actualizada del archivo.csv y continente ingresado por el usuario

    Returns:
        cantidad de continentes pertenecientes a dicho continente

    """

    contador = 0 # variable que contará los países pertenecientes

    for i in lista:
        # por cada coincidencia sumaremos un país
        if i["continente"] == continente:
            contador += 1

    return contador


# Aclaraciones
# A lo largo del programa se usara "i" como iterador y marcador de indice
# Se utilizará .strip() y .title() para asegurarnos que las entradas tengan la misma escritura que la lista


# ----- Programa Principal -----

print("¡Bienvenido/a al Gestor Informático de Países")
print("Navegue por nuestro menú ingresando el número correspondiente.\n")


# Bucle principal que mostrará un menú gráfico hasta que el usuaio decida salir
while opcion_menu != '7':

    lista_paises = [] # Reiniciamos la lista para evitar duplicación de datos, y trabajar siempre en base al archivo.csv original

    # Menú Gráfico
    print("======== Gestor Informático de Países ========")
    print("|                                            |")
    print("|           1. Agregar un País               |")
    print("|           2. Actualizar (Pob/Sup)          |")
    print("|           3. Buscar País                   |")
    print("|           4. Filtrar Países                |")
    print("|           5. Ordenar Países                |")
    print("|           6. Mostrar Estadísticas          |")
    print("|           7. Salir                         |")
    print("|                                            |")
    print("==============================================\n")

    opcion_menu = input("► ").strip()
    print("")

    match opcion_menu:

        case '1':
            print("============= 1. Agregar un País =============\n")
            lectura_csv(lista_paises) # obtenemos los datos del archivo desde la funcion

            pais = input("Ingrese el nombre del país que desea agregar.\n► ").strip().title()

            if not(pais.isalpha()): # con .isalpha nos aseguramos que no sea un numero o vacío
                print("El valor ingresado no corresponde con uno valido\nIntente nuevamente")
            else:
                if verificar_duplicado(lista_paises, pais): # Verificamos que no este en la lista
                    print(f"{pais} ya esta dentro de la lista.")
                    
                else:
                    agregar_pais(pais) # llamamos a la funcion que pide el resto de datos y añade al .csv

        case '2':
            print("========== 2. Actualizar (Pob/Sup) ==========\n")
            lectura_csv(lista_paises) # obtenemos los datos del archivo desde la funcion

            pais = input("Ingrese el país que desearia actualizar su población y superficie.\n► ").strip().title()

            if not(pais.isalpha()): # con .isalpha nos aseguramos que no sea un numero o vacío
                print("El valor ingresado no corresponde con uno valido\nIntente nuevamente")
                
            else:
                if not(verificar_duplicado(lista_paises, pais)): # verificamos si el país esta en la lista
                    print(f"{pais} no se encuentra en la lista.")

                else:
                    agregar_pob_sup(lista_paises, pais) # Lammamos a la funcion que actualiza pob/sup

        case '3':
            print("================ Buscar País ================\n")

            pais = input("Ingrese el nombre del país que desea buscar.\n► ").strip().title()
            lectura_csv(lista_paises) # obtenemos los datos del archivo desde la funcion
            print("")

            bandera = False # usamos bandera para mostrar mensaje al usuario en caso de no encontrar el país ingresado
            for i in lista_paises:
                if i["nombre"] == pais:
                    print(f"{i["nombre"]} cuenta con una población de {i["poblacion"]}, una superficie de {i["superficie"]}km² y esta ubicado en el continente de {i["continente"]}")
                    bandera = True

            if bandera == False:
                print("El país ingresado no se encuentra en la lista")

        case '4':
            print("=============== Filtrar Países ===============\n")

            print("Ingrese el número corresponidente al filtro que desea aplicar.")
            opcion = input("1 - Continente\n2 - Rango de Población\n3 - Rango de Superficie\n► ").strip()
            opcion = verificar_inputs(opcion) # nos aseguramos que el input sea un numero entero
            lectura_csv(lista_paises)
            
            match opcion:
                case 1:
                    continente = input("Ingrese el nombre del continente que desea filtrar.\n► ").strip().title()
                    filtro_continente(lista_paises, continente)
                    print("")

                case 2:
                    rango1 = input("Ingrese el primer valor correspondiente al rango mínimo.\n► ").strip()
                    rango1 = verificar_inputs(rango1)
                    print("")
                    rango2 = input("Ingrese el segundo valor correspondiente al rango máximo.\n► ").strip()
                    rango2 = verificar_inputs(rango2)
                    
                    filtro_rango_pob(lista_paises, rango1, rango2)

                case 3:
                    rango1 = input("Ingrese el primer valor correspondiente al rango mínimo (km²).\n► ").strip()
                    rango1 = verificar_inputs(rango1)
                    print("")
                    rango2 = input("Ingrese el segundo valor correspondiente al rango máximo (km²).\n► ").strip()
                    rango2 = verificar_inputs(rango2)

                    filtro_rango_sup(lista_paises, rango1, rango2)

                case _:
                    print("El número ingresado no corresponde con las opciones\nIntente nuevamente.")

        case '5':
            print("=============== Ordenar Países ===============\n")

            print("Ingrese el número corresponidente al ordenamiento que desea aplicar.")
            opcion = input("1 - Por Nombre\n2 - Por Población\n3 - Por Superficie\n► ").strip()
            opcion = verificar_inputs(opcion) # nos aseguramos que el input sea un numero entero
            lectura_csv(lista_paises)
            
            match opcion:
                case 1:
                    print('Ingrese si desea ordenar por nombre de manera ascendente o descendente.')
                    opcion = input("1 - Ascendente\n2 - Descendente\n► ")
                    opcion = verificar_inputs(opcion)
                    ordenar_por_nombre(lista_paises, str(opcion))
                
                case 2:
                    print('Ingrese si desea ordenar por población de manera ascendente o descendente.')
                    opcion = input("1 - Ascendente\n2 - Descendente\n► ")
                    opcion = verificar_inputs(opcion) 
                    ordenar_por_poblacion(lista_paises, str(opcion)) 
                
                case 3:
                    print('Ingrese si desea ordenar por superficie de manera ascendente o descendente.')
                    opcion = input("1 - Ascendente\n2 - Descendente\n► ")
                    opcion = verificar_inputs(opcion) 
                    ordenar_por_superficie(lista_paises, str(opcion))
                
                case _:
                    print("El número ingresado no corresponde con las opciones\nIntente nuevamente.")

        case '6':
            print("============ Mostrar Estadísticas ============\n")

            print("Ingrese el número corresponidente a la estadística que desea aplicar.")
            print("1 - País con mayor y menor población\n2 - Promedio de población\n3 - Promedio de superficie\n4 - Cantidad de países por continente")
            opcion = input("► ").strip()
            opcion = verificar_inputs(opcion) # nos aseguramos que el input sea un numero entero
            lectura_csv(lista_paises)

            match opcion:
                case 1:
                    print("")

                    # recurrimos a la funcón que imprimirá por pantalla la respuesta
                    mayor_menor_pob(lista_paises)

                case 2:
                    print("")

                    promedio = promedio_poblacion(lista_paises) # usamos la función que nos da el promedio
                    print(f"El promedio de población de los países en la lista es: {promedio}")

                case 3:
                    print("")

                    promedio = promedio_superficie(lista_paises) # usamos la función que nos da el promedio
                    print(f"El promedio de superficie de los países en la lista es de: {promedio}km²")

                case 4:
                    print("")
                    bandera = False
                    continente = input("Ingrese el continente sobre el cual desea saber la cantidad de países que pertenecen a este.\n► ").strip().title()

                    # verificamos que el continente pertenezca a uno en la lista
                    for i in lista_paises:
                        if i["continente"] == continente:
                            bandera = True
                        
                    if bandera == True: # si el continente existe hará la bandera True y ejecuta la respuesta
                        cantidad = pais_por_continente(lista_paises, continente) # tomamos la cantidad devuelta por la funcion
                        print(f"El continente {continente} cuenta con {cantidad} Países en esta lista.")
                    else:
                        print("El continente ingresado no corresponde con uno dentro de la lista.")

                case _:
                    print("El número ingresado no corresponde con las opciones\nIntente nuevamente.")

        case '7':
            print("=================== Salir ===================\n")
            print("¡Gracias por usar el Gestor Informático de Países!\nHasta Luego.")

        case _:
            print("Opción invalida, intente nuevamente\nRecuerde usar un número (1 - 5)")
    
    print("") # salto de linea luego de cada iteración