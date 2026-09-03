from pelicula import Pelicula
from funcion import Funcion
from sala import Sala

def main():

    pelicula1 = Pelicula("El Padrino", "Drama", 175)
    pelicula2 = Pelicula("Mario", "Accion", 120)


    print(pelicula1.mostrar_datos())
    print("--------------------")
    print(pelicula2.mostrar_datos())

#Crear funcion

    funcion1 = Funcion("2023-06-15", "19:30", 10.0)
    print(funcion1.mostrar_datos())
    print("--------------------")
    print(f"¿Es función nocturna? {funcion1.es_funcion_nocturna()}")

#Crear sala
sala1= Sala(1,100)
print(sala1.mostrar_datos())
print(sala1.hay_disponibilidad(115))




if __name__ == "__main__":
    main()