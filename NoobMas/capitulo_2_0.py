from time import sleep


class Stoplight:  # Context
    _state = None
    battery = 5

    def switch(self, state):
        if self.battery > 0:
            self._state = state
            self._state.context = self
            self._state.run()

    def __init__(self):
        self.switch(Green())


class StoplightState:  # State
    _color: None
    _wait_time: None
    _info: None

    def next(self):  # Set next State
        print("Error Malo Horrible")

    def run(self):
        print("El semaforo está en", self._color, self._info)
        print("Por favor, espere:", self._wait_time, "segundos")
        self.context.battery -= 1
        print("Estado de bateria:", self.context.battery)
        sleep(self._wait_time)
        self.next()


class Green(StoplightState):
    _color = "Verde"
    _wait_time = 5
    _info = "Puede avanzar"

    def next(self):
        # self.context.battery -= 1
        self.context.switch(Yellow())


class Yellow(StoplightState):
    _color = "Amarillo"
    _wait_time = 2
    _info = "Avance con cuidado"

    def next(self):
        self.context.switch(Red())


class Red(StoplightState):
    _color = "Rojo"
    _wait_time = 4
    _info = "Debe esperar para avanzar"

    def next(self):
        # self.context.battery -= 1
        self.context.switch(Green())


if __name__ == "__main__":
    Stoplight()
