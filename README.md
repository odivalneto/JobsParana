# Jobs Paraná

![Licença](https://img.shields.io/badge/licença-MIT-blue.svg)

## Descrição

Sistema de cadastramento e divulgação para vagas de trabalhos do estado do Paraná.

## Status

🛠 Em desenvolvimento

## Índice

- [Funcionalidades Externas](#funcionalidades-externa)
- [Funcionalidades Internas](#funcionalidades-interna)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Docker Container](#docker-container)
- [Django Run](#django-run)

## Funcionalidades Externa

- [x] Login
- [x] Criação de Usuário
- [x] Listagem de Vagas
- [x] Detalhe da Vaga
- [ ] Cadastro de Currículo (Em Desenvolvimento)
- [ ] Atualização de Perfil
- [x] Listagem de Candidaturas
- [ ] Landing Page
- [ ] Api


## Funcionalidades Interna

- [x] Painel Administrativo
- [ ] Login
- [ ] Cadastro de Usuários
- [ ] Cadastro de Vagas
- [ ] Cadastro de Empresas
- [ ] Listagem de Candidaturas

## Tecnologias Utilizadas

- Linguagem: [ Python, JavaScript, CSS, HTML ]
- Frameworks: [ Django, Flowbite, TailwindCSS, Django-Rest ]
- Banco de Dados: [ PostgreSQL ]
- Outras ferramentas: [ Docker, GitHub ]

## Docker Container

Para rodar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/odivalneto/JobsParana
   
2. Instale o Docker Desktop:
   >https://www.docker.com/products/docker-desktop/

3. Renomeie ``.env-config`` para ``.env`` e confirgure as variáveis de ambiente.

4. Execute o seguinte comando em seu terminal:
   ```bash
   docker-compose -p jobsparana up -d
   
## Django Run

1. Adicione uma **SECRET_KEY** em ``settings.py``:
   >https://djecrety.ir

2. Altere a comunicação com o ``Database`` em ``settings.py``:
   ```bash
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
   
4. Execute os seguintes comandos no terminal:
   ```bash 
   pip install -r requirements.txt
   sudo npm install
   npm run tailwind
   python manage.py runserver
   
5. Em seguida execute os seguintes comandos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
6. Crie um super usuário:
   ```bash
   python manage.py createsuperuser

7. Digite a seguinte **URL** em seu browser 
   >localost:8000
   