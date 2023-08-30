##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Utilizando estrutura de repeticao while crie um programa que faça a soma de todos os numeros digitados. o loop so devera parar quando for digitado 0

##------------------------------------------------------------------------------------------------

# Entrada de Dados

i = True
Soma = 0

# Estrutura de Loop para soma de números

while i == True:
    N = float(input("Digite o número a ser somado (caso escreva 0 a soma terminará): "))
    Soma = N + Soma
    if N == 0:
        i = False

# Saída de Dados

print("A soma dos números é {}.".format(Soma))