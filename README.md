#BackEnd em Python


##Instalação 

**Requerimentos**

- Python 3.10 +
- Pip
- Banco de Dados PostegreSQL local

**Passo a passo**

1. Clonar o repositório:
    ```bash
    git clone https://github.com/Powp-Devs/backEnd-python.git
    ```

2. instalar todas as bibliotecas
    ```bash
    pip install -r requirements.txt
    ```

3. Crie o ambiente virtual
    ```bash
    python -m venv venv
    ```

4. Ative o ambiente
    ```bash
    venv\Scripts\activate
    ```

5. Instalar o SqlAlchemy
    ```
    pip install sqlalchemy
    ```
6. Instalar o Pydantic
    ```
    pip install pydantic[email]
    ```

7. Instalar o PG8000
    ```
    pip install pg8000
    ```

8. Instalar o LangChain para conexão com a IA
    ```bash
    pip install langchain langchain-community langchain-openai
    ```

9. Instale o framework e o servidor
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

10. Criar as máquinas virtuas do PostegreSQL no docker
    ```bash
    docker compose up -d
    ```

11. Iniciar o servidor
    ```bash
    uvicorn app.main:app --reload
    ```

12. Acessar documentação API
    ```
    http://127.0.0.1:8000/docs
    ```

13. Instalar o Pytest
    ```bash
    pip install pytest
    ```