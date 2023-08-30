def selecao (Num1, Num2, Num3):

    maior = Num1

    if Num2 > Num1 and Num2 > Num3:

        maior = Num2

    if Num3 > Num1 and Num3 > Num2:

        maior = Num3

    menor = Num1

    if Num2 < Num3 and Num2 < Num1:

        menor = Num2

    if Num3 < Num2 and Num3 < Num1:

        menor = Num3

    return maior, menor