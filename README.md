# 🚀 Sistema Web CRUD | Django & MySQL

![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

Sistema de gerenciamento de tarefas robusto com autenticação de usuários, seguindo o padrão de projeto **MVT (Model-View-Template)**. O projeto foca em segurança, organização de código e persistência de dados em banco relacional.

## 📌 Funcionalidades

- [x] **Autenticação Segura:** Cadastro e Login de usuários.
- [x] **Privacidade:** Cada usuário visualiza e gerencia apenas suas próprias tarefas.
- [x] **CRUD Completo:** Criação, listagem, edição e exclusão de registros.
- [x] **Interface Responsiva:** Adaptado para dispositivos móveis via Bootstrap 5.

## 🛠️ Tecnologias e Ferramentas

- **Backend:** Python 3.x / Django
- **Banco de Dados:** MySQL
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Segurança:** Variáveis de ambiente com `python-dotenv`

---

## 🔧 Configuração do Ambiente

### 1. Clonar e Preparar Ambiente

```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

# Crie o ambiente virtual
python -m venv venv

# Ative a venv (Windows)
.\venv\Scripts\activate

# Ative a venv (Linux/Mac)
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
2. Banco de Dados (MySQL)
Crie o banco de dados no seu servidor MySQL:

SQL
CREATE DATABASE sistema_web_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
3. Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e preencha com suas credenciais:

Snippet de código
SECRET_KEY=sua_chave_secreta
DEBUG=True

DB_NAME=sistema_web_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
4. Migrações e Execução
Bash
# Sincronize o banco de dados
python manage.py migrate

# Inicie o servidor
python manage.py runserver
Acesse em: http://127.0.0.1:8000
```
