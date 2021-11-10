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

vidas = 3
puntos = 0
palabra_objetivo = palabraRandom.aleatoria(palabraRandom.easy())
# Esta palabra viene del conjunto de palabras cargadas, que varia segun dificultad

palabra_usuario = ""
flag = 0
print(palabra_objetivo)
while time.time() - start_time < 5:

    palabra_usuario = input("Ingrese la palabra objetivo: ")
    if palabra_usuario == palabra_objetivo and time.time() - start_time < 5:
        try:
            puntos += len(palabra_objetivo)
            flag = 1
            print("Acertaste, tus puntos son:",puntos)
            break
        except:
            pass

if flag == 0 and vidas > 0: # Esto significa que paso el tiempo sin acertar
    vidas = vidas - 1
    print("Perdiste, te quedan",vidas,"Vidas")

if vidas == 0:
    print("Game Over")