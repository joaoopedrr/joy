##------------------------------------------------------------------------------------------------


# Crie um programa que receba uma idade e retorne se pode obter carteira de motorista(CNH)

##------------------------------------------------------------------------------------------------

# Entrada de Dados
from CNH import CNH

Idade = int(input("Insira a idade do avaliado: "))

# Avaliação dos dados

C = CNH(Idade)

# Saída de dados

print("A CNH do indivíduo é: {}.".format(C))