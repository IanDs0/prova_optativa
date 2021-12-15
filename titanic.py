import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('./titanic.csv')

#print(titanic.head(10))#printa os 10 primeiros

titanic.sort_values(by=['Name'], ascending=True, inplace=True)#ordena

#print(titanic.head(10))#printa ordenado

titanic['Sobrevivente']= titanic['Survived'].map({1:'Sim', 0:'Não'})#cria uma nova coluna colocando se morreu ou não com sim ou não

#print(titanic.head(10))#printa com a coluna extra

titanic = titanic.drop(columns=['SibSp', 'Parch', 'Ticket'])#remove "SibSp", "Parch", "Ticket"

#print(titanic.head(10))#printa sem as colunas "SibSp", "Parch", "Ticket"

titanic = titanic.rename(columns={"Name":"Nome", "PassengerId":"BilheteId", "Survived":"Sobrevive", "Pclass":"Classe_P", "Sex":"Sexo", "Age":"Idade", "Fare":"Tarifa", "Cabin":"Cabine", "Embarked":"Embacou"})#troca os nomes das colunas em ingles para portugues

#print(titanic.head(10))#printa com as colunas com nome trocado

titanic['Sexo'] = titanic['Sexo'].replace(['male','female'],['masculino','FEMININO'])#altera os valors male e flame das colunas

#print(titanic.head(10))#printa com a tradução dos sexos

sobrevivente_class = titanic.groupby(['Classe_P','Sobrevivente'])['Sobrevive'].count()#agrpa classe por sobrevivente

print(sobrevivente_class.head(10))#printa o numero de sobreviventes por classe

sobrevivente_sexo = titanic.groupby(['Sexo','Sobrevivente'])['Sexo'].count()#agrupa sexo com sobrevivente

print(sobrevivente_sexo.head(10))#printa o numero de sobrevidentes por sexo

sobrevivente_class.plot(kind = 'pie')#monta o gráfico em pizza
plt.show()

titanic.to_excel('titanic.xlsx',index = None, header=True)#convertendo csv para o arquivo xlsx
