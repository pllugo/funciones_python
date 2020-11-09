#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.2"

import random


def imprimir_nombre(nombre, apellido):#Función imprimir nombre

    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)
    print(nombre, apellido)


def promedio(numeros):
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    if numeros:
        print("La lista no esta vacia")
        suma = sum(numeros)
        resultado = suma / len(numeros)
    else:
        print("La lista ésta vacia")
        resultado = 0
    return resultado # Cuando termine de implementar está función borrar "pass"


def nuevo_promedio(numeros): #Esta es otra forma de obtener una función promedio
    suma = 0
    if numeros:
        print("La lista no esta vacia")
        for i in range(len(numeros)): #Recorro la lista por indice con un for
            suma = suma + numeros[i]
        resultado = suma / len(numeros)
    else:
        print("La lista esta vacia")
        resultado = 0
    return resultado


def ej1():
    
    print('Mi primera funcion')
    # Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe cumpletar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    imprimir_nombre('Pedro', 'Lugo')

    # Reemplazar por su nombre y apellido los textos


def ej2():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle.
    Puede utilizar la función "sum" y la función "len"
    sum --> obtener la sumatoria de números
    len --> obtener la cantidad de números
    promedio = sumatoria_numeros / cantidad_numeros

    La función debe retornar (return) el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado

    '''

    print("El valor de retorno de promedio es:", promedio(numeros))
    # La función ya se encuentra definida arriba de todo en el archivo,
    # busque al princpio de todo "def promedio"
    # Ya la función fue preparada para que usted le pase "numeros"
    # como parámetro, falta que calcule el promedio y retorne el valor
    # resultante.

    # Llamar a la función en este lugar y capturar el valor del retorno
    # promedio_re

    # Luego imprimir en pantalla el valor resultante, tal que:


def ordenar (numeros):#Función para ordenar una lista de números
    if numeros:
        print("La lista no esta vacia")
        numeros.sort()
    else:
        print("La lista esta vacia")
    return numeros
        

def ej3():
    # Ejercicios de listas y métodos
    numeros = [12, 8, 6, 4, 10, 2]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.

    '''
    
    # Luego de crear la función invocarla en este lugar:
    # lista_ordenada = ordenar(numeros)
    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar
    print(numeros)
    lista_ordenada = ordenar(numeros)
    print("La lista ordenada es:", lista_ordenada)


def lista_aleatoria(inicio, fin, cantidad): #Función para generar lista de números aleatorios
    lista = []
    for i in range(cantidad):
        numero = random.randrange(inicio, fin + 1)
        lista.append(numero) 
    return lista


def ej4():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10
    cantidad = 5

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    # numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.

    --> def lista_aleatoria (inicio, fin, cantidad)

    Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    veces esta operacion:
    numero = random.randrange(inicio, fin+1)

    Cada valor generado lo debe guardar en una lista, recuerde:
    1) Iniciar y crear esa lista vacia.
    2) Para agregar nuevos elementos en la lista utiliza "append"

    Finalmente dicha función debe retornar la lista de elementos random generados.
    '''

    # Invocar lista_aleatoria
    # mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    # print(mi_lista_aleatorio)
    mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    print("Esta es la lista aleatoria:", mi_lista_aleatorio)


def contar(lista_numeros, elemento): #Función de cantidad que se repite un número en una lista
    cantidad = lista_numeros.count(elemento)
    return cantidad


def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5
    inicio = 1
    fin = 9
    numero = 3
    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''
    mi_lista_aleatoria = lista_aleatoria(inicio, fin, cantidad_numeros)
    print("La lista aleatoria es:\n", mi_lista_aleatoria)
    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)
    cantidad_tres = contar(mi_lista_aleatoria, numero)
    print("El número {} , se repite {}".format(numero,cantidad_tres))




if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
