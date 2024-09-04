import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="🏃",
    layout="wide"
)

# Carregando tabela para a pagina de players
df_data = st.session_state["data"]

# Lista de valores da coluna club
clubes = df_data["Club"].unique()
# Adicionando um filtro com os valores da coluna club
club = st.sidebar.selectbox("Clube", clubes)

# Filtrando na tabela o valor selecionado da coluna club
df_players = df_data[(df_data["Club"] == club)]
# Lista de valores da coluna Name filtrado pelo club
players = df_players["Name"].unique()
# Adicionando filtro com os valores da coluna name
player = st.sidebar.selectbox("Jogador", players)

# Filtrando a linha com o valor da coluna name selecionado
player_stats = df_data[df_data["Name"] == player].iloc[0]
# Selecionando a coluna foto do valor da coluna name filtrado
st.image(player_stats["Photo"])
# Selecionando a coluna name do valor da coluna name filtrado
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posicao:** {player_stats['Position']}")

# Adicionando colunas na aplicacao web
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade:** {player_stats["Age"]}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")

# Adicionando divisor na visualizacao da aplicacao web
st.divider()

# Adicionando descricao
st.subheader(f"Overall {player_stats['Overall']}")
# Adicionando valor da coluna overall
st.progress(int(player_stats["Overall"]))

# Adicionando colunas na visualizacao da aplicacao web
col1, col2, col3, col4 = st.columns(4)

# Adicionando metricas com descricao e valor
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal",
            value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de recisão", value=f"£ {
            player_stats['Release Clause(£)']:,}"
            )

# Adicionando divisor na visualizacao web
st.divider()

# Adicionando colunas na visualizacao web
col1, col2, col3 = st.columns(3)

maximo_valor_mercado = df_data[df_data["Club"] == club]['Value(£)'].sum()
remuneracao_mediana = df_data[df_data["Club"] == club]['Wage(£)'].mean()
clausula_maxima = df_data[df_data["Club"] == club]['Release Clause(£)'].max()

# Alterando formato
maximo_valor_mercado = f"£ {maximo_valor_mercado:,}"
remuneracao_mediana = f"£  {round(remuneracao_mediana, 2):,}"
clausula_maxima = f"£  {clausula_maxima:,}"

col1.metric("Valor de mercado do elenco:", maximo_valor_mercado)
col2.metric("Média de remuneração no clube:", remuneracao_mediana)
col3.metric("Maior clausula do clube:", clausula_maxima)
