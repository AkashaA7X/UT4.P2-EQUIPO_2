'''
Created on 11 feb 2022

@author: ana
'''
import random



codigoSecreto=[]
muertos=[]
intentos=0
cont=0

codigoSecreto = random.randrange(1000, 10000)
print(codigoSecreto)
    
codigoUsu=int(input('Introduce codigo:'))

while codigoUsu != codigoSecreto:
    
    intentos+=1
    #Convertimos a String para extraer los digitos
    codigoUsu= str(codigoUsu)
    
    codigoSecreto=str(codigoSecreto)
    
    muertos=[ '#']*4
    
    for i in range(4):
        if(codigoUsu[i]==codigoSecreto[i]):
            #Recoger el numero de digitos que han coincidido
            cont+=1
            muertos[i]=codigoUsu[i]
        else:
            continue
    
    #Cuando no todos los digitos introducidor son correctos
    if( cont<4) and (cont !=0 ):
        print('Nº muertos:',cont)
        for j in muertos:
            print(j,end=' ')
        print('\n')
        cont=0
        codigoUsu=int(input('Indroduce un nuevo codigo:'))
        
                          
    elif (cont==0):
        print('No ha habido suerte, ningun digito coincide')
        codigoUsu=int(input('Indroduce un nuevo codigo:'))
        
    

print('¡¡¡Fin de la partida!!! ')
print('Codigo secreto: ',codigoSecreto)
print('Numero de intetos:',intentos)
    