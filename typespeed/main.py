import time
import typespeed.jugadores
import typespeed.palabraRandom

print("BIENVENIDO AL TIMESPEED GAME!\n")


def newOrLoad ():
    """
    Funcion en la que se determinara si se comienza con una partida nueva o con una guardada
    :return: 'partida' varialble entera que determinará como continuará el juego
    """
    partida=input("¿Quiere empezar una nueva partida, o continuar una partida anterior?\n1.PARTIDA NUEVA\t2.CARGAR PARTIDA\n>>")
    while int(partida) < 1 or int(partida) > 2:
        partida=input("\nRespuesta incorrecta, elija entre 1.PARTIDA NUEVA o 2.CARGAR PARTIDA\n>>")
    return int(partida)


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
        addCant = open("progress_g.txt", "a+")
        addCant.write("Jugadores," + str(cantidad)+"\n")
        addCant.close()
        return cantidad


def dataPlayer(n,d):
    """
    Funcion que pide el ingreso de los nombres y la condicion de si el jugador es humano o bot
    :param n: cantidad de jugadores
    :return: None
    """

    for i in range (1,n+1):
        print(f"Por favor ingrese el nombre del jugador {i}:")
        nombre=input("\nNombre\n>>")
        print(f"\nSi {nombre} es humano ingrese 1, si es bot (CPU) ingrese 2")
        condition=int(input("\nCondicion\n>>"))
        while condition <1 or condition >2:
            condition=int(input(f"\nRespuesta incorrecta, indique si {nombre} es 1.humano o 2.bot\n\nCondicion\n>>"))

        guardado = open("progress_p.txt", "a+")
        listPlayer= str(typespeed.jugadores.listPlayer(nombre,str(condition),d))
        guardado.write(listPlayer+"\n")
        guardado.close()

        i+=1


def gameMode ():
    """
    Funcion que solicita y valida el ingreso del nivel de dificultad o si se desea jugar en modo Typespeed
    :return: dif variable que sera requerida por varias funciones para definir el modo de juego
    """
    print("Por favor, ingrese la dificultad que desea jugar:\n1.Facil\n2.Normal\n3.Dificil\n4.Typespeed\n")
    dif =int(input(">>"))
    while dif < 1 or dif > 4:
        dif=int(input("\nRespuesta incorrecta\nIngrese la dificultad que desea jugar:\n1.Facil\t2.Normal\n3.Dificil\t4.Typespeed\n>>"))

    addDif=open("progress_g.txt","a")
    addDif.write("MODO DE JUEGO "+str(dif)+"\n")
    return dif


def startGame():
    """
    Funcion que llevara todas las demas para poder correr el juego
    :return: None
    """

    partida=newOrLoad()

    if partida==1: #Al tomar la decicion de jugar nueva partida...

        resetSave1=open("progress_g.txt","w").truncate() #Limpia el archivo donde se guardo cualquier informacion de partidas anteriores
        resetSave2 = open("progress_p.txt","w").truncate()  # Limpia el archivo donde se guardo cualquier informacion de partidas anteriores
        cantidad = cantPlayers()
        dif = gameMode()
        dataPlayer(cantidad,dif)

        lista_game = typespeed.palabraRandom.listaSegunDif(dif)
        for i in range(0,cantidad): #Repite la los turnos por la cantidad de jugadores

            puntos=0
            vidas=5
            ready= typespeed.jugadores.readyCheck(input(f"Jugador {i+1}, si esta listo ingrese 'ok'\n>>"))

            while vidas !=0:    #Repite la peticion de palabras hasta que las vidas sean 0
                print("Pasamos con",vidas,"vidas","y tus puntos son:", puntos)
                start_time = time.time()

                palabra = typespeed.palabraRandom.aleatoria(lista_game)

                print("La palabra es:",palabra)
                respuesta=input(">>")
                if palabra!=respuesta and time.time()-start_time<5:
                    vidas -= 1

                if palabra==respuesta and time.time()-start_time<5:
                    puntos += len(palabra)

                if time.time()-start_time>5:
                    vidas -= 1

            if vidas==0:
                print(f"Jugador {i+1}, consiguio {puntos} puntos")


startGame()
