##------------------------------------------------------------------------------------------------


# Crie um programa que simule uma fila de tarefas a serem executadas. 
# O usuário deve poder adicionar tarefas à fila e retirá-las na ordem em que foram adicionadas.

##------------------------------------------------------------------------------------------------

# Entrada de Dados

i = True
Tarefas = []

while i == True:
    R = input("Qual ação gostaria de tomar? Adicionar Tarefa (1), Realizar Tarefa (2) ou Sair (3)")   

    if R == "1":
        I = input("Qual tarefa deseja adicionar à fila de tarefas? ")
        Tarefas.append(I)
    elif R == "2":    
        T = Tarefas.pop(0)
        print("Foi realizada a tarefa de {}." .format(T))

    elif R == "3":
        i = False
    else:
        print("Escolha não autorizada.")
    
    if len(Tarefas) == 0:
        print("Não há mais nenhuma tarefa para executar.")

        I = input("Qual tarefa deseja adicionar à fila de tarefas? ")

        Tarefas.append(I)
        
        if len(Tarefas) == 0:
            i = False





