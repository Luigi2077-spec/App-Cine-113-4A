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
        pass