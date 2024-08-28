import simpy
from random import random as rd
from math import log

def carro(env, bomba, num, ls):

    #Solicitud de carga de gasolina
    with bomba.request() as req:
        yield req

        #Se carga gasolina
        print(f'El carro {num} se comienza a cargar en el minuto {round(env.now, 2)}')
        carga = -log(rd())/ls
        yield env.timeout(carga)
        print(f'El carro {num} termina de cargar en el minuto {round(env.now, 2)}')

def gasolinera(env, bomba, num, ll, ls):
    for i in range(num):
        llegada = -log(rd())/ll
        yield env.timeout(llegada)
        print(f'Ha llegado el carro {i} en el minuto {round(env.now, 2)}')
        env.process(carro(env, bomba, i, ls))
        

entorno = simpy.Environment()
bomba = simpy.Resource(entorno, capacity=1)
entorno.process(gasolinera(entorno, bomba, 7, 1/2, 1/20))
entorno.run()


"""
def carro(env, bomba, num, ll, ls):
    llegada = -log(rd())/ll
    yield env.timeout(llegada)
    print(f'Ha llegado el carro {num} en el minuto {round(env.now, 2)}')

    #Solicitud de carga de gasolina
    with bomba.request() as req:
        yield req

        #Se carga gasolina
        print(f'El carro {num} se comienza a cargar en el minuto {round(env.now, 2)}')
        carga = -log(rd())/ls
        yield env.timeout(carga)
        print(f'El carro {num} termina de cargar en el minuto {round(env.now, 2)}')


entorno = simpy.Environment()
bomba = simpy.Resource(entorno, capacity=1)
for i in range(1,11):
    #LLegada de un carro 
    entorno.process(carro(entorno, bomba, i, 1, 1/40))
entorno.run()
"""