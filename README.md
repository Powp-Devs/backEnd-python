#BackEnd em Python


##Instalação 

**Requerimentos**

- Python 3.10 +
- Pip
- Banco de Dados PostegreSQL local
1. instalar todas as bibliotecas
    ```bash
    pip install -r requirements.txt
    ```

**Passo a passo**

1. Clonar o repositório:
    ```bash
    git clone
    ```

2. Crie o ambiente virtual
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente
    ```bash
    venv\Scripts\activate
    ```

4. Instale o framework e o servidor
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

5. Iniciar o servidor
    ```bash
    uvicorn app.main:app --reload
    ```