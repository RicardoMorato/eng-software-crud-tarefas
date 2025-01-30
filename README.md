# CRUD Tarefas

Esse repositório é uma atividade da disciplina de Engenharia de Software do curso de Sistemas de Informação da UFPE.

O intuito foi fazer um CRUD (Create, Read, Update and Delete) simples de tarefas utilizando Django como backend e PostgreSQL como banco de dados.

## Como rodar o projeto

### Pré-requisitos

- `Docker`
- `Docker Compose`
- `Python >= 3.10` (caso queira rodar o backend localmente)

### Rodando com Docker

Para colocar o ambiente de pé, será necessário:

1. Criar um arquivo `.env` a partir do exemplo deixado em `.env.example`. O valor da `DJANGO_SECRET_KEY` pode ser alterado para qualquer hash de sua escolha.
2. Rodar o comando `docker compose up --build` no terminal.

Você verá alguns logs e, em poucos segundos, a mensagem `Listening at: http://0.0.0.0:8000`, como no print abaixo.

![image](https://github.com/user-attachments/assets/380406eb-fad8-483f-a9f7-b4e11cc92e6e)

Pronto, você já pode começar a testar o projeto 🚀

### Rodando localmente

Ao rodar localmente, você será responsável por criar e manter um banco de dados, para tanto, será necessário modificar as informações no arquivo `.env` referentes à comunicação com o banco de dados, utilizando as credenciais do banco de sua escolha.

Após isso, [crie e inicie uma máquina virtual em seu ambiente local](https://docs.python.org/3/library/venv.html) para conseguir instalar as dependências com segurança.

Por fim, rode:
1. `pip install -r requirements.txt` -> Para instalar as dependências
2. `python3 manage.py runserver` -> Para rodar o servidor localmente

Em alguns segundos, você deve ver uma mensagem como no print abaixo:

![image](https://github.com/user-attachments/assets/72c4ee4d-5c68-4f24-880a-8cee14c12619)
