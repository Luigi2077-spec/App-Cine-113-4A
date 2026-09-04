from cliente import Cliente


class ClientePremium(Cliente):

    def __init__(self, nombre, correo, edad, descuento, puntos):
        super().__init__(nombre, correo, edad)
        self.__descuento = descuento
        self.__puntos = puntos

    def calcular_precio(self, precio):
        precio = super().calcular_precio(precio)
        print("Precio después del descuento de menor de edad:", precio)

        total = precio * (1 - self.__descuento)
        return f"Precio con descuento: {total}"

    def Acumular_puntos(self, puntos):
        self.__puntos += puntos