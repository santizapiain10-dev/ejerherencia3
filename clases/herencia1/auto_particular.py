from clases.herencia1.vehiculo import Vehiculo

class AutoParticular(Vehiculo):

    def __init__(self, matricula, modelo, potenciaCV, numeroPuertas):
        super().__init__(matricula, modelo, potenciaCV)
        self.numeroPuertas = numeroPuertas

    def __str__(self):
        return super().__str__() + " " + str(self.numeroPuertas)

    def abrirPuertas(self):
        print("Abriendo puertas...")

    def cerrarPuertas(self):
        print("Cerrando puertas...")