from distutils.command.clean import clean
import time
from turtle import clear
import getpass

print('*************************************')
print('                                     ')
print('          JUEGO AHORCADO             ')
print('                                     ')
print('      Pulsa ENTER para comenzar      ')
print('                                     ')
print('*************************************')

input()
print("....")
time.sleep(2)
print("REGLAS: Debes adivinar la palabra secreta que ha colocado el jugador 1")
time.sleep(3)
print("Pulsa Enter para continuar")
input()
palabraSecreta= getpass.getpass('JUGADOR 1: Introduzca palabra secreta:')

##Numero de vidas
vidas= 5
listaLetrasAdivinadas=[]
# Imprimir longitud de palabra
print('_ ' *len(palabraSecreta))

while True:
    while True:
        letraAdivinada= input("Introduce una letra:")
        #En caso de que se haya introducido mas de un digito o sea un numero salta error
        if(len(letraAdivinada)!=1 and letraAdivinada.isnumeric()):
            print("Eso no es una letra, introduce una letra:")
        else:
            if letraAdivinada.lower() in listaLetrasAdivinadas:
                print("Ya lo intentaste con esa letra, prueba otra")
                print("Letras intentadas :",listaLetrasAdivinadas)
            else:
                listaLetrasAdivinadas.append(letraAdivinada)
                if(letraAdivinada.lower() in palabraSecreta):
                    #Cuando aciertas una letra, rompe el bucle y va a mostrar lo que ha ido consiguiendo el usuario
                    print("¡BUEN TRABAJO !, Acertaste una letra")
                    break
                else:
                    vidas-=1
                    print("Letra erronea...")
                    time.sleep(2)
                    print("Pierdes una vida")
                    print("Vidas restantes: ",vidas)
                    break
    if vidas<=0:
        print("Haz perdido la palabra secreta era: "+ palabraSecreta)
        break
    #Se establece una variable para contar cuantas letras le faltan por adivinar
    letras_faltantes = 0
    estadoPalabra=''
    for letra in palabraSecreta:
        if letra in listaLetrasAdivinadas:
            estadoPalabra = estadoPalabra + letra
        else:
            estadoPalabra = estadoPalabra + "_"
            letras_faltantes = letras_faltantes + 1
 
    ## Imprimir palabra con algunas letras
    print(estadoPalabra)
 
 
    if letras_faltantes == 0:
        print("Felicidades haz ganado")
        print("La palabra secreta es: " + palabraSecreta)
        break