class ContaBancaria():

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def deposito(self, valor):
        self.saldo += valor
        return print(f'Com a adição de R${valor}, {self.titular} terá R${self.saldo}.')


    def sacar(self, valor):
        if valor > self.saldo:
            return print(f'{self.titular} não pode sacar o valor por saldo insuficiente.')
            
        else:      
            self.saldo -= valor
            return print(f'Com a retirada de R${valor}, {self.titular} terá R${self.saldo}.')
        

guilherme = ContaBancaria('Guilherme', 0)
guilherme.deposito(50)
guilherme.deposito(100)
guilherme.sacar(125)