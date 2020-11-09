#!/usr/bin/env python
'''
Mimodulo
---------------------------
Autor: Pedro Luis Lugo Garcia
Version: 1
Descripcion:
Módulo con algunas de las funciones que ejemplifican
las herramientas desarrolladas en este curso.
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1"


import random


def promedio(numeros): #Promedio de una lista de números
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
    return resultado


def lista_aleatoria(inicio, fin, cantidad): #Función para generar lista de números aleatorios
    lista = []
    for i in range(cantidad):
        numero = random.randrange(inicio, fin + 1)
        lista.append(numero) 
    return lista


def contar(lista_numeros, elemento): #Función de cantidad que se repite un número en una lista
    cantidad = lista_numeros.count(elemento)
    return cantidad


def ordenar (numeros): #Función de ordenar una lista de números
    if numeros:
        print("La lista no esta vacia")
        numeros.sort()
    else:
        print("La lista esta vacia")
    return numeros


def vector_dados(dados): #Genera un vector de dados que se repiten en una lista aleatoria
    inicio = 1
    fin = 6
    lista_dados = lista_aleatoria(inicio, fin, dados)
    print(lista_dados)
    #Usando la función max y con key de list.count
    max_repeticiones = max(lista_dados, key=lista_dados.count)
    contar_lista = contar(lista_dados, max_repeticiones)
    if contar_lista != 1:
        print("El número {} se encuentra {} en mi lista de dados".format(max_repeticiones, contar_lista))
        dados_guardados = []
        for i in range(contar_lista):
            dados_guardados.append(max_repeticiones)
        print(dados_guardados)
    else:
        print("No existen números que se repiten, vuela a jugar")
        dados_guardados = []
    return dados_guardados     