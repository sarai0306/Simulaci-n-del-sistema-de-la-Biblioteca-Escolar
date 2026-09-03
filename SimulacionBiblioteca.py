import simpy, random
from colorama import Fore, Style

#entidad principal de la simulación

def estudiante(env, nombre, bibliotecario):
    llegada = env.now
    print(f"{env.now:.2f} - {nombre} llega a la biblioteca y busca su libro")

    with bibliotecario.request() as solicitud:
        yield solicitud

        espera= env.now - llegada

        print(Fore.Green + f"{env.now:.2f}-{nombre} empieza el registro del libro a prestar"
              f"(esperó{espera:.2f} min)" + Style.RESET_ALL)

        tiempo_registro = random.randint (2, 5)
        yield env.timeout (tiempo_registro)

        print (f"{env.now:.2f}- {nombre} recibe su ticket y el  libro prestado. Sale de la biblioteca")

#creando el entorno
env = simpy.Environment()

#Definiendo recursos: 1 bibliotecario disponible
bibliotecario=simpy.Resource(env, capacity = 1)

# Generar eventos (atención a cada cliente)
env.process(estudiante(env, "Ana", bibliotecario))
env.process(estudiante(env, "Carlos", bibliotecario))
env.process(estudiante(env, "Diana", bibliotecario))
env.process(estudiante(env, "Eduardo", bibliotecario))

# Ejecutar simulación durante 30 minutos
env.run(until=30)

print("Simulación finalizada")