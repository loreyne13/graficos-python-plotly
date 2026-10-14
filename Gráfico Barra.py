#importar biblioteca pandas e plotly express "as pd e px são nomes dados as respecitivas bibliotecas para facilitar a escrita do código"
import pandas as pd
import plotly.express as px

df = pd.read_csv("vendas.csv") #ler o arquivo csv e armazenar na variável df

#criar tabela e somar por categoria
dados = df.groupby("categoria", as_index=False)["vendas"].sum()

#criar gráfico de barras com os dados agrupados
fig = px.bar(dados, x="categoria", y="vendas", title="Vendas por Categoria") 

fig.write_html("meu_grafico.html")
