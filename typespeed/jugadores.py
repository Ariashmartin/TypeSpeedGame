

def dictPlayer (name,cond):
    nuevo_dic={"Jugador":name,"BotOrNot":cond,"puntos":0,"vidas":5}
    return nuevo_dic




def dataPlayers ():
    linea=guardado.readline()
    linea=linea.split("-")
    print(f"\n{linea}")
    return linea
