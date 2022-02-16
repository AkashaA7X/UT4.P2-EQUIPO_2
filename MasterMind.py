# -*- coding: utf-8 -*-
'''
Created on Feb 16, 2022

@author: celia
'''
import random
import time
import sys
from asyncio.tasks import sleep

numeros = '0123456789'
codigoSecreto= ''
codigoUsu=''
contmuertos=0
contheridos=0
muertos=[]
heridos=[]
intentos=0


def pedirNumero():
    while True:
        codigoUsu=input('Introduce un codigo: ')
        
        if (codigoUsu.isnumeric() == False) :
            print("Debes introducir un codigo de 4 digitos numericos:")
        elif (len(codigoUsu) !=4):
            print("Debes introducir un codigo de 4 digitos:")
        else:
            break
    return codigoUsu
    

print('**************************************************************************')
print('                                                                          ')
print('                           JUEGO MASTERMIND                               ')
print('                                                                          ')
print('                      Pulsa ENTER para comenzar                           ')
print('                                                                          ')
print("**************************************************************************")

input()
time.sleep(1)
print("**************************************************************************")
print("            REGLAS: Debes adivinar el código secreto de 4 dígitos         ")
print("        Aquel número que introduzcas y esté en la misma posición          ")
print("        que el número del código secreto, es un número muerto.            ")
print("        En el caso de que introduzcas un número que se encuentra en el    ")
print("      código secreto pero no en la misma posición, será un número herido  ")
print("**************************************************************************")
time.sleep(1)
print("                    Pulsa ENTER cuando estes listo                    ")
input()
while len(codigoSecreto) < 4:
    numero = random.choice(numeros)
    if numero not in codigoSecreto:
        codigoSecreto+=numero


codigoU= pedirNumero()    
while codigoSecreto != codigoU:
    intentos+=1
    heridos=[]
    muertos=[ '#']*4
    for i in range(4):
        if codigoU[i] in codigoSecreto:
            if codigoU[i]==codigoSecreto[i]:
                contmuertos+=1
                muertos[i]=codigoU[i]
            else:
                contheridos+=1
                heridos.append(codigoU[i])
    
    
    if contmuertos<4 and contmuertos !=0 or contheridos<4 and contheridos:
        print('Nº muertos:',contmuertos, '-->', muertos)
        print('Nº heridos:', contheridos, '-->', heridos)
        codigoU= pedirNumero() 
        
    elif contmuertos==0 and contheridos==0:
        print('No ha habido suerte, ningun digito coincide')
        codigoU= pedirNumero() 
        
    
    contmuertos=0
    contheridos=0
        
print('!!!Fin de la partida!!! ')
print('Codigo secreto: ',codigoSecreto)
print('Numero de intentos:',intentos)
