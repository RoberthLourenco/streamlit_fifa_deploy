from pathlib import Path
from datetime import datetime

import streamlit as st
import webbrowser as wb
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)


pasta_datasets = Path(__file__).parent.parent / "dataset_fifa" / "datasets"

df_data = pd.read_csv(
    pasta_datasets / "CLEAN_FIFA23_official_data.csv", index_col=0)

# Criando um session state para salvar cache do usuario
if "data" not in st.session_state:
    # Filtrando valores de ano maior ou igual ao ano atual
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    # Filtrando valores na coluna valor
    df_data = df_data[df_data["Value(£)"] > 0]
    # Ordenando tabela pela coluna overall
    df_data = df_data.sort_values(by="Overall", ascending=False)

    # Adicionando tabela em um cache de usuario
    st.session_state["data"] = df_data


# Adicionando titulo na visualizacao da pagina 1
st.markdown("# FIFA23 OFFICIAL DATASET!")

# Adicionando texto no sidebar da visualizacao web
st.sidebar.markdown("Desenvolvido por [Roberth Lourenço]")

# Adicionando botao para direcionar direto para o kaggle
btn = st.button("Acesso os dados no Kaggle")
if btn:
    wb.open_new_tab(
        "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados de jogadores de **futebol de 2017 a 2023** fornece 
    informações abrangentes sobre jogadores de futebol profissionais. 
    O conjunto de dados contém uma ampla gama de atributos, incluindo 
    dados demográficos dos jogadores, características físicas, estatísticas de jogo, 
    detalhes de contratos e afiliações de clubes. Com mais de 17.000 registros, 
    este conjunto de dados oferece um recurso valioso para analistas de futebol, 
    pesquisadores e entusiastas interessados ​​em explorar vários aspectos do mundo do futebol, 
    pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, 
    análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.

    """
)
