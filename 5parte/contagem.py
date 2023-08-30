def contagem():
    SomaM = 0
    SomaF = 0
    i = True
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
    return SomaM, SomaF

contagem