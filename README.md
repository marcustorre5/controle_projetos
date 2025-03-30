# Sistema de Controle de Entrada de Projetos

Este projeto é um **sistema de controle de entrada de projetos** desenvolvido para a área de **Engenharia Civil**, utilizando o framework **Django** com **Python**. O sistema foi projetado para organizar e gerenciar os projetos de engenharia, facilitando o **cadastro de projetos**, o **controle de status** e o **histórico de alterações**.

## Funcionalidades

- **Cadastro de Projetos**: Registre e armazene informações detalhadas sobre os projetos de engenharia civil.
- **Controle de Status**: Acompanhe o status dos projetos, como "Em andamento", "Em revisão", "Aprovado", etc.
- **Histórico de Alterações**: Registre todas as alterações feitas nos projetos, com detalhes de quem fez a alteração e o que foi modificado.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Django**: Framework para desenvolvimento web.
- **HTML**: Linguagem de marcação para estruturação das páginas web.
- **CSS**: Estilização das páginas e interfaces.
- **JavaScript**: Usado para interatividade e dinamismo no front-end.
- **PostgreSQL**: Banco de dados utilizado para armazenar as informações do sistema.

## Como Rodar o Projeto

### Requisitos

Antes de rodar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- **Python** 3.x ou superior.
- **Django**.
- **PostgreSQL** (configurado corretamente para o projeto).

### Passos para Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/controle-entrada-projetos.git
   cd controle-entrada-projetos
   ```

2. **Crie um ambiente virtual**:

   Crie e ative um ambiente virtual para gerenciar as dependências do projeto:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências**:

   Instale as dependências necessárias para o projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração do Banco de Dados PostgreSQL**:

   No arquivo `settings.py`, configure a conexão com o banco de dados PostgreSQL. Exemplo de configuração:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nome_do_banco',
           'USER': 'usuario',
           'PASSWORD': 'senha',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

   Certifique-se de que o banco de dados esteja criado no PostgreSQL antes de continuar.

5. **Execute as migrações do banco de dados**:

   Execute as migrações para configurar o banco de dados:

   ```bash
   python manage.py migrate
   ```

6. **Criação do Superusuário**:

   Crie um superusuário para acessar o painel administrativo do Django:

   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor de desenvolvimento**:

   Execute o servidor de desenvolvimento do Django:

   ```bash
   python manage.py runserver
   ```

8. **Acesse a aplicação**:

   Abra o navegador e acesse a aplicação em [http://127.0.0.1:8000](http://127.0.0.1:8000).

   - Para acessar o painel administrativo, acesse [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) e faça login com as credenciais do superusuário.

## Estrutura do Projeto

A estrutura básica do projeto é a seguinte:

```
controle-entrada-projetos/
├── controle_projetos/          # Diretório do aplicativo principal
│   ├── migrations/             # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py               # Configuração do painel administrativo
│   ├── apps.py
│   ├── models.py              # Modelos de dados (Projetos, Status, etc)
│   ├── views.py               # Lógica da aplicação
│   ├── urls.py                # URLs do aplicativo
│   └── templates/             # Templates HTML
├── manage.py                  # Comando de administração do Django
├── requirements.txt           # Arquivo de dependências do Python

```

**Desenvolvido por: Marcus Torres**
