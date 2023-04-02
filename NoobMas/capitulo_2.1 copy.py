class Apagador:
    estado_actual = None

    def __init__(self):
        self.estado_actual = Encendido()

    def cambiar(self, estado_nuevo):
        if self.estado_actual.funciona:
            self.estado_actual = estado_nuevo
        self.estado_actual.imprimir()


class Estado:
    info = None
    funciona = True

    def imprimir(self):
        print(self.info)


class Apagado(Estado):
    info = "Esta Apagado"


class Encendido(Estado):
    info = "Esta Encendido"


class Roto(Estado):
    info = "Esta Molido"
    funciona = False


apagador = Apagador()
encendido = Encendido()
apagador.cambiar(encendido)
apagador.cambiar(Roto())
apagador.cambiar(Encendido())
