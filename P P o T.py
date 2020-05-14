

import random
import time

eleccion = ["tijera", "papel", "piedra"]

puntuacion = {}
puntuacion[('piedra', 'piedra')] = 2
puntuacion[('piedra', 'papel')] = 1
puntuacion[('piedra', 'tijera')] = 3
puntuacion[('papel', 'piedra')] = 3
puntuacion[('papel', 'papel')] = 2
puntuacion[('papel', 'tijera')] = 1
puntuacion[('tijera', 'piedra')] = 1
puntuacion[('tijera', 'papel')] = 3
puntuacion[('tijera', 'tijera')] = 2

def Final(resp):
    global puntos
    if resp=="s":
        print("Next round")
        puntos -= 3
    elif resp=="n":
        print("puntos:", puntos)
        exit()
    else:
        print("respuesta mala ")
        exit()

print("Bienvenido a al piedra papel o tijera\n")
time.sleep(0.5)
print("\Inicio \n")
time.sleep(0.5)
puntos=0
m_puntos=0
while True:
    if puntos==3:
        print("FIN DE LA PARTIDA")
        print("HAS GANADO")
        print("vuelves a jugar ?")
        print("SI quieres seguir pon s y  Si no quieres pon n")
        respuesta2=input()
        Final(respuesta2)                    
    if m_puntos==3:
        print("the End")
        print("Perdiste")
        print("Quieres intentarlo otra ves ")
        print("escribe 'q' para jugar otra vez o dale a la 'e' para no volver a jugar")
        respuesta2=input()
        Final(respuesta2)    
    for elemento in eleccion:
        time.sleep(0.7)
        print(f"{elemento}")   
    respuesta = input()
    if respuesta!="piedra" and respuesta!="papel" and respuesta!="tijera": 
        print("Respuesta mal")
        exit()
    maquina = random.choice(eleccion)
    print(f"maquina: {maquina}")
    total = puntuacion[maquina, respuesta]
    if total==1:
        print("Eres el ganador ")
        puntos += 1
    elif total ==2:
        print("Empate")
    elif total ==3:
        print("You lose")
        m_puntos += 1
    print(f"Puntos del usuario  {puntos}")
    print(f"Puntos de la maquina: {m_puntos}")