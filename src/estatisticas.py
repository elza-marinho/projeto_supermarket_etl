import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/supermarket_tratada.csv")

# Qual filial apresentou o maior faturamento?
faturamento_por_filial = df.groupby("filial")['vendas'].sum().sort_values(ascending=False).round(2)

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(faturamento_por_filial.index, faturamento_por_filial.values)
ax.bar_label(barras, fmt="%.0f", padding=3)

ax.set_title("Faturamento por filial")
ax.set_xlabel("Filial")
ax.set_ylabel("Faturamento")
fig.tight_layout()

os.makedirs("charts", exist_ok=True)
fig.savefig("charts/faturamento_filial.png")
plt.show()

# Qual filial realizou a maior quantidade de vendas?
vendas_por_filial = df.groupby("filial")["id_venda"].count().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(vendas_por_filial.index, vendas_por_filial.values, color="#0C1251")
ax.bar_label(barras, padding=3)

ax.set_title("Número de vendas por filial")
ax.set_xlabel("Filial")
ax.set_ylabel("Número de vendas")
ax.set_ylim(0, vendas_por_filial.max() * 1.15)
fig.tight_layout()

os.makedirs("charts", exist_ok=True)
fig.savefig("charts/vendas_filial.png")
plt.show()


#Qual linha de produto apresentou o maior faturamento?
faturamento_por_linha = (
    df.groupby("linha_produto")["vendas"].sum().sort_values(ascending=False).round(2)
)
linha_top = faturamento_por_linha.idxmax()
cores = ["orange" if linha == linha_top else "#0C1251" for linha in faturamento_por_linha.index]

plt.figure(figsize=(9, 5))
bars = plt.bar(faturamento_por_linha.index, faturamento_por_linha.values, color=cores)
plt.bar_label(bars, fmt="%.0f", padding=3)

plt.title("Faturamento por linha de produto")
plt.xlabel("Linha de produto")
plt.ylabel("Faturamento")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

os.makedirs("charts", exist_ok=True)
plt.savefig("charts/faturamento_linha_produto.png")
plt.show()


#Qual linha de produto recebeu a melhor avaliação média?
avaliacao_linha_produto = df.groupby('linha_produto')['avaliacao'].mean().sort_values(ascending=False).round(2)
avaliacao_linha_produto = (
    df.groupby("linha_produto")["avaliacao"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 5))
barras = ax.barh(avaliacao_linha_produto.index, avaliacao_linha_produto.values, color="#3A07D6")
ax.bar_label(barras, fmt="%.2f", padding=3)

ax.set_title("Avaliação média por linha de produto")
ax.set_xlabel("Avaliação média")
ax.set_ylabel("Linha de produto")
ax.set_xlim(0, 10)
ax.invert_yaxis() 
fig.tight_layout()

os.makedirs("charts", exist_ok=True)
fig.savefig("charts/avaliacao_linha_produto.png")
plt.show()

#Qual foi a forma de pagamento mais utilizada?
pagamentos = df["forma_pagamento"].value_counts()
percentuais = (pagamentos / pagamentos.sum() * 100).round(1)

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(pagamentos.index, pagamentos.values, color=["#4C72B0", "#55A868", "#C44E52"])
ax.bar_label(
    barras,
    labels=[f"{n} ({p}%)" for n, p in zip(pagamentos.values, percentuais.values)],
    padding=3,
)

ax.set_title("Formas de pagamento mais utilizadas")
ax.set_xlabel("Forma de pagamento")
ax.set_ylabel("Número de vendas")
ax.set_ylim(0, pagamentos.max() * 1.15) 
fig.tight_layout()

os.makedirs("charts", exist_ok=True)
fig.savefig("charts/forma_pagamento.png")
plt.show()

#  Qual foi o valor médio das vendas?

media_vendas = df['vendas'].mean()

#Qual foi a maior venda registrada?
maior_venda = df['vendas'].max()

#Em qual dia da semana ocorreu a maior quantidade de vendas?
vendas_por_dia = df["dia_semana"].value_counts()
ordem = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
vendas_dia = df["dia_semana"].value_counts().reindex(ordem)
fig, ax = plt.subplots(figsize=(9, 5))
barras = ax.bar(vendas_dia.index, vendas_dia.values, color="#045333")
ax.bar_label(barras, padding=3)

ax.set_title("Número de vendas por dia da semana")
ax.set_xlabel("Dia da semana")
ax.set_ylabel("Número de vendas")
ax.set_ylim(0, vendas_dia.max() * 1.15)
fig.tight_layout()

os.makedirs("charts", exist_ok=True)
fig.savefig("charts/vendas_dia_semana.png")
plt.show()

