import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import SQLDatabase
from langchain_community.chat_models import ChatOllama
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import PromptTemplate

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+pg8000://{db_user}:{db_password}@localhost:5433/{db_name}"


db = SQLDatabase.from_uri(
    DATABASE_URL, 
    include_tables=['pwplanopagamento', 'pwcobranca']
)

llm = ChatOllama(model="mistral", temperature=0)

def total_produtos():
    return db.run("SELECT COUNT(*) FROM pwplanopagamento")

print("Analisando o banco de dados...")

resultado = total_produtos()

prompt = f"""
O sistema retornou que existem {resultado} plano de pagamento cadastrado(s).
Explique isso de forma clara e amigável para o usuário.
"""

response = llm.invoke(prompt)

print("Resposta:")
print(response.content)