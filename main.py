import sqlite3
import tkinter as tk

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
        

#GUI
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("400x500")

titulo = tk.Label(janela, text="Gerenciador de Tarefas")
titulo.pack()

desc_tarefa = tk.Entry(janela)
desc_tarefa.pack()

att_tarefas = tk.Listbox(janela)
att_tarefas.pack()

lista_ids = []


def clicar_adicionar():
    descricao = desc_tarefa.get()
    adicionar_tarefa(descricao)
    atualizar_tarefas()


def atualizar_tarefas():
    lista_ids.clear()
    ids_tarefas = lista_ids
    att_tarefas.delete(0, tk.END)
    cursor.execute("SELECT * FROM tarefas")
    atualizar = cursor.fetchall()
    for a in atualizar:
        if a[2] == False:
            ids_tarefas.append(a[0])
            att_tarefas.insert(tk.END, f"{a[1]}: [ ]")
        else:
            ids_tarefas.append(a[0])
            att_tarefas.insert(tk.END, f"{a[1]}: [X]")

def clicar_concluir():
    concluir = att_tarefas.curselection()
    posicao = concluir[0]
    id_real = lista_ids[posicao]
    concluir_tarefas(id_real)
    atualizar_tarefas()

def clicar_remover():
    remover = att_tarefas.curselection()
    p_remover = remover[0]
    id_real = lista_ids[p_remover]
    remover_tarefas(id_real)
    atualizar_tarefas()



btn_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=clicar_adicionar)
btn_adicionar.pack()

btn_concluir = tk.Button(janela, text="Concluir Tarefa", command= clicar_concluir)
btn_concluir.pack()

btn_remover = tk.Button(janela, text="Remover Tarefa", command= clicar_remover)
btn_remover.pack()
    
atualizar_tarefas()        
    

janela.mainloop()