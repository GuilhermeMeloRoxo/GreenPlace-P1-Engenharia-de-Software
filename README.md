# GreenPlace
Projeto do primeiro período do curso de Engenharia de Software - IFPB Campus João Pessoa

## Descrição
O GreenPlace é um espaço criado para ajudar pessoas a entenderem o impacto de suas escolhas no meio ambiente. A partir de um formulário simples e intuitivo, o usuário responde perguntas sobre seus hábitos do dia a dia e, ao final, recebe uma pontuação que representa o nível de carbono que emite. acompanhada de uma classificação visual clara e fácil de interpretar. 

Além disso, a plataforma também oferece um ambiente voltado para empresas e instituições interessadas em dados ambientais. Esses perfis podem acessar informações consolidadas dos usuários, visualizar resultados em tabelas e gerar relatórios em PDF, contribuindo para análises, pesquisas e estudos relacionados à emissão de carbono e à sustentabilidade.

## Funcionalidades
- Navegação Intuitiva
- Layout Resposivo
- Formulários

## Tecnologias Utilizadas
- Frontend: HTML, CSS e JavaScript
- Backend: Python
- Armazenamento: CSV

## Como Executar

### Pré-requisitos
- Python
- Outras dependências específicas

### Instalação
1. Clone o repositório
   git clone https://github.com/GuilhermeMeloRoxo/GreenPlace-P1-Engenharia-de-Software.git
2. Criar e ativar um ambiente virtual (opcional)
   - Criar: python3 venv venv (python venv venv)
   - Ativar (Linux/macOS): source venv/bin/activate
   - Ativar (Windows): .\venv\Scripts\Activate
4. Instale as dependências
   pip install -r requirements.txt
5. Execute o projeto
   python main.py

## Estrutura do Projeto

    GreenPlace/
      ├── app/              # Pacotes e rotas
          ├── empresas/
              ° __init__.py
              ° routes.py
          └── usuario_comum/
              ° __init__.py
              ° routes.py
          ° __init__.py
      ├── data/             # Armazenamento
      ├── docs/             # Documentos do projeto
          ° Arquitetura.drawio.pdf
          ° emissao-carbono.md
      ├── static/           # Estilos e interação
          ├── css/
              ° style.css
          ├── imagens/
              ° logo.png
          └── js/
              ° script.js
      └── templates/       # Páginas da aplicação
          ° base.html
          ° cadastro.html
          ° empresas.html
          ° index.html
          ° login.html
          ° questionario.html
          ° resultado.html
      ° .gitignore
      ° README.md
      ° main.py
      ° requirements.txt
      
## Autores
- **Gabriel Neres** - Desenvolvimento Full Stack - [@GabrielNeres](https://github.com/GabrielNeres44)
- **Guilherme Mélo** - Desenvolvimento Full Stack - [@GuilhermeMelo](https://github.com/GuilhermeMeloRoxo)
- **Maria Clara Fernandes** - Desenvolvimento Full Stack - [@MariaClara](https://github.com/mariaclara-fs)
- **Yasmin Marinho** - Desenvolvimento Full Stack - [@YasminMarinho](https://github.com/Yasmin-Marinho1)
