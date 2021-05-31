def run():
    #for contador in range (1000):
     #   if contador % 2 != 0:
      #      continue
       # print (contador)
    
    #for i in range (2,20):
     #   if i == 15:
      #      break
      #  print(i)
    frase = input ('Ingrese una frase')
    for letra in frase:
        if letra == 'p':
            break
        print (letra)

if __name__ == '__main__':
    run()