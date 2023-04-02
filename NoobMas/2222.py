from time import sleep


class StopLight:
    def __init__(self):
        self.state = Green(self)

    def switch(self, state):
        self.state = state
        self.run()

    def run(self):
        self.state.run()


class State:
    def __init__(self, context):
        self.context = context

    def run(self):
        raise NotImplementedError


class Green(State):
    def run(self):
        print("El semáforo está en verde. Puede avanzar.")
        sleep(5)
        self.context.switch(Yellow(self.context))


class Yellow(State):
    def run(self):
        print("El semáforo está en amarillo. Avance con cuidado.")
        sleep(2)
        self.context.switch(Red(self.context))


class Red(State):
    def run(self):
        print("El semáforo está en rojo. Debe esperar para avanzar.")
        sleep(4)
        self.context.switch(Green(self.context))


if __name__ == "__main__":
    stoplight = StopLight()
    stoplight.run()
