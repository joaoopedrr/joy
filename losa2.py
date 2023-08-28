vel=float(input("Digite a velocidade que o carro percorreu: "))
if vel>80:
    multa=(vel-80)*7
    print("Você foi multado e a multa será de {}R$".format(multa))
else:
    print("Não foi multado")