import sqlite3

conn = sqlite3.connect("banco_tarefas.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas(
      id INTEGER PRIMARY KEY,
      descricao TEXT,
      concluida BOOLEAN
    )
''')

conn.commit()

def adicionar_tarefa(descricao):
    cursor.execute("INSERT INTO tarefas(descricao, concluida) VALUES(?,?)", (descricao, False))
    conn.commit()


def listar_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    resultado = cursor.fetchall()
    for lista in resultado:
        if lista[2] == False:
            print(lista[1], "[ ]")
        else:
            print(lista[1], "[X]")


def concluir_tarefas(id):
    cursor.execute("UPDATE tarefas SET concluida =? WHERE id=?",(True, id))
    conn.commit()


def remover_tarefas(id):
    cursor.execute("DELETE FROM tarefas WHERE id=?", (id,))
    conn.commit()

def menu():
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
            adicionar_tarefa(descricao=adicionar)

        elif escolha == "2":
            listar_tarefas()

        elif escolha == "3":
            concluir = input("Qual tarefa quer concluir: ")
            concluir_tarefas(int(concluir))

        elif escolha == "4":
            remover = input("Qual tarefas quer remover: ")
            remover_tarefas(int(remover))

        elif escolha == "5":
            break

        else:
            print("Escolha somente um dos números informados.")
        

#Testes

menu()
    