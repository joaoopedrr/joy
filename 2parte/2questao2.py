num1=int(input("Digite o número1: "))
num2=int(input("Digite o número2: "))
num3=int(input("Digite o número3: "))
if num1 > num2 and num1 > num3 and num2<num3:
    print("O número 1 é o maior e o número 2 é o menor")
elif num1 > num2 and num1 > num3 and num3<num2:
    print("O número 1 é o maior e o número 3 é o menor")
elif num2 > num1 and num2 > num3 and num1 < num3:
    print("O número 2 é o maior e o número 1 é o menor")
elif num2 > num1 and num2 > num3 and num1 > num3:
    print("O número 2 é o maior e o número 3 é o menor")
elif num3 > num1 and num3 > num2 and num1 > num2:
    print("O número 3 é o maior e o número 2 é o menor")
elif num3 > num1 and num3 > num2 and num2 > num1:
    print("O número 3 é o maior e o número 1 é o menor")
