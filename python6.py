#Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable.
# A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

cant = input('Indique cantidad de show vistos en el ultimo año')
cant = int(cant)
if (cant>3): 
    print ('True')
else:
    print ('False')