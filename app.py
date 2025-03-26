
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Calcular métricas principais
total_gasto = df["gasto"].sum()
total_vendas_valor = df["valor_vendas"].sum()
total_cliques = df["cliques_wpp"].sum()
total_visitas = df["visitas"].sum()
total_agendamentos = df["agendamentos"].sum()
total_propostas = df["propostas"].sum()
total_vendas_qtd = df["vendas"].sum()
roas_medio = df["roas"].mean()

# Layout
st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - João Carvalho")

col1, col2, col3 = st.columns(3)
col1.metric("Total Gasto", f"R$ {total_gasto:,.2f}")
col2.metric("Valor de Vendas", f"R$ {total_vendas_valor:,.2f}")
col3.metric("ROAS Médio", f"{roas_medio:.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Cliques no WhatsApp", f"{int(total_cliques)}")
col5.metric("Visitas", f"{int(total_visitas)}")
col6.metric("Agendamentos", f"{int(total_agendamentos)}")

col7, col8 = st.columns(2)
col7.metric("Propostas", f"{int(total_propostas)}")
col8.metric("Vendas", f"{int(total_vendas_qtd)}")

# Gráficos
st.markdown("### Gasto por Campanha")
fig_gasto = px.bar(df, x="campanha", y="gasto", title="Gasto por Campanha", text_auto=True)
st.plotly_chart(fig_gasto, use_container_width=True)

st.markdown("### Vendas por Campanha")
fig_vendas = px.bar(df, x="campanha", y="valor_vendas", title="Valor de Vendas por Campanha", text_auto=True)
st.plotly_chart(fig_vendas, use_container_width=True)

# Tabela
st.markdown("### 📋 Campanhas detalhadas")
st.dataframe(df)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
