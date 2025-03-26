
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados reais do João
df = pd.read_csv("dados.csv")

# Calcular métricas reais
total_gasto = df["gasto"].sum()
total_leads = df["cliques_wpp"].sum()
total_agendamentos = df["agendamentos"].sum()
total_visitas = df["visitas"].sum()
total_propostas = df["propostas"].sum()
total_vendas = df["vendas"].sum()
total_valor_vendas = df["valor_vendas"].sum()
roas_medio = df["roas"].mean()

# Logo e título
st.image("logo-clara.png", width=150)
st.markdown("<h2 style='text-align: center;'>Gestão de Tráfego</h2>", unsafe_allow_html=True)
st.markdown("### Painel de Resultados - João Carvalho")

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Total Gasto", f"R$ {total_gasto:,.2f}")
col2.metric("Leads (Cliques WhatsApp)", f"{int(total_leads)}")
col3.metric("ROAS Médio (Planilha)", f"{roas_medio:.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Agendamentos", f"{int(total_agendamentos)}")
col5.metric("Visitas", f"{int(total_visitas)}")
col6.metric("Propostas", f"{int(total_propostas)}")

col7, col8 = st.columns(2)
col7.metric("Vendas", f"{int(total_vendas)}")
col8.metric("Valor Total Vendido", f"R$ {total_valor_vendas:,.2f}")

# Cálculo de comissão sobre valor de venda
st.markdown("### 💰 Calculadora de Comissão + ROAS")
valor_venda = st.number_input("Digite o valor da venda (R$)", value=1500000.00, step=50000.00, format="%.2f")
comissao_5 = valor_venda * 0.05
comissao_6 = valor_venda * 0.06

# ROAS com base no valor total e no lucro do João
roas_total = valor_venda / total_gasto if total_gasto > 0 else 0
roas_joao_5 = comissao_5 / total_gasto if total_gasto > 0 else 0
roas_joao_6 = comissao_6 / total_gasto if total_gasto > 0 else 0

st.markdown(f"**Venda Total:** R$ {valor_venda:,.2f}")
st.markdown(f"**Comissão João 5%:** R$ {comissao_5:,.2f}")
st.markdown(f"**Comissão João 6%:** R$ {comissao_6:,.2f}")
st.markdown(f"---")
st.metric("📊 ROAS (Venda Total)", f"{roas_total:.2f}")
col_a, col_b = st.columns(2)
col_a.metric("🧠 ROAS João (5%)", f"{roas_joao_5:.2f}")
col_b.metric("🧠 ROAS João (6%)", f"{roas_joao_6:.2f}")

# Gráficos
st.markdown("### 📊 Gasto por Campanha")
fig1 = px.bar(df, x="campanha", y="gasto", title="", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 📈 Valor de Vendas por Campanha")
fig2 = px.bar(df, x="campanha", y="valor_vendas", title="", text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

# Tabela
st.markdown("### 📋 Campanhas detalhadas")
st.dataframe(df)

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
