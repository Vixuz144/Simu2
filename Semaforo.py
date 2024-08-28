import simpy 

def main():
    env = simpy.Environment()
    env.process(semaforo(env))
    env.run(until=1200)
    print("Simulation complete")
    print(env)
    print(type(env))

def semaforo(env):
    while True:
        print(f'Luz verde en t = {env.now}')
        yield env.timeout(30)
        print(f'Luz amarilla en t = {env.now}')
        yield env.timeout(5)
        print(f'Luz roja en t = {env.now}')
        yield env.timeout(20)   

if __name__ == '__main__':
    main()