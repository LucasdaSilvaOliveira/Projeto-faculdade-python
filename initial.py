import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("varejo.csv")

print("Dados Carregados:")
print(df.head())

vendas_categoria = df.groupby('Categoria')['Total'].sum().reset_index()
print("\nTotal de Vendas por Categoria:")
print(vendas_categoria)

vendas_genero = df.groupby('Sexo')['Total'].sum().reset_index()
print("\nTotal de Vendas por Gênero:")
print(vendas_genero)

idade_clientes = df['Idade'].dropna()
print("\nDistribuição de Idade dos Clientes:")
print(idade_clientes.describe())

plt.figure(figsize=(10, 6))
sns.barplot(x='Categoria', y='Total', data=df, estimator=sum, ci=None)
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total de Vendas')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Sexo', y='Total', data=df, estimator=sum, ci=None)
plt.title('Total de Vendas por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Total de Vendas')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(idade_clientes, bins=15, kde=True)
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()