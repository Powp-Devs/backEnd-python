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
                "pwtabpr",
                "pwsetor"
            ]
        )

        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0
        )


        self.contexto_negocio = """
            Você é um assistente de banco de dados do ERP POWP.
            Responda sempre em português. Gere apenas queries SQL válidas para PostgreSQL.
            
            REGRAS DE NEGÓCIO DO SISTEMA:
            1. Produtos (pwproduto):
               - Um produto "ativo" significa que a coluna 'status' = 'A'.
               - Um produto "inativo" ou "bloqueado" significa 'status' = 'I'.
            2. Preços (pwtabpr):
               - O preço de venda de um produto está na tabela 'pwtabpr' na coluna 'preco_venda'.
               - Para saber o preço de um produto, você deve fazer um JOIN entre pwproduto (codproduto) e pwtabpr (codproduto).
            3. Empregados (pwempregado):
               - O 'bloqueio' = 'S' significa que o funcionário está bloqueado/demitido. 'N' significa ativo.
               
            REGRAS DE COMPORTAMENTO:
            - Nunca estime resultados. Use apenas dados reais.
            - Nunca use LIMIT 5 a menos que o usuário peça "os 5 melhores".
            - Nunca retorne uma query SQL sempre o valor solicitado.
            - Nunca retorne uma query sql e sim somente o resultado.
        """

        self.agent = create_sql_agent(
            llm=self.llm,
            db=self.db,
            verbose=True,
            max_iterations=8,
            handle_parsing_errors=True,
            prefix=self.contexto_negocio
        )



    # consultas exemplo - retirar depois ou não

    def contar_produtos(self):
        resultado = self.db.run("SELECT COUNT(*) FROM pwproduto")
        return ast.literal_eval(resultado)[0][0]

    def contar_planos(self):
        resultado = self.db.run("SELECT COUNT(*) FROM pwplanopagamento")
        return ast.literal_eval(resultado)[0][0]


    def perguntar(self, pergunta_usuario):
        pergunta = pergunta_usuario.lower()

        if "quantos produtos" in pergunta or "total de produtos" in pergunta:
            total = self.contar_produtos()
            return f"Existem {total} produtos cadastrados no sistema."

        if "quantos planos" in pergunta or "total de planos" in pergunta:
            total = self.contar_planos()
            return f"Existem {total} planos de pagamento cadastrados."

        try:
            resposta = self.agent.invoke({"input": pergunta_usuario})
            return resposta["output"]
        except Exception as e:
            return "Desculpe, a IA teve dificuldade em montar a consulta para essa pergunta específica. Tente perguntar de outra forma."