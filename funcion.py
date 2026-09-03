class Funcion:

    def __init__(self, fecha, hora, precio):
        self.__fecha = fecha
        self.__hora = hora
        self.__precio = precio

    def mostrar_datos(self):
        return f"Fecha: {self.__fecha}\nHora: {self.__hora}\nPrecio: {self.__precio}"

    def es_funcion_nocturna(self):
        if self.__hora >= "20:00":
            return True
        else:
            return False

    #Tambien se puede hacer de esta manera:
    #def es_funcion_nocturna(self):
    # hora = int(self.__hora.split(":")[0])
    # if hora >= 20:   