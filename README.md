Projeto: Formulário de Tarefas com Flask

Descrição:
Este projeto é uma aplicação web para gerenciamento de tarefas. 

Funcionalidades principais:
- Tela de login com email e senha.
- Cadastro de novos usuários.
- Após login, o usuário pode criar tarefas associadas a categorias.
- As tarefas e usuários são armazenados em um banco de dados SQLite.
- A aplicação foi desenvolvida com Flask, um microframework Python, utilizando PyCharm como IDE.

Tecnologias usadas:
- Python 3.x
- Flask
- Flask-Login (para autenticação)
- Flask-WTF (para formulários)
- Flask-Bcrypt (para hash de senhas)
- Flask-SQLAlchemy (para ORM e banco SQLite)
- SQLite (banco de dados local)

Como rodar o projeto:
1. Clone o repositório.
2. Crie um ambiente virtual (recomendado).
3. Instale as dependências:
   pip install -r requirements.txt
4. Execute o script para criar o banco de dados:
   python criar_banco.py
5. Rode a aplicação:
   python app.py
6. Acesse no navegador:
   http://localhost:5000

Observações:
- Certifique-se de ter o Python 3 instalado.
- As categorias padrão são criadas automaticamente na criação do banco.
- Use o formulário de cadastro para criar novos usuários.
- Após login, você pode criar e visualizar suas tarefas.


David Gomes de Freitas

---

Obrigado por usar o projeto! Qualquer dúvida, entre em contato.
