# StudyHub

Sistema Full Stack para gerenciamento de usuários, com autenticação JWT e integração entre FastAPI e React.

## 🧱 Tecnologias

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, Alembic, Docker
- **Frontend**: React, Vite, Axios, Material UI
- **Autenticação**: JWT com contexto global
- **Banco de dados**: PostgreSQL com migrations Alembic

## 🔧 Como rodar o projeto

### Backend
1. Clone o repositório
2. Configure o `.env` com as variáveis `DATABASE_URL`, `SECRET_KEY`, etc.
3. Suba o container do banco:
   ```bash
   docker-compose up -d
