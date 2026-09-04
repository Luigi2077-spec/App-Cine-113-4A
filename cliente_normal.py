from cliente import Cliente


class ClienteNormal(Cliente):

    def calcular_precio(self, precio):
        if self._Cliente__edad < 18:
            return precio * 0.8  # Aplicar descuento del 20% para menores de edad
        return precio