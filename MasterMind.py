# -*- coding: utf-8 -*-
'''
Created on 11 feb 2022
@author: ana
'''
import random

numeros = '0123456789'
codigoSecreto= ''
codigoUsu=''
contmuertos=0
contheridos=0
muertos=[]
heridos=[]
intentos=0

print('*************************************')
print('                                     ')
print('          JUEGO MASTERMIND           ')
print('                                     ')
print('      Pulsa ENTER para comenzar      ')
print('                                     ')
print('*************************************')

input()

while len(codigoSecreto) < 4:
    numero = random.choice(numeros)
    if numero not in codigoSecreto:
        codigoSecreto+=numero
print(codigoSecreto)
codigoUsu=input('Introduce un codigo: ')

while codigoSecreto != codigoUsu:
    intentos+=1
    heridos=[]
    muertos=[ '#']*4
    for i in range(4):
        if codigoUsu[i] in codigoSecreto:
            if codigoUsu[i]==codigoSecreto[i]:
                contmuertos+=1
                muertos[i]=codigoUsu[i]
            else:
                contheridos+=1
                heridos.append(codigoUsu[i])
    
    
    if contmuertos<4 and contmuertos !=0 or contheridos<4 and contheridos:
        print('Nº muertos:',contmuertos)
        print('Nº heridos:', contheridos, '-->', heridos)
        for j in muertos:
            print(j,end=' ')
        print('\n')
        codigoUsu=input('Introduce un nuevo codigo: ')
    elif contmuertos==0 and contheridos==0:
        print('No ha habido suerte, ningun digito coincide')
        codigoUsu=input('Indroduce un nuevo codigo: ')
    
    contmuertos=0
    contheridos=0
        
print('¡¡¡Fin de la partida!!! ')
print('Codigo secreto: ',codigoSecreto)
print('Numero de intetos:',intentos)
    
