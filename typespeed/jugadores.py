def listPlayer (name,cond,dif):
    """
    Funcion para convertir los parametros en datos de un diccionario y aagregar los datos de puntos y vida a cada jugador para luego guardarlo
    :param name: Nombre que ira en la keyword "Jugador"
    :param cond: Entero que indica si el jugador es bot o no
    :return: nuevo_dic es el diccionario que sera escrito en el archivo para guardar los previos al juego
    """
    if dif == 1:
        vidas = "5"
    if dif == 4:
        vidas = "None"
    if dif > 1 and dif < 4:
        vidas = "3"

    nueva_list= str(name + "," + cond + ",0," + vidas)

    return nueva_list

def readyCheck(ready):

    while ready != "ok" and ready != "OK":
        print("Ingreso invalido, si esta listo ingrese 'ok'")
        ready=input("\n>>")
    return ready




