def conversor (tipo_precio , valor_dolar):
    pesos = input ("Cuantos pesos" + tipo_precio + "tienes?")
    pesos = float (pesos)
    dolares = pesos/valor_dolar
    dolares = round (dolares,4)
    dolares = str(dolares)
    print ("Tienes $", dolares, "dolares")

menu = """
Bienvenido 😍😍❤❤

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion : """

opcion = input(menu)
opcion = int(opcion)
if opcion == 1:
    conversor('colombianos',3875)
elif opcion == 2:
    conversor('argentino' , 65)
elif opcion == 3:
    conversor('mexicanos', 24)
else: 
    print ('Opcion incorrecta')