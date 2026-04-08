#Comandos importantes para uso do docker


**Comandos**

1. Subir o Banco no Docker
    ```bash
    docker compose up -d
    ```

2. Finalizar/Pausar o container Docker
    ```bash
    docker compose stop
    ```

3. Iniciar/Despausar o container Docker
    ```bash
    docker compose start
    ```
4. Derrubar o container Docker
    ```bash
    docker compose down
    ```
5. Resetar o banco apagando todos os containers
    ```bash
    docker compose down -v
    ```
6. Verificar configuração docker
    ```bash
    docker compose config
    ```
7. Logs do container do banco
    ```bash
    docker compose logs -f
    ```
8. Listar todos container ativos
    ```bash
    docker ps
    ```
9. Listar todos container ativos e inativos
    ```bash
    docker ps -a
    ```