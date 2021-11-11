def dictPlayer (name,cond):
    """
    Funcion para convertir los parametros en datos de un diccionario y aagregar los datos de puntos y vida a cada jugador para luego guardarlo
    :param name: Nombre que ira en la keyword "Jugador"
    :param cond: Entero que indica si el jugador es bot o no
    :return: nuevo_dic es el diccionario que sera escrito en el archivo para guardar los previos al juego
    """
    nuevo_dic={"Jugador":name,"BotOrNot":cond,"puntos":0,"vidas":5}
    return nuevo_dic





