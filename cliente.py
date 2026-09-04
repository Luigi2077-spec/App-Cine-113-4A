class Cliente:

    def __init__(self, nombre, correo, edad):
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad

    def mostrar_datos(self):
        print(f"nombre {self.__nombre}")
        print(f"correo {self.__correo}")
        print(f"edad {self.__edad}")

    def calcular_precio(self, precio):
        if self.__edad < 18:
            return precio * 0.8  # Aplicar descuento del 20% para menores de edad
        return precio