import os
from collections import deque

def AGREGAR():
    print("USTED ELIGIO AGREGAR ")
    print("ESTOS SON LOS ELEMENTOS ACTUALES DE  LA CARPETA")
    print(lista_de_archivos)
    cola_2 = []
    num_elemento = int(input ("Que elemento desea seleccionar "))
    cola_2.append(lista_de_archivos[num_elemento]) 
    print("elemento seleccionado")   
    print(cola_2)

def IMPRIMIR():
    print("USTED ELIFIO IMPRIMIR")
    print(lista_de_archivos)
    print("Y LOS ELEMENTOS QUE  IMPRIMIR SON  ")
    print(cola_2)



ruta = input("INGRESE LA RUTA DE LA CARPETA")
cola_1 = [os.listdir(ruta)]
lista_de_archivos = os.listdir(ruta)
print(lista_de_archivos)
print ("MENU PRINCIPAL")
print ("1)AGREGAR UN ELEMENTO A LA IMPRECION ")
print ("2)IMPRIMIR")
print ("3)SALIR ")
while True:
    op = int(input ("SELECCIONE UNA OPCION"))
    if op == 1:
        AGREGAR()
    elif op == 2:
        IMPRIMIR()
    else: 
        print("Fin de el programa")
        break

