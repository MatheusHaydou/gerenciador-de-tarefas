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