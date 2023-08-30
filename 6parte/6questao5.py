##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# 5 polimorfism 
# Crie uma classe base chamada Animal com métodos para emitir um som e mostrar informações gerais. 
# Crie subclasses como Cachorro e Gato que herdam de Animal e implementam seus próprios métodos para emitir sons específicos.

##------------------------------------------------------------------------------------------------

class Animal:
    def __init__(self, nome, classificacao, raca):
        self.nome = nome
        self.classificacao = classificacao
        self.raca = raca

    def emitir_som(self):
        pass

    def informacoes(self):
        print(f"Nome:{self.nome}, Classificacao:{self.classificacao} e Raça/Cor:{self.raca}.")


class Cachorro(Animal):
    def __init__(self,nome,classificacao,raca):
        super().__init__(nome,classificacao, raca)
        self.raca =raca

    def emitir_som(self):
        return "Au Au"
    
class Gato(Animal):
    def __init__(self, nome, classificacao, raca):
        super().__init__(nome,classificacao, raca)
        self.raca = raca

    def emitir_som(self):
        return "Miau Miau"
    
class Humano(Animal):
    def __init__(self, nome, classificacao, cor):
        super().__init__(nome, classificacao, cor)
        self.cor = cor

    def emitir_som(self):
        return "Alguma coisa."
    
cachorro = Cachorro("Berilio", "Canideo", "Fox Paulistinha")
gato = Gato("Jorel", "Felineo", "SRD")
humano = Humano("Lucas", "Homínideo", "Pardo")

animais = [cachorro, gato, humano]

for animal in animais:
    animal.informacoes()
    print(animal.emitir_som())
    print()