import streamlit as st

# Configurando nome da pagina no sidebar
st.set_page_config(
    page_title = "Teams",
    page_icon = "⚽️",
    layout = "wide"
)

# Carregando tabela da pagina 1
df_data = st.session_state["data"]

# Adicionando lista com os valores da coluna club
clubes = df_data["Club"].unique()
# Adicionando filtro no sidebar com os valores da coluna club
club = st.sidebar.selectbox("Clube", clubes)

# Filtrando valor da coluna club selecionado e valor da coluna name
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

# Adicionando imagem com logo
st.image(df_filtered.iloc[0]["Club Logo"])
# Adicionando titulo com valor da coluna club
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)",
            "Joined", "Height(cm.)", "Weight(lbs.)",
            "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
            column_config={
                "Overall": st.column_config.ProgressColumn(
                    "Overall", format="%d", min_value=0, max_value=100
                ),
                "Wage(£)": st.column_config.ProgressColumn(
                    "Weekly Wage", 
                    format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()
                ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")
            }
)