from pelicula import Pelicula
from funcion import Funcion
from sala import Sala
from cliente_normal import ClienteNormal
from cliente_premium import ClientePremium
from cliente import Cliente

def main():

    pelicula1 = Pelicula("El Padrino", "Drama", 175)
    pelicula2 = Pelicula("Mario", "Accion", 120)


    print(pelicula1.mostrar_datos())
    print("--------------------")
    print(pelicula2.mostrar_datos())

#Crear funcion

    funcion1 = Funcion("2023-06-15", "19:30", 10000)
    print(funcion1.mostrar_datos())
    print("--------------------")
    print("¿Es función nocturna?", "Sí" if funcion1.es_funcion_nocturna() else "No")



#Crear sala
    sala1= Sala(1,100)
    sala1.mostrar_datos()
    print(sala1.hay_disponibilidad(115))

#Crear cliente
    cliente_normal = ClienteNormal("Juan", "juan@email.com", 16)
    cliente_normal.mostrar_datos()
    print("Precio con descuento:", cliente_normal.calcular_precio(10000))

    cliente_premium = ClientePremium("pedro", "pedro@email.com", 17, 0.15, 100)
    cliente_premium.mostrar_datos()
    print("Precio con descuento:", cliente_premium.calcular_precio(10000))

      


if __name__ == "__main__":
    main()