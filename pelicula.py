class Pelicula:

    def __init__(self, titulo, genero, duracion):
        self.__titulo = titulo
        self.__genero = genero
        self.__duracion = duracion

    def mostrar_datos(self):
        return f"titulo: {self.__titulo}\ngenero: {self.__genero}\nduracion: {self.__duracion}"

    #si dijera void en el diagrama tendria que poner print de esta manera: 
    #print(f"titulo: {self.__titulo}\ngenero: {self.__genero}\nduracion: {self.__duracion}")