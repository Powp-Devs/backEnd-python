import ast

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

from langchain_ollama import ChatOllama
from config import DATABASE_URL


class ERPAssistent:

    def __init__(self):

        self.db = SQLDatabase.from_uri(
            DATABASE_URL,
            include_tables=[
                "pwproduto",
                "pwplanopagamento",
                "pwcobranca",
                "pwempregado",
                "pwtabpr"
            ]
        )


        # usando 3B para seus testes
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0
        )


        self.contexto_negocio = """
            Você é um assistente especialista em ERP.

            REGRAS:
            - Execute consultas reais.
            - Nunca estime resultados.
            - Não use LIMIT para inferir contagens.
            - Use somente resultados reais do banco.
            - Responda em português.
            - Não informe a estrutura das tabelas ou do banco.
            - Sempre execute a consulta SQL antes de responder.
            - Nunca estimar, supor ou inferir quantidades.
            - Nunca responder com base em amostras ou limites.
            - Só responda usando resultados reais retornados do banco.
            - Use a ferramenta sql_db_query para executar consultas.
            - Não use apenas sql_db_query_checker.
        """


        # usa create_sql_agent normal
        self.agent = create_sql_agent(
            llm=self.llm,
            db=self.db,
            verbose=True,
            max_iterations=8,
            handle_parsing_errors=True,
            prefix=self.contexto_negocio
        )


    # ---------------------
    # consultas críticas
    # ---------------------

    def contar_produtos(self):

        resultado = self.db.run(
            "SELECT COUNT(*) FROM pwproduto"
        )

        return ast.literal_eval(resultado)[0][0]


    def contar_planos(self):

        resultado = self.db.run(
            "SELECT COUNT(*) FROM pwplanopagamento"
        )

        return ast.literal_eval(resultado)[0][0]


    def explicar(self, texto):

        resposta = self.llm.invoke(
            f"""
            Responda objetivamente em uma frase:

            {texto}
            """
        )

        return resposta.content


    def perguntar(self, pergunta_usuario):

        pergunta = pergunta_usuario.lower()


        # ROTAS DETERMINÍSTICAS
        if "quantos produto" in pergunta:
            total = self.contar_produtos()

            return self.explicar(
                f"Existem {total} produtos cadastrados."
            )


        if "quantos planos" in pergunta:
            total = self.contar_planos()

            return self.explicar(
                f"Existem {total} planos cadastrados."
            )


        # PERGUNTAS ABERTAS
        resposta = self.agent.invoke(
            {
                "input": pergunta_usuario
            }
        )

        return resposta["output"]