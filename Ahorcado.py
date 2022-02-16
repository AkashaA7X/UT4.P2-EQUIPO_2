import time

print('*************************************')
print('                                     ')
print('          JUEGO AHORCADO             ')
print('                                     ')
print('      Pulsa ENTER para comenzar      ')
print('                                     ')
print('*************************************')

input()

time.sleep(2)
print("REGLAS: Debes adivinar la palabra secreta que ha colocado el jugador 1")
time.sleep(3)
print("Pulsa Enter para continuar")
input()
#La palabra secreta que introduzca estará en minusculas para favorecer la ejecución del programa
palabraSecreta=input('Introduce la palabra secreta:').lower()

##Dibujo del ahorcado
ahorcado=['''
     !=====N
     O     N
  / | \    N
  \ | /    N
   /\      N
  /  \     N
 _\  /_    N
           N''','''
     !=====N
     O     N
  / | \    N
  \ | /    N
   /       N
  /        N
 _\        N
           N''','''
     !=====N
     O     N
  / | \    N
  \ | /    N
           N
           N
           N
           N
           N''','''
     !=====N
     O     N
   / |     N
   \ |     N
           N
           N
           N
           N''','''
    
     !=====N
     O     N
     |     N
     |     N
           N
           N
           N
           N''','''
    
     !=====N
     O     N
           N
           N
           N
           N
           N
           N''','''
     !=====N
           N
           N
           N
           N
           N
           N''']

##Numero de vidas
vidas= 6
listaLetrasAdivinadas=[]
# Imprimir longitud de palabra
print(ahorcado[vidas])
print('_ ' *len(palabraSecreta))
#Boleano para salir por ganar el juego
ganaPalabra=False
ganaLetra=False
while True:
    while ganaPalabra==False or ganaLetra==False or vidas<=0:
        op=input("¿Que deseas introducir?\n 1-Letra \ 2-Palabra: ")
        
        if(op=='1'):
            while True:
                letraAdivinada= input("Introduce una letra:").lower()
                #En caso de que se haya introducido mas de un digito o sea un numero salta error
            
                if(letraAdivinada.isnumeric()):
                    print("Eso no es una letra, introduce una letra:")
                else:
                    if letraAdivinada.lower() in listaLetrasAdivinadas:
                        print("Ya lo intentaste con esa letra, prueba otra")
                        print("Letras intentadas :",listaLetrasAdivinadas)
                    else:
                        listaLetrasAdivinadas.append(letraAdivinada)
                        if(letraAdivinada.lower() in palabraSecreta):
                            #Cuando aciertas una letra, rompe el bucle y va a mostrar lo que ha ido consiguiendo el usuario
                            print("")
                            print("! BUEN TRABAJO !, Acertaste una letra")
                            print("")
                            break
                        else:
                            vidas-=1
                            print("Letra erronea...")
                            time.sleep(2)
                            print(ahorcado[vidas])
                            print("Pierdes una vida | VIDAS RESTANTES",vidas)
                            break
            #Se establece una variable para contar cuantas letras le faltan por adivinar
            letras_faltantes = 0
            estadoPalabra=''
            for letra in palabraSecreta:
                if letra in listaLetrasAdivinadas:
                    estadoPalabra = estadoPalabra + letra + " "
                else:
                    estadoPalabra = estadoPalabra + "_ "
                    letras_faltantes = letras_faltantes + 1
             
            ## Imprimir palabra con algunas letras
            print(estadoPalabra)
            if vidas<=0:
                break
            if letras_faltantes == 0 :
                print("!!!!FELICIDADES, HAS GANADO!!!!!")
                print("La palabra secreta es: " + palabraSecreta)
                ganaLetra=True
                break
        elif(op=='2'):    
            palabraAdivina=input('Introduce la palabra secreta:')
            if palabraAdivina.lower() == palabraSecreta.lower():
                print("!!!!FELICIDADES, HAS GANADO!!!!!")
                print("La palabra secreta es: " + palabraSecreta.lower())
                ganaPalabra=True
                break
            else:
                print(" HAS PERDIDO ")
                vidas=0
                break
        else:
            print("Debes elegir una opción válida:")
        
    if vidas<=0:
        print("Haz perdido la palabra secreta era: "+ palabraSecreta)
        break
    elif ganaPalabra==True:
        break
    elif ganaLetra==True:
        break
    
