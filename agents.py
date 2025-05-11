import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Agente Pesquisador
researcher = Agent(
    role="Pesquisador",
    goal="Pesquisar informações relevantes sobre o tema proposto",
    backstory="Você é um especialista em reunir dados úteis de fontes confiáveis.",
    llm=llm,
    verbose=True
)

# Agente Redator
writer = Agent(
    role="Redator",
    goal="Escrever um artigo claro e informativo baseado na pesquisa",
    backstory="Você é um redator com foco em transformar ideias em conteúdo acessível e atrativo.",
    llm=llm,
    verbose=True
)

# Agente Revisor
reviewer = Agent(
    role="Revisor",
    goal="Melhorar o texto final com correções gramaticais e clareza de ideias",
    backstory="Você é um editor detalhista com experiência em revisar conteúdos complexos.",
    llm=llm,
    verbose=True
)
