from langchain_community.utilities import SQLDatabase
from langchain_community.chat_models import ChatOllama
from langchain_community.agent_toolkits import create_sql_agent

from config import DATABASE_URL

class ERPAssistent:

    def __init__(self):
        self.db = SQLDatabase.from_uri(
            DATABASE_URL,
            include_tables=[
                'pwproduto',
                'pwplanopagamento',
                'pwcobranca',
                'pwempregado'
            ]
        )

        self.llm = ChatOllama(
            model="qwen2.5:3b", 
            temperature=0
        )

        self.contexto_negocio = """
            Você é um assistente especialista no ERP.

            Mapeamento de tabelas:

            pwproduto:
            Cadastro de produtos

            pwestoque:
            Controle de estoque

            pwplanopagamento:
            Planos de pagamento

            pwcobranca:
            Cobranças

            Regras:
            - Se usuário falar "produtos", considere pwproduto
            - Se falar "estoque", consulte pwestoque
            - Gere SQL PostgreSQL válido
            - Nunca invente dados
            - Sempre consultar banco antes de responder
            - Responda em português
            - Sempre execute a consulta SQL antes de responder.
            - Nunca estimar, supor ou inferir quantidades.
            - Nunca responder com base em amostras ou limites.
            - Só responda usando resultados reais retornados do banco.
            - Use a ferramenta sql_db_query para executar consultas.
            - Não use apenas sql_db_query_checker.
        """

        self.agent = create_sql_agent(
            llm=self.llm,
            db=self.db,
            verbose=False,
            max_iterations=5
        )

    def perguntar(self, pergunta_usuario):
        prompt = f"""
            {self.contexto_negocio}

            Pergunta:
            {pergunta_usuario}
        """

        resposta = self.agent.invoke(
            {
                "input": prompt
            }
        )

        return resposta["output"]