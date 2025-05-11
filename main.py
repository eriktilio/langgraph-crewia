from graph import build_graph

if __name__ == "__main__":
    flow = build_graph()

    # Estado inicial com o tema do artigo
    initial_state = {
        "topic": "O impacto da inteligência artificial na educação"
    }

    # Executa o fluxo completo
    result = flow.invoke(initial_state)

    # Exibe o resultado final do artigo
    print("\n✅ Artigo Final Revisado:\n")
    print(result["final_article"])
    print(flow.get_graph().draw_mermaid())
