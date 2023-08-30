class Carro():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self, acelerar):
        if acelerar > 0:
            print(f'O  carro de marca {self.marca} e modelo {self.modelo} de {self.ano} está a {acelerar} km/h.')
        else:
            print(f'O  carro de marca {self.marca} e modelo {self.modelo} de {self.ano} está parado.')

carrinho = Carro("Ford", "Ranger", 2015)


carrinho.acelerar(0)
carrinho.acelerar(50)