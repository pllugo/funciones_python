#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.3"


import mimodulo


def ej1(): #Para esta parte cree mimodulo.py
    print('Comencemos a crear lo nuestro!')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    '''

    #El archivo es mimodulo.py


def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada
    '''

    tiros_dados = 5
    inicio = 1
    fin = 6

    nueva_lista = mimodulo.lista_aleatoria(inicio, fin, tiros_dados) #Genero una lista aleatoria enviandole a la función
                                                                     # el inicio y fin y la cantidad de dados
    print("Lista generada", nueva_lista)
    lista_ordenada = mimodulo.ordenar(nueva_lista) #Genero la lista ordenada
    print("Lista ordenada es:", lista_ordenada)


def ej3():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "contar" para contar cuantas veces aparece:
    a - Cuantsa veces aparece el número 1 en su lista de dados tirados
    b - Cuantsa veces aparece el número 2 en su lista de dados tirados
    c - Cuantsa veces aparece el número 3 en su lista de dados tirados
    d - Cuantsa veces aparece el número 4 en su lista de dados tirados
    e - Cuantsa veces aparece el número 5 en su lista de dados tirados
    f - Cuantsa veces aparece el número 6 en su lista de dados tirados


    2)
    Utilice la función de Python max con la key de list.count para
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase para ver como se implementa max con esa key

    '''

    tiros_dados = 5
    inicio = 1
    fin = 6

    nueva_lista = mimodulo.lista_aleatoria(inicio, fin, tiros_dados)
    print("Lista generada", nueva_lista)
    lista_ordenada = mimodulo.ordenar(nueva_lista)
    print("Lista ordenada es:", lista_ordenada)
    for j in range(6):#Uso un ciclo for para recorrer la lista
        contar_lista = mimodulo.contar(lista_ordenada, j+1) #j+1 ya que quiero comparar empezando con el número 1
        print("El número {} se encuentra {} en mi lista de dados".format(j+1,contar_lista))
    #Usando la función max y con key de list.count
    max_repeticiones = max(lista_ordenada, key=lista_ordenada.count)
    print('El número que mas se repite en la lista', max_repeticiones)


def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".
    El enunciado está armado a modo de guía, pueden resolver el problemla
    de otra forma.
    Si tienen dudas sobre el enunciado o alguno de los puntos por favor
    comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
    puede haber varias interpretaciones de un mismo enunciado.

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y sacar 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.

    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitio entre los 5 dados.
    Debe usar la función de Python max con la key de list.count paara
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase o el ejercicio anterior de esta guia.

    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole una lista separada
    dados_guardados = [4,4,4]
    Debe realizar un bucle para recorrer la lista de dados_tirados
    y guardar los "4" en nuestra nueva lista dados_guardados
    Utilie append para ir sumando a dados_guardados los valores

    4) Debe volver a tira los dados, generar nuevos
    números aleatorios.
    Si en la lista "dados_guardados" tengo 3 dados guardados
    significa que ahora deberé tirar dos dados. Puede usar la función
    "len" para ver cuantos elementos hay en "dados_guardados"
    Es decir que en este caso debería generar dos números
    aleatorios nuevos con "lista_generica"
    Ahora tendré una nueva lista de "dados_tirados" en este caso
    de dos nuevos números aleatorios entre 1 y 6 representando a los dados
    tirados.

    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo guardo en "dados_guardados".

    5) Debe repetir este proceso hasta que en su lista de "dados
    guardados" tenga "generala", es decir, 5 números iguales.

    '''
  
    dados = 5
    lista_dados = mimodulo.vector_dados(dados) #Genero el vector de dados lanzados
    while len(lista_dados) > 1:
        if len(lista_dados) == 5:
            print("Generala")
            print(lista_dados)
            break
        else:
            if len(lista_dados) == 2:
                nueva_lista = mimodulo.lista_aleatoria(1, 6, 3)#Debo lanzar 3 dados
                print("Se lanzan 3 dados")
                numero = mimodulo.contar(nueva_lista, lista_dados[0])
                if numero >= 1:
                    for y in range(numero):
                        lista_dados.append(lista_dados[y])
                    print(lista_dados)
            else:
                if len(lista_dados) == 3:
                    nueva_lista = mimodulo.lista_aleatoria(1, 6, 2)#Debo lanzar 2 dados
                    print("Se lanzan 2 dados")
                    numero = mimodulo.contar(nueva_lista, lista_dados[0])
                    if numero >= 1:
                        for y in range(numero):
                            lista_dados.append(lista_dados[y])
                        print(lista_dados)
                else:
                    if len(lista_dados) == 4:
                        nueva_lista =mimodulo.lista_aleatoria(1, 6, 1)#Debo lanzar 1 dado
                        print("Se lanza 1 dado")
                        numero = mimodulo.contar(nueva_lista, lista_dados[0])
                        if numero >= 1:
                            for y in range(numero):
                                lista_dados.append(lista_dados[y])
                            print(lista_dados)


if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    # ej2()
    # ej3()
    ej4()
