# Gerenciador de Tarefas
 
Aplicação desktop de gerenciamento de tarefas (To-Do List) desenvolvida em Python, com interface gráfica, persistência de dados em banco SQLite e notificações do sistema operacional.
 
![Python](https://img.shields.io/badge/Python-3.14-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
 
## Sobre o projeto
 
Este projeto foi construído como um estudo prático, evoluindo em fases — do CRUD mais simples possível até um aplicativo funcional com interface gráfica e integração com o sistema operacional.
 
### Funcionalidades
 
- Adicionar novas tarefas
- Listar todas as tarefas cadastradas
- Marcar tarefas como concluídas
- Remover tarefas
- Persistência de dados (as tarefas não se perdem ao fechar o programa)
- Notificação de confirmação ao adicionar uma tarefa
- Notificação com o resumo de tarefas pendentes ao abrir o programa
## Tecnologias utilizadas
 
- **Python** — linguagem principal do projeto
- **SQLite** (`sqlite3`) — banco de dados para persistência das tarefas
- **Tkinter** — biblioteca padrão do Python para construção da interface gráfica
- **Plyer** — biblioteca para notificações nativas do sistema operacional
## Como executar
 
### Pré-requisitos
 
- Python 3 instalado
- Biblioteca `plyer` instalada
### Instalação
 
```bash
# Clone o repositório
git clone https://github.com/MatheusHaydou/gerenciador-de-tarefas.git
 
# Acesse a pasta do projeto
cd gerenciador-de-tarefas
 
# Instale a dependência
pip install plyer
```
 
### Executando
 
```bash
python main.py
```
 
Ao rodar, uma janela será aberta com o gerenciador de tarefas. Um arquivo `banco_tarefas.db` será criado automaticamente na primeira execução, para armazenar as tarefas.
 
## Como usar
 
1. Digite a descrição de uma tarefa no campo de texto e clique em **"Adicionar Tarefa"**
2. As tarefas aparecem na lista, marcadas com `[ ]` (pendente) ou `[X]` (concluída)
3. Selecione uma tarefa na lista e clique em **"Concluir Tarefa"** para marcá-la como feita
4. Selecione uma tarefa na lista e clique em **"Remover Tarefa"** para excluí-la
5. Ao abrir o programa, uma notificação mostra quais tarefas ainda estão pendentes
## Jornada do projeto
 
O projeto foi desenvolvido em 4 fases incrementais, como parte de um processo de estudo:
 
1. **CRUD em memória** — lógica de adicionar, listar, concluir e remover tarefas, usando listas e dicionários em Python, rodando no terminal
2. **Persistência com SQLite** — substituição das listas em memória por um banco de dados real, com `INSERT`, `SELECT`, `UPDATE` e `DELETE`
3. **Interface gráfica com Tkinter** — construção de uma janela visual com campo de texto, lista de tarefas e botões, substituindo o menu de terminal
4. **Notificações do sistema** — integração com a biblioteca `plyer` para notificações nativas do Windows
## Possíveis melhorias futuras
 
- Separar o código em múltiplos arquivos (ex: `banco.py`, `interface.py`, `main.py`)
- Adicionar edição de tarefas já existentes
- Adicionar categorias ou prioridades às tarefas
- Lembretes agendados por data/horário
## Autor
 
Desenvolvido por [Matheus Haydou](https://github.com/MatheusHaydou) como projeto de estudo.