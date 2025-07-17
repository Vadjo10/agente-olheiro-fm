import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType # Adicionado
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# --- CONFIGURAÇÃO INICIAL ---

def carregar_dados(caminho_csv):
    """Carrega os dados do CSV para um DataFrame do Pandas."""
    try:
        # Tenta carregar com codificação padrão, se falhar, tenta outras comuns
        return pd.read_csv(caminho_csv)
    except UnicodeDecodeError:
        print("Falha na codificação padrão (utf-8), tentando \'latin1\'...")
        return pd.read_csv(caminho_csv, encoding="latin1")
    except FileNotFoundError:
        print(f"Erro: Arquivo \'{caminho_csv}\' não encontrado. Verifique o nome e o caminho do arquivo.")
        return None

def criar_agente_olheiro(df):
    """Cria e retorna um agente configurado para analisar o DataFrame de jogadores."""
    if df is None:
        return None
        
    # Inicializa o LLM da OpenAI com o modelo mais econômico e compatível
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-nano")

    # Cria o agente específico para Pandas DataFrames
    # verbose=True nos mostra o "pensamento" do agente
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        # handle_parsing_errors=True, # Este parâmetro foi descontinuado em versões mais recentes do LangChain
        allow_dangerous_code=True # Permite a execução de código Python gerado pelo agente
    )
    return agent

def consultar_olheiro(agent, pergunta):
    """Envia uma consulta para o agente e imprime a resposta."""
    if agent is None:
        print("Agente não foi inicializado devido a um erro ao carregar os dados.")
        return

    print(f"\n>>> VOCÊ PERGUNTOU: {pergunta}")
    
    # O prompt é a instrução que damos ao agente.
    # É importante dar contexto sobre as colunas, especialmente as mais complexas.
    prompt_template = f"""
    Você é um olheiro de futebol experiente. Sua tarefa é analisar a base de dados de jogadores e fornecer recomendações.
    
    Aqui está o significado de algumas colunas importantes:
    - \'Name\': Nome do jogador.
    - \'Age\': Idade do jogador.
    - \'Position\': Posição principal do jogador. (Ex: \'S\' para atacante, \'GK\' para goleiro, \'D C\' para zagueiro central, \'M C\' para meio-campo central, \'DR\' para lateral direito, \'DL\' para lateral esquerdo)
    - \'Values\': Valor de mercado do jogador em euros.
    - \'ca\': Habilidade atual do jogador (de 0 a 200).
    - \'pa\': Potencial máximo de habilidade que o jogador pode atingir (de 0 a 200).
    - \'Salary\': Salário do jogador.
    - Outras colunas são atributos de 1 a 20 (ex: \'Finishing\', \'Passing\', \'Pace\', \'Strength\').

    Com base nisso, responda à seguinte pergunta:
    Pergunta: {pergunta}

    Forneça uma resposta clara e, se encontrar jogadores, liste os 5 melhores resultados em uma tabela com as colunas mais relevantes (Name, Age, Position, Values, ca, pa, Salary). Se a coluna \'Salary\' tiver valores ausentes, ignore-os ou trate-os como 0 para fins de comparação se necessário.
    """
    
    try:
        resposta = agent.invoke({"input": prompt_template})
        print("\n<<< RESPOSTA DO OLHEIRO:")
        print(resposta["output"])
    except Exception as e:
        print(f"Ocorreu um erro durante a consulta: {e}")


# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    # 1. Carregar os dados
    # Certifique-se de que o nome do arquivo CSV está correto!
    caminho_do_arquivo_csv = "/home/ubuntu/upload/FM2023.csv" 
    dataframe_jogadores = carregar_dados(caminho_do_arquivo_csv)

    # 2. Criar o agente
    agente_olheiro = criar_agente_olheiro(dataframe_jogadores)

    # 3. Fazer consultas ao nosso olheiro virtual!
    if agente_olheiro:
        print("\nAgente Olheiro de FM pronto! Faça suas perguntas.\n")
        
        # Exemplos de consultas:
        consultar_olheiro(
            agente_olheiro, 
            "Quais são os 5 jogadores mais caros na base de dados?"
        )
        
        consultar_olheiro(
            agente_olheiro, 
            "Estou procurando um lateral-direito (posição \'DR\') com menos de 23 anos e com capacidade potencial (pa) acima de 150. Quem você recomenda?"
        )
        
        consultar_olheiro(
            agente_olheiro, 
            "Preciso de um atacante (posição \'S\') de graça. Encontre jogadores com valor de mercado (Values) igual a zero."
        )

        consultar_olheiro(
            agente_olheiro, 
            "Tenho um orçamento de 2000000. Mostre-me os melhores meio-campistas (posição \'MC\') que posso comprar com esse dinheiro, ordenados pela maior capacidade atual (ca)."
        )
        
        consultar_olheiro(
            agente_olheiro,
            "Encontre \'jóias escondidas\': jogadores com menos de 20 anos, capacidade atual (ca) abaixo de 120, mas com capacidade potencial (pa) acima de 160."
        )


