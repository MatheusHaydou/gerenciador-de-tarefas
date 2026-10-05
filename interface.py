from banco import adicionar_tarefa, listar_tarefas, concluir_tarefas, remover_tarefas, cursor
import tkinter as tk
from plyer import notification

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("400x500")


titulo = tk.Label(janela, text="Gerenciador de Tarefas", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

desc_tarefa = tk.Entry(janela)
desc_tarefa.pack(pady=8)

att_tarefas = tk.Listbox(janela)
att_tarefas.pack(pady=8)

lista_ids = []


def clicar_adicionar():
    descricao = desc_tarefa.get()
    adicionar_tarefa(descricao)
    atualizar_tarefas()
    notification.notify(
        title = "Tarefa Adicionada",
        message = descricao,
        timeout = 5
    )


def atualizar_tarefas():
    lista_ids.clear()
    ids_tarefas = lista_ids
    att_tarefas.delete(0, tk.END)
    tarefas_registradas = listar_tarefas()
    for a in tarefas_registradas:
        if a.concluida == False:
            ids_tarefas.append(a.id)
            att_tarefas.insert(tk.END, f"{a.descricao}: [ ]")
        else:
            ids_tarefas.append(a.id)
            att_tarefas.insert(tk.END, f"{a.descricao}: [X]")
    

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

def notificacao_pendentes():
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    pendentes = []
    for p in tarefas:
        if p[2] == False:
                pendentes.append(p[1])
    tarefas_pendentes = "\n".join(pendentes)
    notification.notify(
            title = "Tarefas Pendentes",
            message = tarefas_pendentes,
            timeout = 5
        )

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=8)


btn_adicionar = tk.Button(frame_botoes, text="Adicionar Tarefa", command=clicar_adicionar)
btn_adicionar.pack(side="left", padx=5)

btn_concluir = tk.Button(frame_botoes, text="Concluir Tarefa", command= clicar_concluir)
btn_concluir.pack(side="left", padx=5)

btn_remover = tk.Button(frame_botoes, text="Remover Tarefa", command= clicar_remover)
btn_remover.pack(side="left", padx=5)