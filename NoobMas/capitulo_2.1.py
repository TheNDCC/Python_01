import time

class EstadoSemaforo:
    semaforo = None
    def __init__(self, semaforo):
        self.semaforo = semaforo

    def ejecutar(self):
        pass

    def __str__(self):
        pass

class EstadoVerde(EstadoSemaforo):
    def ejecutar(self):
        print("El semáforo está en verde. Puede avanzar.")
        time.sleep(5)
        self.cambiar_estado(EstadoAmarillo())

    def __str__(self):
        return "verde"

class EstadoAmarillo(EstadoSemaforo):
    def ejecutar(self):
        print("El semáforo está en amarillo. Avance con cuidado.")
        time.sleep(2)
        self.semaforo.cambiar_estado(EstadoRojo())

    def __str__(self):
        return "amarillo"

class EstadoRojo(EstadoSemaforo):
    def ejecutar(self):
        print("El semáforo está en rojo. Debe esperar para avanzar.")
        time.sleep(4)
        self.semaforo.cambiar_estado(EstadoVerde())

    def __str__(self):
        return "rojo"

class Semaforo:
    def __init__(self):
        self.cambiar_estado(EstadoVerde())
        self.estado_actual.semaforo = self
        self.ejecutar()

    def cambiar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado

    def ejecutar(self):
        self.estado_actual.ejecutar()

    def __str__(self):
        return "El semáforo está en estado {}".format(self.estado_actual)

# Ejemplo de uso
semaforo = Semaforo()
for i in range(10):
    print(semaforo)
    semaforo.ejecutar()
