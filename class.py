class Cachorro ():
    def __init__(self, nombre, juguete_favorito):
         self.nombre = nombre
         self.juguete_favorito =  juguete_favorito

    def jugar(self):
        print(f"{self.nombre} está jugando con su {self.juguete_favorito}!")
coca = Cachorro("Coca", "pelota")
coca.jugar()