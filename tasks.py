from crewai import Task, Crew
from agents import researcher, writer, reviewer

def research_task(input: str):
    task = Task(
        description=f"Realize uma pesquisa aprofundada sobre: {input}",
        expected_output="Um resumo com as informações mais relevantes sobre o tema.",
        agent=researcher
    )
    crew = Crew(agents=[researcher], tasks=[task], verbose=True)
    return crew.kickoff()

def writing_task(input: str):
    task = Task(
        description=f"Com base na pesquisa abaixo, escreva um artigo claro e bem estruturado:\n\n{input}",
        expected_output="Um artigo bem escrito e informativo sobre o tema.",
        agent=writer
    )
    crew = Crew(agents=[writer], tasks=[task], verbose=True)
    return crew.kickoff()

def review_task(input: str):
    task = Task(
        description=f"Revise o seguinte artigo, corrija erros e melhore a clareza:\n\n{input}",
        expected_output="Um artigo revisado e corrigido, pronto para publicação.",
        agent=reviewer
    )
    crew = Crew(agents=[reviewer], tasks=[task], verbose=True)
    return crew.kickoff()
