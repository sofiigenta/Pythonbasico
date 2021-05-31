import random

def run():
    numero = int(input('Escribe un numero'))
    numero_aleatorio = random.randint(1,100)
    while numero != numero_aleatorio:
        if numero_aleatorio > numero:
            print ('Elige un numero mayor')
        else : 
            print('Elige un numero menor')
        numero = int(input('Escribe otro numero'))
    print ('Ganaste!!❤')

if __name__ == '__main__':
    run()




