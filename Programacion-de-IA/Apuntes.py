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
