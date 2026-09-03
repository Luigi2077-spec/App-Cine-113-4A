class Sala:

    def __init__(self, numero, capacidad):
        self.__numero = numero
        self.__capacidad = capacidad

    def mostrar_datos(self):
        print(f"Numero: {self.__numero}")
        print(f"Capacidad: {self.__capacidad}")

    def hay_disponibilidad(self, entradas_vendidas):
        if entradas_vendidas <= self.__capacidad:
            return "Hay disponibilidad"
        return "No hay salas"
