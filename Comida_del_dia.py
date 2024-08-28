import numpy as np
from random import random
import simpy

def desayuno(env):
    #bebida
    bebidas = ['leche', 'chocolate', 'café', 'jugo', 'licuado']
    p = [0.10, 0.15, 0.35, 0.25, 0.15]
    tb = [1, 2, 5, 15, 7]
    b = random()
    k = 0
    bebida = ''
    while b > sum(p[:k+1]):
        bebida = bebidas[k]
        k += 1
    yield env.timeout(round(-np.log(random())*tb[k]))

    #huevo
    if k-1 == 3:
        th = 10
    else:
        th = 15
    yield env.timeout(round(-np.log(random())*th))

    #complemento (pan, tortilla, fruta, galleta, etc.)
    yield env.timeout(round(-np.log(random())*10))
    return bebida+', huevo y algo más'


def almuerzo(env):
    soa = random()
    if soa <= 0.5:
        #sopa
        SOA = 'sopa'
        yield env.timeout(round(-np.log(random())*7))
    else:
        #arroz
        SOA = 'arroz'
        yield env.timeout(round(-np.log(random())*5))
    
    #guisado
    yield env.timeout(round(-np.log(random())*15))

    #postre
    yield env.timeout(round(-np.log(random())*5))
    return SOA+', guisado y un postre'

def cena(env):
    #bebida
    bebidas = ['leche', 'licuado', 'té']
    p = [0.40, 0.20, 0.40]
    tb = [1, 7, 15]
    b = random()
    k = 1
    bebida = ''
    while b > sum(p[:k]):
        bebida = bebidas[k-1]
        k += 1
    yield env.timeout(round(-np.log(random())*tb[k-1]))

    #comida
    cosa = ['pan', 'lo que sobró']
    p = [0.40, 0.60]
    tc = [5, 15]
    c = random()
    k = 1
    cen = ''
    while c > sum(p[:k]):
        cen = cosa[k-1]
        k += 1
    yield env.timeout(round(-np.log(random())*tc[k-1]))
    return f'{bebida} y {cen}'

def comida(env):
    while True:
        yield env.timeout(round(-np.log(random())*(7*60)))
        des = desayuno(env)
        print(f'Desayuné {des} a las {env.now}')


        yield env.timeout(round(-np.log(random())*(7*60)))
        alm = almuerzo(env)
        print(f'Almorcé {alm} a las {env.now}')

        yield env.timeout(round(-np.log(random())*(7*60)))
        cen = cena(env)
        print(f'Cené {cen} a las {env.now}')
    

def prueba(env):
    while True:
        yield env.timeout(-np.log(random())*2)
        print(env.now)

if __name__ == '__main__':
    ent = simpy.Environment()
    ent.process(comida(ent))
    # ent.process(prueba(ent))
    ent.run(until=400*60)