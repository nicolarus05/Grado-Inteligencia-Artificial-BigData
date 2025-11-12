#TEMA 1 Introduccion y fundamentos de python
'''
Es un lenguaje de programacion interpretado, multiparadigma y multiplataforma.
Fue creado por Guido van Rossum y su primera version fue lanzada en 1991.
Python se utiliza en desarrollo web, ciencia de datos, inteligencia artificial, automatizacion de tareas, entre otros.
'''

#TEMA 2 Tipos de datos y Operadores logicos
'''
Los tipos de datos mas comunes en python son:
- Numeros: enteros (int) y de punto flotante (float)
- Cadenas de texto (str)
- Listas (list)
- Tuplas (tuple)
- Diccionarios (dict)
- Conjuntos (set)

Los operadores logicos en python son:
- and
- or
- not
'''
#Ejemplo de tipos de datos
""" entero = 10
flotante = 10.5
cadena = "Hola, Mundo!"
booleano = True """

#Operadores aritmeticos
"""
+ Suma
- Resta
* Multiplicacion
/ Division
% Modulo
** Exponente
// Division entera
"""

#Operadores de comparacion
"""
== Igual
!= Diferente
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
and, or, not Operadores logicos
"""
#Ejemplos
#1. La media de 3 notas (0-10) y decir si aprueba o no (5 o mas)
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 5:
    print("Aprobado")
else:
    print("Suspenso")
    
#2. Suma de dos numeros y muestra el tipo de dato
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
suma = num1 + num2
print("La suma es:", suma)
print("El tipo de dato de la suma es:", type(suma))

#3. Multiplica por 2 un numero decimal ingresado como texto
num = input("Introduce un numero decimal: ")
num_decimal = float(num)
resultado = num_decimal * 2
print("El resultado es:", resultado)

#4. Verificar si es mayor de edad (18 o mas)
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
#5. Muestra el mayor de dos numeros
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
if num1 > num2:
    print("El mayor es:", num1)
else:
    print("El mayor es:", num2)
    
#6. Verificar si un numero es par y mayor que 10
num = float(input("Introduce un numero: "))
if num > 10 and num % 2 == 0:
    print("El numero es par y mayor que 10")
else:
    print("El numero no cumple las condiciones")

#7. operador logico(and) entre dos valores convertidos a booleanos
valor1 = "hola"
valor2 = 5

valor1 = bool(valor1)
valor2 = bool(valor2)

resultado = valor1 and valor2

print("El resultado de valor1 and valor2 es:", resultado)

#8. Indica si un numero es 0, positivo o negativo (hacerlo en el menor numero de lineas posible)
num = float(input("Introduce un numero: "))
if num > 0: print("Positivo")
elif num < 0: print("Negativo")
else: print("Cero")

#Operadores especiales
"""
Pertenencia: in, not in
    in: Verifica si un elemento esta en una secuencia
    not in: Verifica si un elemento no esta en una secuencia

Identidad: is, is not
    is: Verifica si dos variables apuntan al mismo objeto en memoria
    is not: Verifica si dos variables no apuntan al mismo objeto en memoria
"""

#Ejercicios 
#9 Busca una palabra en una frase y verifica condiciones in/not in
frase = "En un lugar de La Mancha"
palabra = str(input("Introduce una palabra: "))
if palabra in frase:
    print("La palabra esta en la frase")
else:
    print("La palabra no esta en la frase")
    
#10 Comparacion de tipo y valores usando is/is not
a = 5
b = 5
c = "hello"
d = [1, 2, 3]

print(a is b)  # True
print(a is not b)  # False
print(type(a) is int)  # True
print(type(c) is not int)  # True
print(d is [1, 2, 3])  # False

#Tema 3 Estructuras de control
'''
Condicionales: if, elif, else
Bucles: for, while
- for: itera sobre una secuencia (lista, tupla, diccionario, conjunto, cadena)
- while: ejecuta un bloque de codigo mientras una condicion sea verdadera
'''
#Ejemplos
#for
for i in range(5):
    print("Iteracion:", i)
    
#while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

'''
break: termina el bucle
continue: salta a la siguiente iteracion

Anidamiento de estructuras de control
'''

#Ejercicio 1. Genera un numero aleatorio y pide al usuario adivinar hasta acertar. Usa while y condicionales
import random
num_aleatorio = random.randint(1, 10)
adivinar = 0
while adivinar != num_aleatorio:
    adivinar = int(input("Adivina el numero: "))
    if adivinar < num_aleatorio:
        print("Demasiado bajo")
    elif adivinar > num_aleatorio:
        print("Demasiado alto")
    else: 
        print("Correcto!")

#Ejercicio 2. Solicita un entero positivo y calcula su factorial con un bucle for. Muestra el resultado al final
num = int(input("Introduce un numero positivo: "))
factorial = 1
if num < 0:
    print("El numero no es positivo")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)

#Ejercicio 3. Muestra opciones(sumar, restar, salir). Emplea un bucle while true con if/elif y break para salir
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = int(input("Selecciona una opcion: "))
    
    if opcion == 1:
        print("La suma es:\n", num1 + num2)
    elif opcion == 2:
        print("La resta es:\n", num1 - num2)
    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")
        
#Ejercicio 4. Dado 3 numeros, encuentra e imprime el mayor utilizando sentencias if anidadas
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
num3 = float(input("Introduce el tercer numero: "))

if (num1 >= num2) and (num1 >= num3):
    mayor = num1
elif (num2 >= num1) and (num2 >= num3):
    mayor = num2
else:
    mayor = num3
print("El mayor es:", mayor)

#Ejercicio 5. Escribe un programa que imprima la tabla de multiplicar del 1 al 10 de un numero proporcionado por el usuarioa usando un bucle for
num1 = int(input("Introduce un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(num1, "x", i, "=", num1 * i)
    
#Ejercicio 6. Usa un bucle while para sumar numeros hasta que el numero supere 100. muestra cuantas iteraciones han sido necesarias
suma = 0
contador = 0
while suma <= 100:
    num = float(input("Introduce un numero para sumar: "))
    suma += num
    contador += 1
print("Se han necesitado", contador, "iteraciones para superar 100. La suma es:", suma)

#Ejercicio 7. Demuestra el uso de break buscando un valor especifico en una lista y deteniendo el bucle al encontrarlo
lista = [3, 5, 7, 9, 11, 13, 15]
valor_buscado = int(input("Introduce un valor a buscar en la lista: "))
for numero in lista:
    if numero == valor_buscado:
        print("Valor encontrado:", numero)
        break
else:
    print("El valor no esta en la lista.")
    
#Ejercicio 8. Demuestra el uso de continue imprimiendo todos los numeros impares del 1 al 20
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
    
#Ejercicio 9. Utiliza un bucle for con una clausula else para buscar un elemento en una lista y mostrar un mensaje si no se encuentra
lista = [2, 4, 6, 8, 10]
valor_buscado = int(input("Introduce un valor a buscar en la lista: "))
for numero in lista:
    if numero == valor_buscado:
        print("Valor encontrado:", numero)
        break
else:
    print("El valor no esta en la lista.")
    
#Ejercicio 10. Escribe un bucle anidado que imprima un triangulo de asteriscos con un numero de filas especificado por el usuario
asteriscos = int(input("Introduce el numero de filas para el triangulo de asteriscos: "))
for i in range(1, asteriscos + 1):
    for j in range(i):
        print("*", end="")
    print()

#Tema 4: Funciones y Modularizacion
'''
Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica.
'''
#Ejemplo
def suma(a, b):
    return a + b

'''
Tipos de funciones:

1. Funciones predefinidas: Son las que ya vienen con python, como print(), input(), len(), etc.
2. Funciones definidas por el usuario: creadas por el programador usando def.
3. Funciones lambda(funciones anonimas): se definen en una sola linea, sin nombre.
'''
#Ejemplo de funcion lambda
cuadrado = lambda x: x ** 2
print(cuadrado(5))

'''
Parametros y argumentos:
- Parametros: variables que se definen en la funcion. 
- Argumentos: valores que se pasan al llamar la funcion.
'''
#Ejemplo
def saludar(nombre):  # nombre es el parametro
    print("Hola,", nombre)
    
saludar("Juan")  # "Juan" es el argumento

'''
Tipos de parametros:
1. Posicionales: se pasan en orden.
2. Nombrados: se especifica el nombre del parametro.
3. Por defecto: tienen un valor predefinido.
4. Arbitrarios: permiten un numero variable de argumentos. 
'''

'''
Modularacion en python.
La modularizacion consiste en dividir un programa en modulos mas pequeños y manejables, cada uno con funciones especificas.

Ventajas:
- Reutilizacion de codigo.
- Mantenimiento mas facil.
- Mejor organizacion.
'''

'''
Tipos de importacion:
import math              # importa todo el módulo
from math import sqrt    # importa solo una función
from math import *       # importa todo (no recomendado)
import math as m         # alias para el módulo
'''

#Tema 5: Colecciones en Python
'''
- Listas: colecciones ordenadas y mutables. Se definen con corchetes [].
  - append(): Agrega un elemento al final de la lista.
  - extend(): Agrega los elementos de otra lista.
  - insert(): Agrega un elemento en una posicion especifica.
  - remove(): Elimina el primer elemento con el valor especificado.
  - pop(): Elimina y devuelve el ultimo elemento de la lista.
  - clear(): Elimina todos los elementos de la lista.
  - index(): Devuelve la posicion del primer elemento con el valor especificado.
  - count(): Devuelve el numero de veces que un elemento aparece en la lista.
  - sort(): Ordena los elementos de la lista.
  - reverse(): Invierte el orden de los elementos de la lista.
  - copy(): Devuelve una copia superficial de la lista.
  - Lista por comprension: 
    - Sintaxis: [expresion for item in iterable if condicion]
    - Ejemplo: cuadrados = [x**2 for x in range(10) if x % 2 == 0]
    - Ventajas: codigo mas conciso y legible, mejor rendimiento.
    - Desventajas: puede ser menos claro para principiantes, no apto para operaciones complejas.

- Tuplas: colecciones ordenadas e inmutables. Se definen con paréntesis ().
  - count(): Devuelve el número de veces que un elemento aparece en la tupla.
  - index(): Devuelve la posición del primer elemento con el valor especificado.

- Diccionarios: colecciones desordenadas de pares clave-valor. Se definen con llaves {}.
  - keys(): Devuelve una lista con las claves del diccionario.
  - values(): Devuelve una lista con los valores del diccionario.
  - items(): Devuelve una lista de tuplas con los pares clave-valor.
  - get(): Devuelve el valor de una clave especificada.
  - pop(): Elimina y devuelve el valor de una clave especificada.

- Conjuntos: colecciones desordenadas de elementos únicos. Se definen con llaves {} o con la función set().
  - add(): Agrega un elemento al conjunto.
  - remove(): Elimina un elemento del conjunto.
  - discard(): Elimina un elemento del conjunto sin generar un error si no existe.
  - pop(): Elimina y devuelve un elemento aleatorio del conjunto.
  - clear(): Elimina todos los elementos del conjunto.
'''

#Tema 6 Manejo de errores y excepciones
'''
Tipos de errores comunes: 
- SyntaxError: error de sintaxis.
- TypeError: operacion o funcion aplicada a un tipo de dato inapropiado.
- NameError: variable o funcion no definida.
- IndexError: indice fuera de rango.
- KeyError: clave no encontrada en un diccionario.
- ValueError: valor inapropiado para una operacion.
- ZeroDivisionError: division por cero.

raise: se utiliza para lanzar una excepcion de manera explicita.
'''

#Tema 7 Modulos y Paquetes
'''
Modulo: Archivo .py que contiene funciones, clases y variables relacionadas.
Paquete: Coleccion de modulos organizados en un directorio con un archivo __init__.py.

Que es pip?
- Pip es el gestor de paquetes de Python que permite instalar y gestionar bibliotecas y dependencias externas.

Comandos basicos de pip:
- pip install nombre_paquete: Instala un paquete.
- pip uninstall nombre_paquete: Desinstala un paquete.
- pip list: Muestra los paquetes instalados.
- pip show nombre_paquete: Muestra informacion sobre un paquete instalado.
- pip freeze: Muestra las versiones de los paquetes instalados en formato compatible con requirements.txt
- pip install --upgrade nombre_paquete: Actualiza un paquete a la ultima version.

Como crear un paquete:
1. Crea un directorio con el nombre del paquete.
2. Dentro del directorio, crea un archivo __init__.py (puede estar vacio).
3. Agrega modulos (.py) dentro del directorio.
4. Importa los modulos en __init__.py si es necesario.
5. Instala el paquete localmente usando pip install -e ruta_del_directorio.
'''

# Tema 8: lectura y escritura de archivos
'''
Manejo de CSV con csv: 
- csv.reader(): Lee archivos CSV.
- csv.writer(): Escribe archivos CSV.
- csv.DictReader(): Lee archivos CSV como diccionarios.
- Abrir archivos con newline='' para evitar problemas de formato.

Pandas para manejo de datos:
DataFrame: tabla de datos bidimensional.
- head(): Muestra las primeras filas del DataFrame.
- info(): Muestra informacion del DataFrame.
- describe(): Estadisticas descriptivas del DataFrame.

Paso a paso de CSV a DataFrame:
1. Importar pandas: import pandas as pd
2. Leer CSV: df = pd.read_csv('archivo.csv')
3. Explorar datos: df.head(), df.info()
4. Manipular datos: df['columna'], df.loc[], df.iloc[]
5. Guardar cambios: df.to_csv('archivo_modificado.csv', index=False)
'''

#Tema 9: Introduccion a Docker.
'''
Docker es una plataforma de contenedores que permite empaquetar aplicaciones y sus dependencias en un entorno aislado y portable.

- FastApi: Es un framework web rapido para construir APIs con Python. Se destaca por su rendimiento y facilidad de uso.
- Clean Architecture: Es un patron de diseño de software que organiza el codigo en capas, 
    separando la logica de negocio de los detalles de implementacion, facilitando el mantenimiento y la escalabilidad.
'''

#Tema 10: Bases de datos con python.
'''
Conexion a SQLite con sqlite3:
- Conectar a la base de datos: conn = sqlite3.connect('base_de_datos.db')
- Crear un cursor: cursor = conn.cursor()
- Ejecutar consultas SQL: cursor.execute('SQL_QUERY')
- Obtener resultados: resultados = cursor.fetchall()
- Guardar cambios: conn.commit()
- Cerrar la conexion: conn.close()
'''

#Tema 11: lectura y escritura de archivos csv.
'''
Manejo de CSV con csv: 
- csv.reader(): Lee archivos CSV.
- csv.writer(): Escribe archivos CSV.
- csv.DictReader(): Lee archivos CSV como diccionarios.
- csv.DictWriter(): Escribe archivos CSV desde diccionarios.
- Abrir archivos con newline='' para evitar problemas de formato.

Gestores de contexto:
- with: Se utiliza para manejar recursos como archivos, asegurando que se cierren correctamente.
Ejemplo:
with open('archivo.csv', 'r', newline='') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
        
Pasos a paso de csv a DataFrame con pandas:
1. Importar pandas: import pandas as pd
2. Leer CSV: df = pd.read_csv('archivo.csv')
3. Explorar datos: df.head(), df.info()
4. Manipular datos: df['columna'], df.loc[], df.iloc[]
5. Guardar cambios: df.to_csv('archivo_modificado.csv', index=False)
'''