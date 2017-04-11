#! /usr/bin/env python3
def createDictionary():
    spanish = dict()
    spanish['hello']='hola'
    spanish['yes']='si'
    spanish['one']='uno'
    spanish['two']='dos'
    spanish['three']='tres'
    spanish['four']='cuatro'
    spanish['black']='negro'
    spanish['green']='verde'
    spanish['blue']='azul'
    spanish['red']='rojo'
    return spanish

def main():
    dictionary = createDictionary()
    print(dictionary['two'])

main()
