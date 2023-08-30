# Utilizando estrutura de repeticao while crie um programa que leia exclusivamente o sexo como 'F' e 'M' e o loop so deve terminar quando sexo for = sair. ao fim mostre a quantidade e mulheres e homens

##------------------------------------------------------------------------------------------------

# Entrada de Dados

from contagem import contagem

# Estrutura de Loop para contagem

SomaM, SomaF = contagem()

# Saída de Dados

print("Foram contados {} homens e {} mulheres.".format(SomaM, SomaF))