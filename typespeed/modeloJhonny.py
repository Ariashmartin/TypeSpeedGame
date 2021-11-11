from typespeed import palabraRandom

"""
Pasos:

1) Tomar informacion del usuario
2) La palabra tiene que estar bien escrita ó pasar 5 segundos
    2.1) Si en 5 segundos no esta bien escrita, el juego se corta y perdes una vida
    2.2) Si la palabra esta bien escrita el jugador gana 10 puntos
"""

import time

start_time = time.time()

def timer(vidas,puntos,palabra):

    print(palabra)
    while time.time() - start_time < 5:

        palabra_usuario = input("\n>>")
        if palabra_usuario == palabra and time.time() - start_time < 5:
            try:
                puntos += len(palabra)
                flag = 1
                print("Acertaste, tus puntos son:",puntos)
                break
            except:
                pass

    if vidas > 0: # Esto significa que paso el tiempo sin acertar
        vidas = vidas - 1
        print("Perdiste, te quedan",vidas,"Vidas")

    if vidas == 0:
        print("Game Over")