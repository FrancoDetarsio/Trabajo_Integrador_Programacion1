# -- Trabajo Integrador Programación-1 --

# Descripción del proyecto
Este trabajo realizado en grupo de 2 personas, pertenece a la entrega del trabajo integrador correspondiente a la materia Programación 1.
En el se desarrolla una aplicación modular que toma datos sobre países desde un archivo.csv, mostrando un menú interactivo con el cual
el usuario podrá optar por distintas funciones para analizar, buscar o filtrar información contenida en dicho archivo.csv.


# Datos de la universidad y la cátedra
- Universidad: UTN
- Carrera: Tecnicatura Universitaria en Programación a Distancia
- Catedra: Programación 1 (1º cuatrimestre - 1º Año)


# Integrantes
- Integrante 1: Agustín Pieve (Comision - 10)
- Integrante 2: Franco Detarsio (Comision - 4)


# Datos de profesores
- Profesora comision 10: Martina Zabala
- Profesora comision 4: Ana Mutti


# Estructura
El programa contiene:
- Bloque -- Definición de funciones
- Aclaraciones
- Programa Principal
    Bucle while: Muestra el menú gráfico interactivo con el que el usuario interactúa
        match/case: Dará funcionalidad a las opciones del menú gráfico, según lo que el usuario ingrese
        apoyandose en las funciones del "Bloque -- Definición de funciones"


# Instrucciones de ejecución
Se muestra un menú gráfico con opciones numericas
El usuario puede navegar entre las opciones ingresando el número correspondiente
Según la opción seleccionada se le pedirá al usuario que ingrese un nombre de País/Continente o bien otra opción numerica
Se mostrará la información solicitada por el usuario
En caso de no contar con la información requerida se le notificará al usuario
En caso del ingreso de valores inválidos se le notificará al usuario del error, permitiendo reintentar o reiniciando el menú gráfico
El prográma se detendrá cuando el usario seleccione la opción "5. Salir"


# Ejemplo de entradas y salidas
Ejemplo con opción 1 "Buscar País":
1 - El usuario visualiza el menú gráfico y desea seleccionar la primera opción "1. Buscar País"
2 - El usuario ingresa ► "1" por teclado y presiona enter para confirmar
3 - se le indicará por pantalla: "Ingrese el nombre del país que desea buscar."
4 - El usuario ingresa por ejemplo ► "argentina" por teclado y presiona enter para confirmar (se aceptan mayúsculas y espacios redundantes)
5 - El programa busca en el archivo.csv si este país pertenece a uno dentro de la lista
6 - Si pertenece dará una salida: "Argentina cuenta con una población de 45376763, una superficie de 2780400km² y esta ubicado en el continente de America"
7 - Si no pertenece dará otra salida: "El país ingresado no se encuentra en la lista"


# Participación de los integrantes
- Estructura general: Trabajo Colaboratibo
- opción "1. Buscar País": Trabajo Colaboratibo
- opción "2. Filtrar Países": Trabajo Colaboratibo
- opción "3. Ordenar Países": Agustín Pieve
- opción "4. Mostrar Estadísticas": Franco Detarsio


# Repositorio de GitHub
Link: https://github.com/FrancoDetarsio/Trabajo_Integrador_Programacion1


# Link a Video
link: 