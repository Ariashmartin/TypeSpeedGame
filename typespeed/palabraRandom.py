import random

palabras_dic=open("diccionario.txt","rt") #Abro el archivo diccionario para automaticamente convertirlo en una lista

def listaSegunDif (dif):
    """
    Funcion que lee las palabras y de acuerdo a su tamaño y el parametro recibido crea una lista para cada dificultad
    :param dif: numero entero que determina si el modo de juego sera facil,normal,dificil o tipespeed
    :return: una lista de acuerdo a la dificultad
    """
    lista = palabras_dic.read().split("\n")
    listaEasy = []
    listaNormal = []
    listaHard = []
    for i in range(len(lista)):

        if len(lista[i]) < 6 and dif == 1:
            listaEasy.append(lista[i])
            i += 1

        elif len(lista[i]) < 10 and dif == 2:
            listaNormal.append(lista[i])
            i += 1

        elif len(lista[i]) < 15 and dif == 3:
            listaHard.append(lista[i])
            i += 1

    if dif == 1:
        return listaEasy
    if dif == 2:
        return listaNormal
    if dif == 3:
        return listaHard
    else:
        return lista

#print(listaSegunDif(4))

def aleatoria (list):
    """
    Recibe la lista de palabras y selecciona una palabra aleatoria para tipear
    :param list: lista recibida de "listaSegunDif"
    :return: palabra que debera ser tipeada
    """
    nroPalabra= random.randint(0,len(list)-1)

    palabra=list[nroPalabra]

    return palabra
