# Jobs Paraná

![Licença](https://img.shields.io/badge/licença-MIT-blue.svg)

## Descrição

Sistema de cadastramento e divulgação de vagas de trabalhos para o estado do Paraná.

## Status

🛠 Em desenvolvimento

## Índice

- [Funcionalidades Externas](#funcionalidades-externa)
- [Funcionalidades Internas](#funcionalidades-interna)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Docker Container](#docker-container)
- [Django Run](#django-run)
- [Uso](#uso)
- [Licença](#licença)

## Funcionalidades Externa

- [x] Login
- [x] Criação de Usuário
- [x] Listagem de Vagas
- [x] Detalhe da Vaga
- [ ] Cadastro de Currículo (Em Desenvolvimento)
- [ ] Atualização de Perfil
- [ ] Listagem de Candidaturas
- [ ] Landing Page


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

4. Execute o comando no terminal de sua escolha:
   ```bash
   docker-compose -p jobsparana up -d
   
## Django Run

1. Adicione uma **SECRET_KEY** nos ``settings.py``:
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
   python manage.py run
   
5. Em seguida execute os seguintes comandos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
6. Crie um super usuário:
   ```bash
   python manage.py createsuperuser

7. Abra a **URL** em seu browser <localost:8000>

## Licença

MIT License

Copyright (c) 2024 Odival Neto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.