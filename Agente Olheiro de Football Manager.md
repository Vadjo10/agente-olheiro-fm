# Agente Olheiro de Football Manager

## Visão Geral do Projeto

Este projeto implementa um agente de Inteligência Artificial (IA) para atuar como um "olheiro" virtual no jogo Football Manager. Utilizando uma base de dados de jogadores em formato CSV, o agente é capaz de responder a perguntas complexas em linguagem natural, como "Encontre jogadores gratuitos" ou "Sugira laterais com menos de 23 anos e alto potencial", fornecendo recomendações de contratação baseadas nos dados do jogo.

O objetivo principal é demonstrar a aplicação prática de Large Language Models (LLMs) e frameworks de agentes para interagir com dados estruturados, transformando consultas em linguagem natural em análises de dados acionáveis. O projeto foi desenvolvido com foco em baixo custo de operação, utilizando o modelo `gpt-3.5-turbo` da OpenAI.

## Arquitetura do Sistema

A arquitetura do Agente Olheiro de Football Manager é modular e baseada na integração de bibliotecas Python para processamento de dados e interação com modelos de linguagem. Abaixo, um diagrama visual que ilustra o fluxo de dados e a interação entre os componentes:

![Diagrama de Arquitetura](https://private-us-east-1.manuscdn.com/sessionFile/dXFOBbUSnCxHrxD5jFkpRK/sandbox/QeCyOUwrJvhFf2UAhpqRXc-images_1752668215118_na1fn_L2hvbWUvdWJ1bnR1L2FyY2hpdGVjdHVyZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZFhGT0JiVVNuQ3hIcnhENWpGa3BSSy9zYW5kYm94L1FlQ3lPVXdySnZoRmYyVUFocHFSWGMtaW1hZ2VzXzE3NTI2NjgyMTUxMThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyRnlZMmhwZEdWamRIVnlaUS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=oxFOc66PXJZ5GUm4F0W14Cvyu8sxEYN0Y4wL~Gcbmqmf5qAl8fCMLdVb0yLpPmpn-2vVM~snIFRW5mkBO-uDNbRRu4VmzfDRIfQzjBL5~xtAtTwdmMX7k6NPeA35LZkRwsqpLaxxFfNIxO1WhWZsmPP2NEVoOim533MAroDuuRlAYFtHnJE-zPRXAwxousREGF0hN2Iq0IRgOEp8NdCfAlLhxr3-vxcRBmYJZc3kFD8ikWXgeu6B9OrR~ASXLhPOODDv4apBE3-YhKLyWKTa5MllB98zmIljT2GVRy9r7G0JQ7G6MKDJrjNAfppxuKbKl79ODo7JcbgtSYN9Q8eEdg__)

### Componentes Principais:

1.  **Base de Dados (`FM2023.csv`):** Contém todas as informações dos jogadores do Football Manager, incluindo nome, idade, posição, valor de mercado, capacidade atual (CA), capacidade potencial (PA), salário e diversos atributos. É a fonte de dados para as análises do agente.

2.  **Pandas DataFrame:** A biblioteca `pandas` é utilizada para carregar o `FM2023.csv` em memória como um DataFrame. Isso permite uma manipulação e consulta eficiente dos dados em Python.

3.  **Agente Olheiro de FM (Lógica Central):** Este é o coração do sistema, orquestrando a interação entre o usuário, o modelo de linguagem e o DataFrame. Ele interpreta as perguntas do usuário, as traduz em operações de dados e formata as respostas.

4.  **LangChain (`create_pandas_dataframe_agent`):** É o framework principal utilizado para construir o agente. Especificamente, o `create_pandas_dataframe_agent` é uma ferramenta poderosa que permite que um LLM interaja com um DataFrame do Pandas. Ele abstrai a complexidade de gerar e executar código Python para consultar e manipular os dados, permitindo que o LLM "pense" em termos de operações de dados.

5.  **LangChain (`ChatOpenAI`):** Atua como a interface entre o framework LangChain e a API da OpenAI. Ele permite que o agente utilize os modelos de linguagem da OpenAI para processar as perguntas do usuário e gerar o código Pandas necessário.

6.  **OpenAI API (`gpt-3.5-turbo`):** É o Large Language Model (LLM) utilizado pelo agente. O `gpt-3.5-turbo` é responsável por:
    *   Compreender a pergunta do usuário em linguagem natural.
    *   Gerar o código Python (Pandas) apropriado para consultar o DataFrame e obter a informação solicitada.
    *   Interpretar os resultados do código Pandas e formatar a resposta final para o usuário.
    *   O `gpt-3.5-turbo` foi escolhido por seu bom equilíbrio entre capacidade e custo-benefício, sendo ideal para demonstrações.

### Fluxo de Operação:

1.  O usuário faz uma pergunta em linguagem natural ao Agente Olheiro.
2.  A pergunta é enviada ao LLM (`gpt-3.5-turbo`) através do `ChatOpenAI` e do `create_pandas_dataframe_agent`.
3.  O LLM, com base em seu treinamento e no prompt fornecido, "pensa" em como responder à pergunta e gera um trecho de código Pandas para manipular o DataFrame.
4.  O `create_pandas_dataframe_agent` executa esse código Pandas no DataFrame carregado.
5.  O resultado da execução do código é retornado ao LLM.
6.  O LLM interpreta o resultado e formula uma resposta clara e concisa em linguagem natural para o usuário, incluindo uma tabela com os jogadores encontrados, se aplicável.

## Tecnologias Utilizadas

*   **Python 3.x:** Linguagem de programação principal.
*   **Pandas:** Biblioteca para manipulação e análise de dados (DataFrames).
*   **LangChain:** Framework para desenvolvimento de aplicações com LLMs e agentes.
*   **OpenAI API:** Serviço de Inteligência Artificial que fornece o modelo `gpt-3.5-turbo`.

## Configuração e Execução

Para configurar e executar o Agente Olheiro de Football Manager no seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x instalado.
*   Uma chave de API válida da OpenAI. Você pode obtê-la em [platform.openai.com](https://platform.openai.com/).

### Passos

1.  **Baixe os arquivos do projeto:**
    *   Salve o código Python fornecido (`agente_olheiro_fm.py`) em um arquivo no seu computador.
    *   Coloque o arquivo `FM2023.csv` (sua base de dados do Football Manager) na **mesma pasta** do script Python.

2.  **Instale as dependências:**
    Abra seu terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas Python necessárias:
    ```bash
    pip install pandas openai langchain langchain-experimental
    ```

3.  **Configure sua Chave de API da OpenAI:**
    O script precisa da sua chave de API da OpenAI para se comunicar com o modelo `gpt-3.5-turbo`. A forma mais segura e recomendada é configurá-la como uma variável de ambiente. No seu terminal, execute:

    *   **Linux/macOS:**
        ```bash
        export OPENAI_API_KEY="sua_chave_da_openai_aqui"
        ```
    *   **Windows (Prompt de Comando):**
        ```cmd
        set OPENAI_API_KEY="sua_chave_da_openai_aqui"
        ```
    *   **Substitua** `"sua_chave_da_openai_aqui"` pela sua chave de API real da OpenAI. **Nunca compartilhe sua chave de API publicamente ou a inclua diretamente no código que será versionado.**

    Alternativamente, você pode passar a chave diretamente na função `ChatOpenAI` no script, mas **não é recomendado para produção ou versionamento**:
    ```python
    llm = ChatOpenAI(temperature=0, model=model_name, api_key="sua_chave_da_openai_aqui")
    ```

4.  **Execute o Agente:**
    No terminal, navegue até a pasta onde você salvou o script e o CSV, e execute:
    ```bash
    python agente_olheiro_fm.py
    ```

## Como Interagir com o Agente

Após executar o script, o agente carregará a base de dados e estará pronto para receber suas perguntas. O script já vem com alguns exemplos de consultas pré-definidas. Você pode:

*   **Usar as perguntas de exemplo:** O script já chama a função `consultar_olheiro` com várias perguntas. Observe as saídas no terminal.
*   **Adicionar suas próprias perguntas:** Edite o arquivo `agente_olheiro_fm.py` e adicione mais chamadas à função `consultar_olheiro` com suas próprias perguntas. Por exemplo:
    ```python
    consultar_olheiro(
        agente_olheiro, 
        "Quais são os 10 melhores goleiros (posição 'GK') com menos de 25 anos e salário abaixo de 50000 euros?"
    )
    ```

### Dicas para Fazer Perguntas:

*   **Seja claro e específico:** Quanto mais clara for sua pergunta, melhor o agente poderá traduzi-la em código Pandas.
*   **Mencione as colunas:** Use os nomes das colunas da base de dados (`Name`, `Age`, `Position`, `Values`, `ca`, `pa`, `Salary`, `Finishing`, `Pace`, etc.) para guiar o agente.
*   **Combine critérios:** O agente é capaz de combinar múltiplos critérios de filtro e ordenação.
*   **Peça o formato desejado:** Você pode pedir para listar os "5 melhores resultados em uma tabela com as colunas X, Y, Z".

## Limitações Conhecidas

*   **Complexidade do Raciocínio:** Embora o `gpt-3.5-turbo` seja econômico, ele pode ter dificuldades com perguntas que exigem raciocínio multi-etapas muito complexo ou inferência profunda, podendo ocasionalmente entrar em loops de raciocínio ou fornecer respostas incompletas. Modelos mais avançados (como `gpt-4`) são mais robustos para esses cenários.
*   **Interpretação de Posições:** A coluna `Position` no CSV contém muitas variações (ex: `M C`, `DM C`, `DM/M/AM C`). O agente tenta usar `str.contains()` para lidar com isso, mas perguntas muito específicas sobre posições podem exigir um ajuste no prompt ou na lógica do agente.
*   **Dados Ausentes/Inconsistentes:** A qualidade das respostas depende diretamente da qualidade e completude dos dados no `FM2023.csv`. Valores ausentes ou inconsistentes podem afetar a precisão das análises.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido por Manus AI**


