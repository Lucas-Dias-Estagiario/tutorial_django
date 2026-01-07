# 🗳️ Django Polls App (Sistema de Enquetes)

Este projeto é uma aplicação web completa de votação (Enquetes), desenvolvida como parte do estudo aprofundado do framework **Django**. 

O objetivo foi ir além do tutorial oficial, implementando estilização personalizada, configurações avançadas de administração e boas práticas de desenvolvimento Back-end.

## 🚀 Funcionalidades

- **Sistema de Votação:** Usuários podem visualizar perguntas e votar em opções pré-definidas.
- **Resultados em Tempo Real:** Visualização gráfica simples e contagem automática de votos.
- **Painel Administrativo Personalizado:**
  - Interface customizada (títulos e brand).
  - Filtros laterais para buscar perguntas por data.
  - Campos de busca textual.
  - Edição de perguntas e respostas na mesma tela (TabularInline).
- **Validação de Dados:** Lógica para impedir votos em perguntas futuras ou antigas.
- **Home Page Personalizada:** Landing page com navegação facilitada.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Django 5.x** (Framework Web MVT)
- **SQLite** (Banco de dados relacional padrão)
- **HTML5 & CSS3** (Estilização e Templates)
- **Django Template Language (DTL)**
- **Testes Automatizados** (`django.test`)

## 🧠 Conceitos Aplicados

Durante o desenvolvimento, foram aplicados os seguintes conceitos da arquitetura MVT (Model-View-Template):

1.  **Models & ORM:** Criação de tabelas e relacionamentos no banco de dados sem uso de SQL puro.
2.  **Views (Genéricas e Baseadas em Função):** Lógica de processamento de requisições.
3.  **URL Routing:** Configuração de rotas dinâmicas e amigáveis (`polls/5/`).
4.  **Admin:** Personalização avançada da interface administrativa do Django.
5.  **Testes Automatizados:** Criação de testes unitários para garantir a integridade das regras de negócio (ex: bug da data futura).
6.  **Arquivos Estáticos:** Gerenciamento de CSS e imagens separadamente da lógica.

## 🔧 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)

2. **Crie e ative um ambiente virtual (Recomendado):**
   ```bash
   python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3. **Instale as depências:**
   ```bash
   pip install django
   # Se houver outros pacotes como django-debug-toolbar ou pandas:
   # pip install -r requirements.txt

4. **Instale as depências:**
   ```bash
   python manage.py migrate


5. **Crie um superusuário (para acessar o Admin):**
   ```bash
   python manage.py createsuperuser

6. **Inicie o servidor:**
   ```bash
   python manage.py runserver

7. **Acesse o navegador**
   ```bash
   Home: http://127.0.0.1:8000/
   Admin: http://127.0.0.1:8000/admin/

---

## 🔮 Próximos Passos (Roadmap)
- [ ] Implementar integração com Pandas para importação de enquetes via Excel.
- [ ] Adicionar login de usuários para restringir votos.
