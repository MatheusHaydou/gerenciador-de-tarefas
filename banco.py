import sqlite3
from tarefa import Tarefa

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
    tarefas_listadas = []
    for lista in resultado:
        nova_tarefa = Tarefa(lista[0], lista[1], lista[2])
        tarefas_listadas.append(nova_tarefa)
    return tarefas_listadas
        


def concluir_tarefas(id):
    cursor.execute("UPDATE tarefas SET concluida =? WHERE id=?",(True, id))
    conn.commit()


def remover_tarefas(id):
    cursor.execute("DELETE FROM tarefas WHERE id=?", (id,))
    conn.commit()