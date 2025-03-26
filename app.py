
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados reais
df = pd.read_csv("dados.csv")

# Calcular métricas principais
total_gasto = df["gasto"].sum()
total_leads = df["leads"].sum() if "leads" in df.columns else 0
total_cliques = df["cliques_wpp"].sum()
total_visitas = df["visitas"].sum()
total_agendamentos = df["agendamentos"].sum()
total_propostas = df["propostas"].sum()
total_vendas = df["vendas"].sum()
total_valor_vendas = df["valor_vendas"].sum()
roas_medio = df["roas"].mean()

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("<h2 style='text-align: center;'>Gestão de Tráfego</h2>", unsafe_allow_html=True)
st.markdown("### Painel de Resultados - João Carvalho")

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Total Gasto", f"R$ {total_gasto:,.2f}")
col2.metric("Leads (Cliques WhatsApp)", f"{int(total_cliques)}")
col3.metric("ROAS Médio", f"{roas_medio:.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Agendamentos", f"{int(total_agendamentos)}")
col5.metric("Propostas", f"{int(total_propostas)}")
col6.metric("Vendas", f"{int(total_vendas)}")

st.metric("Valor Total de Vendas", f"R$ {total_valor_vendas:,.2f}")

# Cálculo de comissão sobre venda
st.markdown("### 💰 Calculadora de Comissão")
valor_venda = st.number_input("Digite o valor da venda (R$)", value=1500000.00, step=50000.00, format="%.2f")
comissao_5 = valor_venda * 0.05
comissao_6 = valor_venda * 0.06
st.write(f"Se João receber **5%**, ele ganha: R$ {comissao_5:,.2f}")
st.write(f"Se João receber **6%**, ele ganha: R$ {comissao_6:,.2f}")

# Gráficos
st.markdown("### 📊 Gasto por Campanha")
fig1 = px.bar(df, x="campanha", y="gasto", title="", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 📈 Vendas por Campanha")
fig2 = px.bar(df, x="campanha", y="valor_vendas", title="", text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

# Tabela completa
st.markdown("### 📋 Campanhas detalhadas")
st.dataframe(df)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
