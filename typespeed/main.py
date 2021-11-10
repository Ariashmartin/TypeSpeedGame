import typespeed.jugadores


print("BIENVENIDO AL TIMESPEED GAME!\n")

def newOrLoad ():
    """
    Funcion inicial en la que se determinara si se comienza con una partida nueva o con una guardada
    :return: 'partida' varialble entera que determinará como continuará el juego
    """

    partida=input("¿Quiere empezar una nueva partida, o continuar una partida anterior?\n1.PARTIDA NUEVA\t2.CARGAR PARTIDA\n>>")
    while int(partida) < 1 or int(partida) > 2:
        partida=input("\nRespuesta incorrecta, elija entre 1.PARTIDA NUEVA o 2.CARGAR PARTIDA\n>>")

    return int(partida)
#print(newOrLoad())

def cantPlayers ():
    """
    Funcion que solicita la cantidad de jugadores y valida el ingreso de datos
    :return: 'cantidad' variable que indica entre cuantos participantes se deben comparar los resultados
    """
    print("\nPor favor ingrese la cantidad de jugadores. ((MINIMO 2, MAXIMO 4))")
    cantidad=int(input("\n>>"))
    if cantidad < 2:
        print("\nCantidad menor a la minima")
        return cantPlayers()
    elif cantidad >4:
        print("\nCantidad superior a la maxima")
        return cantPlayers()
    else:
        return cantidad
#print(cantPlayers())

def dataPlayer(n):
    """
    Funcion que pide el ingreso de los nombres y la condicion de si el jugador es humano o bot
    :param n: cantidad de jugadores
    :return: None
    """

    for i in range (1,n+1):
        print(f"Por favor ingrese el nombre del jugador {i}:")
        nombre=input("\nNombre\n>>")
        print(f"\nSi {nombre} es humano ingrese 1, si es bot (CPU) ingrese 2")
        condition=int(input("\n>>"))
        while condition <1 or condition >2:
            condition=input(f"\nRespuesta incorrecta, indique si {nombre} es 1.humano o 2.bot")

        guardado = open("progress.txt", "a+")
        dictPlayer=str(typespeed.jugadores.dictPlayer(nombre,condition))
        guardado.write(dictPlayer+"\n")
        guardado.close()
        i+=1
#print(dataPlayer(3))

def gameMode ():
    """
    Funcion que solicita y valida el ingreso del nivel de dificultad o si se desea jugar en modo Typespeed
    :return: dif variable que sera requerida por varias funciones para definir el modo de juego
    """
    print("Por favor, ingrese la dificultad que desea jugar:\n1.Facil\n2.Normal\n3.Dificil\n4.Typespeed\n")
    dif =int(input(">>"))
    while dif < 1 or dif > 4:
        dif=int(input("\nRespuesta incorrecta\nIngrese la dificultad que desea jugar:\n1.Facil\t2.Normal\n3.Dificil\t4.Typespeed\n>>"))

    return dif
print(gameMode())