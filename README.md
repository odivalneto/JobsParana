# Jobs Paraná

![Licença](https://img.shields.io/badge/licença-MIT-blue.svg)

## Descrição

Este repositório contém o código fonte de um projeto web desenvolvido com o framework Django, criado para alunos que desejam aprender programação e desenvolvimento web, mas não têm condições financeiras de pagar por cursos tradicionais. O projeto faz parte de uma iniciativa educacional voluntária, sem vínculo com entidades governamentais ou privadas, e é disponibilizado de forma totalmente gratuita para todos os interessados.

O objetivo é proporcionar um aprendizado acessível e de qualidade sobre o desenvolvimento de aplicações web usando Django, abordando conceitos fundamentais que formarão a base para a criação de projetos profissionais.

Neste projeto, os alunos terão a oportunidade de:

- Aprender Django do zero, sem custos, com um material prático e completo.
- Criar e gerenciar bancos de dados usando o Django ORM, desenvolvendo a lógica de backend.
- Implementar autenticação e permissões de usuários para criar sistemas seguros.
- Desenvolver páginas dinâmicas, trabalhando com templates e formulários.
- Criar APIs RESTful (se aplicável), com o uso do Django Rest Framework.
- Entender as boas práticas de organização e estruturação de projetos Django.

## Status

🛠 Em desenvolvimento

## Índice

- [Funcionalidades Externas](#funcionalidades-externa)
- [Funcionalidades Internas](#funcionalidades-interna)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Docker Container](#docker-container)
- [Django Server](#django-run)

## Funcionalidades Externa

- [x] Login
- [x] Criação de Usuário
- [x] Listagem de Vagas
- [x] Detalhe da Vaga
- [x] Cadastro de Currículo
- [x] Atualização de Perfil
- [x] Listagem de Candidaturas
- [ ] Landing Page (Em Desenvolvimento)
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
   
## Django Server

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
   
