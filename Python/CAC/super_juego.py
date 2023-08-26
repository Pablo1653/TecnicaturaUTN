import random  # importo modulo random


class Dado:
    # gralmente para definir bien oop en el init se inicializan  de valores que seran los atributos de instancia de la clase
    def __init__(self):
        # se ponen en el init porque el init siempre lo voy a correr una vez que instancio un objeto
        # y me aseguro que se inicilizara
        # estado esta definido por el valor
        # Inicializo en 1 podria inicializar en otro o random
        self.__valor = 1

# tirar es el comportamiento que me va  a modificar el estado ,dado que le cambio el valor
# el self quiere decir que le estoy hablando a la instancia de esa clase
# la primer palabra que le ponga va a representar la instancia de esta clase
# como primer parametro reciben la instancia
    def tirar(self):
        self.__valor = random.randint(1, 6)

    # en objeto se le dice metodo pero es lo mismo que función
    def imprimir(self):
        print(f"Salió: {self.__valor}")
    # en py puedo definir objetos con atributo de instancia que lo puedo crear aca e inclusive fuera del codigo

    def obtener_valor(self):
        return self.__valor

    # con _ o __ le digo simular que es  privado y que solo se podra acceder desde sus metodos
    # metodo que tambien retorna un string como str
    # como se va a representar en un formato string
    # str es mas informal
    # mas orientado al desarrollador,se usa mas para el debug
    def __repr__(self):
        return f"Dado({self.__valor})"

    # str esta mas orientado al usuario,se usa mas para el print
    def __str__(self):
        return f"{self.__valor}"
    # para que mi objeto pueda dar acceso a esas variables privadas ,sin pasar las a publico

    # para obtener el valor ,llamo a esa funcion decoratorproperty
    # decorator
    # mi getter y setter me encapsulan mi atributo privado
    # a partir de estos puedo condicionar los valores porque los manejo yo dentro de la clase
    # escribo la property porque le estoy diciendo en mi clase que pueden acceder a ese valor, yo lo dejo
    # si yo no quiero que accedan de ninguna forma no le doy el getter y el setter
    @property  # este es el getter
    def valor(self):
        return self.__valor

    # guardar el valor con un parametro que esta recibiendo
    @valor.setter
    def valor(self, pNuevoValor):
        # yo aca estoy manejando mi estructura interna cuando me brinda un valor
        # aca le digo que si o si sera tal valor y no me lo pueden cambiar porque esta como privada
        if pNuevoValor > 6 or pNuevoValor < 0:
            print("no se puede hacer ")
            self.__valor = pNuevoValor
        else:
            self.__valor = pNuevoValor

    # encapsulo a partir del getter and setter con el decorator

    # si yo quiero poo debo encapsular ,agregando una propiedad que me encapsula en este caso valor
    # ejemplo seria que quiero generar
    # ejemplo : mas variables en lugar de 1 ,ejem 6 solo tengo que cambiar tirar y obtener no afectaria al programa

    # quiero encapsular el valor, dado que yo quiero mostrar pero no que lo pueden meter mano
    # mi atributo seria el bolsillo que no quiero que me toquen

# ambas clases acopladas , buscamos bajo acoplamiento y alta cohesion.
# ejemplo se inventa un dado de 12 lados y todo sigue funcionando
# es decir que las clases se relacionen lo menos posible y la clase haga lo especifico de esa clase
# si yo modifico una clase que no rompa todo


class JuegoDado:
    def __init__(self):
        self.dado_1 = Dado()
        self.dado_2 = Dado()
        self.dado_3 = Dado()

    def jugar(self):
        self.dado_1.tirar()
        self.dado_1.imprimir()
        self.dado_2.tirar()
        self.dado_2.imprimir()
        self.dado_3.tirar()
        self.dado_3.imprimir()

        self.dado_1.valor = 12
        # aca ya es un atributo ,representa un estado de esa entidad ,teniento control sobre eso
        if self.dado_1.valor() == self.dado_2.valor == self.dado_3.valor:
            print("Gano")

        # aca me estoy metiendo en atributo interno , pero en py no hay atributos privados
        if self.dado_1.__valor == self.dado_2.__valor == self.dado_3.__valor:
            print("ganaste")

        # atributo privado cuando solo lo pueden manejar metodos de la misma clase
        # en este caso seria los que estan dentro de clase Dado
        # desde otras clases, objetos y/o instancias fuera no podra

        # manejando encapsulamiento donde no queremos meternos en la estreuctura interna de los dados
        # solo quiero que el dado me de el valor
        if self.dado_1.obtener_valor() == self.dado_2.obtener_valor() == self.dado_3.obtener_valor():
            print("Ganaste")
        else:
            print("Perdiste")


# defino variable mi juego
mi_juego = JuegoDado()
mi_juego.jugar()
