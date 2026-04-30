import os
from fastapi import APIRouter, HTTPException
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

from .schemas import ChatRequest

router = APIRouter(prefix="/chat", tags=["Assistente de IA"])

DATABASE_URL = os.getenv("DATABASE_URL")
db_langchain = SQLDatabase.from_uri(DATABASE_URL)

llm = ChatOpenAI(model="gpr-3.5-turbo", temperature=0)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=db_langchain,
    verbose=True,
    agent_type="openai-tools"
)

@router.post("/")
def perguntar_ao_banco(requisicao: ChatRequest):
    try:
        resposta = agent_executor.invoke({"input": requisicao.pergunta})

        return {
            "resposta": resposta["output"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a pergunta. ERRO => {str(e)}")