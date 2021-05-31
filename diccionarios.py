def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
   }
   # print (mi_diccionario['llave1'])
   # print (mi_diccionario['llave2'])
   # print (mi_diccionario['llave3'])
    participantes_paises = {
       'Argentina': 43,
       'Brasil': 21,
       'Colombia': 32
    }
    #print(participantes_paises['Colombia']
    # for pais in participantes_paises.keys():
    #   print(pais)
    # for pais in participantes_paises.values():
    #   print(pais)
    for pais, participantes in participantes_paises.items():
        print(pais, 'tiene', str(participantes) , 'participantes')

if __name__ == '__main__':
    run()