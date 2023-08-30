##------------------------------------------------------------------------------------------------


# Utilizando estrutura de repeticao while crie um programa que leia exclusivamente o sexo como 'F' e 'M' e o loop so deve terminar quando sexo for = sair. ao fim mostre a quantidade e mulheres e homens

##------------------------------------------------------------------------------------------------

# Entrada de Dados

i = True
SomaM = 0
SomaF = 0

# Estrutura de Loop para contagem

while i == True:
    N = input("Digite 'M' se o indivíduo for homem, 'F' se for mulher e 'sair' se for finalizar a contagem: ")
    
    if N == "M":
        SomaM += 1
    elif N == "F":
        SomaF += 1
    elif N == "sair":
        i = False
    else:
        print("Valor inválido, insira novamente.")

# Saída de Dados

print("Foram contados {} homens e {} mulheres.".format(SomaM, SomaF))