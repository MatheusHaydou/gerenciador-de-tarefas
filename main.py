def adicionar_tarefa(tarefas, descricao):
    lista_tarefas = {"descricao": descricao, "concluida": False}
    tarefas.append(lista_tarefas)


def listar_tarefas(tarefas):
    for lista in tarefas:
        if lista["concluida"] == False:
            print(lista["descricao"], "[ ]")
        else:
            print(lista["descricao"], "[X]")


def concluir_tarefas(tarefas, indice):
    tarefas[indice]["concluida"] = True


def remover_tarefas(tarefas, indice):
    tarefas.pop(indice)

def menu():
    tarefas =[]
    while True:
        escolha = input(" \n"
                    "1 - Adicionar tarefa \n"
                    "2 - Listar tarefas \n"
                    "3 - Concluir tarefa \n"
                    "4 - Remover tarefa \n"
                    "5 - Sair \n"
                    "Escolha uma opção: ")
        print(" ")
        if escolha == "1":
            adicionar = input("Adicione as tarefas: ") 
            adicionar_tarefa(tarefas, adicionar)

        elif escolha == "2":
            listar_tarefas(tarefas)

        elif escolha == "3":
            concluir = input("Escolha o número da tarefa: ")
            concluir_tarefas(tarefas, int(concluir))

        elif escolha == "4":
            remover = input("Escolha o número da tarefa: ")
            remover_tarefas(tarefas, int(remover))

        elif escolha == "5":
            break

        else:
            print("Escolha somente um dos números informados.")
        

#Testes

menu()
    