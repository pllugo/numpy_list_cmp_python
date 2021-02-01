#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.1"

import numpy as np
import random
import math


def ej1():
    print('Comenzamos a divertirnos!')

    '''
    Empecemos a jugar con las listas y su métodos, el objetivo
    es realizar el código lo más simple, ordenado y limpio posible,
    no utilizar bucles donde no haga falta, no "re inventar" una función
    que ya dispongamos de Python. El objetivo es:

    1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
       que estén comprendidos entre 1 y 10 inclusive
       (NOTA: utilizar comprension de listas a pesar de poder hacerlo
        con un método de la librería random)
    2) Luego de generar la lista sumar los números y ver si el resultado
       de la suma es menor o igual a 21
       a) Si el número es menor o igual a 21 se imprime en pantalla
          la suma y los números recoletados
       b) Si el número es mayor a 21 se debe tirar la lista y volver
          a generar una nueva, repetir este proceso hasta cumplir la
        condicion "a"

    Realizar este proceso iterativo hasta cumplir el objetivo
    '''
    while True:
        lista = [random.randint(1, 10) for x in range(3)]
        vector = np.asanyarray(lista)
        suma = np.sum(vector)
        if suma <= 21:
            print(suma)
            print(vector)
            break
        else:
            continue


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Dado una lista de nombres de personas "nombres" se desea
    obtener una nueva lista filtrada que llamaremos "nombres_filtrados"
    La lista se debe filtrar por comprensión de listas utilizando la
    lista "padron" como parámetro.
    La lista filtrada sodo deberá tener aquellos nombres que empiecen
    con alguna de las letras aceptadas en el "padron".
    '''

    padron = ['A', 'E', 'J', 'T']

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]
    # De forma sin compresión de listas
    lista_nueva = []
    for i in range(len(nombres)):
        for j in range(len(padron)):
            if padron[j] in nombres[i]:
                lista_nueva.append(nombres[i])
            else:
                continue
    print(lista_nueva)

    #De forma con compresión de listas
    nombres_filtrados = [x for x in nombres if x[0] in padron]
    print(nombres_filtrados)
        

def ej3():
    print("Un poco de Numpy!")
    # Ejercicio de funciones
    # Se desea calcular los valores de salida de
    # una función senoidal, dado "X" como el conjunto
    # de valores que deben someter a la función "sin"

    # Conjunto de valores "X" en un array
    x = np.arange(0, 2*np.pi, 0.1)
    print(x)

    # Utilizar la función np.sin para someter cada valor de "X",
    # obtenga el array "y_nump" que tenga los resultados
    # NO utilizar comprensión de listas, solo utilice la
    # funcion de numpy "np.sin"

    y_nump = np.sin(x)
    print("Esta es la lista con la función np:\n")
    print(y_nump)

    # Conjunto de valores "X" en una lista
    x = list(np.arange(0, 2*math.pi, 0.1))

    # Utilizar comprensión de listas para obtener la lista
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función math.sin

    y_list = [math.sin(n) for n in x]
    print("Esta es la lista con la función math:\n")
    print(y_list)

    # Este es un ejemplo práctico de cuando es útil usar numpy,
    # basicamente siempre que deseen utilizar una función matemática
    # que esté definida en numpy NO necesitaran un bucle o comprensión
    # de listas para obtener el resultado de un monton de datos a la vez.


def ej4():
    print("Acercamiento al uso de datos relacionales")
    # Transformar variable numéricas en categóricas
    # Se dispone del siguiente diccionario que traduce el número ID
    # de un producto en su nombre, por ejemplo:
    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    producto = {
                556070: 'Auto',
                704060: 'Moto',
                42135: 'Celular',
                1264: 'Bicicleta',
                905045: 'Computadora',
                }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # Crear una nueva lista "lista_compra_productos" que transforme la lista
    # de realizada por "ID" de producto en lista por "nombre" producto
    # Iterar sobre la lista "lista_compra_id" para generar la nueva
    # En cada iteración acceder al diccionario para traducir el ID.
    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados en el sistema, en esos casos se debe
    # almacenar en la lista la palabra 'NaN', para ello puede hacer uso
    # de condicionales PERO recomendamos leer atentamente el método "get"
    # de diccionarios que tiene un parametro configurable respecto
    # que sucede sino encuentra la "key" en el diccionario.
    lista_compra_productos = [{x: producto.get(x, 'NaN')} for x in lista_compra_id]
    print(lista_compra_productos)


def jugar(): #Función para jugar Black Jack!!  
        lista_aleatorios = [random.randint(1,11) for x in range(2)]
        vector = np.asanyarray(lista_aleatorios)
        print(vector)
        suma = np.sum(vector)
        print(suma)
        while True:
            if suma >= 21:
                print("Parar el juego")
                break
            else:
                opcion_usuario = int(input(""" Ingrese:
                            1 Para continuar lanzando cartas
                            2 Para parar el juego\n"""))
                if opcion_usuario == 1:
                    lista_aleatorios = [random.randint(1,11) for x in range(2)]
                    vector = np.append(vector, np.asanyarray(lista_aleatorios))
                    print(vector)
                    suma = np.sum(vector)
                    print(suma)
                else:
                    break
        return suma


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Black jack! [o algo parecido :)]

    El objetivo es realizar una aproximación al juego de black jack,
    el objetivo es generar una lista de 2 números aleatorios
    entre 1 al 10 inclusive, y mostrar los "números" al usuario.
    El usuario debe indicar al sistema si desea sacar más
    números para sumarlo a la lista o no sacar más
    A medida que el usuario vaya sacando números aleatorios que se suman
    a su lista se debe ir mostrando en pantalla la suma total
    de los números hasta el momento.
    Cuando el usuario no desee sacar más números o cuando el usuario
    haya superado los 21 (como la suma de todos) se termina la jugada
    y se presenta el resultado en pantalla

    BONUS Track: Realizar las modificaciones necesarias para que jueguen
    dos jugadores y compitan para ver quien sacá la suma de números
    más cercanos a 21 sin pasarse!
    '''
    
    jugadores = int(input("Ingrese la cantidad de jugadores:\n"))
    resultado = [jugar() for x in range(jugadores)] #Genero una lista de los resultados de jugar Black Jack
    print(resultado)
    vector_resultado = np.asanyarray(resultado) #Transformo la lista a un vector
    nuevo_array = np.where((vector_resultado <= 21), vector_resultado, 0) #Busco los menores o iguales a 21
    print(nuevo_array)
    valor_cercano = max(nuevo_array) #Busco el maximo valor de los resultados de los jugadores
    if valor_cercano == 0:
        print("Nadie gana")
    else:
        print("El jugador que lanzo {} es el ganador".format(valor_cercano)) #El ganador es el maximo valor mas cercano a 21



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    # ej2()
    # ej3()
    # ej4()
    ej5()
