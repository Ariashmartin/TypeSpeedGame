import random


palabras_dic=open("diccionario.txt","r")
palabrasEasy=open("palabras_easy.txt","wt")

def easy ():
    listaEasy=palabras_dic.read()
    listaEasy=listaEasy.split("\n")
    for i in palabras_dic:
        if len(palabras_dic)> 1 and len(palabras_dic)<6:
            palabrasEasy.write(palabras_dic)
        else:
            pass

    return listaEasy
print (easy())

def medium ():
    listaMed=[]
    return listaMed
def hard ():
    listaHard=[]
    return listaHard

def aleatoria (list):

    nroPalabra= random.randint(0,len(list)-1)

    palabra=list[nroPalabra]

    return palabra


