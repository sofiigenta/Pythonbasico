#Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. 
# Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

numero1 = input('Ingrese el primer numero')
numero1 = int(numero1)
numero2 = input('Ingrese el segundo numero')
numero2 = int(numero2)
numero3 = numero1+numero2
numero4 = input ('Ingrese el tercer numero')
numero4 = int(numero4)
numero5 = numero4 * numero3
print ('El resultado de la multiplicacion de ' , numero4 , 'x' , numero3 , 'es' ,numero5)