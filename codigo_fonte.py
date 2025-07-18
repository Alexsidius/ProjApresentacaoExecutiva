#codigo de projeto em Python em ciencia de dados
#usando numPy, Pandas e MatPlotLib
#Autor: Alexandro Ferreira

#improtando biblioteca pandas
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

#importando base de dados
base = pd.read_csv('base_dados.csv')

#exibindo base
# print(base)
# print(base.head())

#exibe o resumo do dataframe 
# base.info()

#exibir quantidade de linhas e colunas
# print(base.shape)

#filtrar linhas com codigo postal nulo
#print(base[base['Postal Code'].isnull()])


#atribuir valores ao codigo postal que estavam em branco e todos eram da mesma cidade e estado. 
#pesquisamos qual  o codigo postal e atribuimos o valor 5401
base.loc[(base.City == 'Burlington') & (base.State == "Vermont") & (base['Postal Code'].isnull()), "Postal Code"]= 5401

#atualizando informacoes abaixo connfirmarmos que o dataFrame ficou sem dados nulos
# print(base.info())

#caso quisesse apenas eliminar a linha Postal Code usariamos o codigo abaixo
base2 = base.drop('Postal Code', axis=1) #xis1  = apaga coluna, axis 0 = apaga linha

# print(base2.info())

print("")
print("informações do dataframe sem valores nulos e com datas ajustadas: ")
print("")
#convertendo colunas para data
base["Order Date"] = pd.to_datetime(base["Order Date"], format='%d/%m/%Y')
base['Ship Date'] = pd.to_datetime(base['Ship Date'], format='%d/%m/%Y')
print(base.info())

print("")
print("data minima e máxima: ")
#agora com formato da data correto podemos analisar qual a data minima, a mais antiga do abase
print (base['Order Date'].min()) #resultado deu 03/01/2015

#agora podemos avaliar a data mais recente, ultima
print (base['Order Date'].max()) #resultado deu 30/12/2018

#criando uma coluna com Ano
base['Ano'] = base['Order Date'].dt.year
print(base.info())


vendasAno = base.groupby('Ano')['Sales'].sum()
print('')
print('Vendas resumo anual')
print(vendasAno)
print(vendasAno.info())

vendasAno.plot.bar()
plt.title("Vendas por Ano")
plt.xlabel("Ano")
plt.ylabel("Sales")
plt.grid(False)
plt.show()
