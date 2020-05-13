import pandas as pd

dataset = pd.read_csv('./data/db.csv', sep=';', index_col=0)
# dataset = dataset.head()

print('\nSelecionando uma coluna:\n')
print(dataset['Valor'])

print('\nSelecionando múltiplas colunas:\n')
print(dataset[['Quilometragem', 'Valor']])

print('\nSelecionando linhas:\n')
print(dataset[0:3])

print('\nSelecionar pela coluna:\n')
print(dataset.loc['Passat'])

print('\nSelecionar por multiplos valores da coluna:\n')
print(dataset.loc[['Passat', 'Crossfox']])

print('\nSelecionar linhas e colunas:\n')
print(dataset.loc[['Passat', 'Crossfox'], ['Quilometragem', 'Valor']])

print('\nSelecionar pelo índice númerico:\n')
print(dataset.iloc[1])

print('\nSelecionar linhas e colunas pelo índice numérico:\n')
print(dataset.iloc[:3, [0, 2]])

print('\nSelecionar valores iguais a X:\n')
select = dataset.Motor == 'Motor Diesel'  # retorna uma Series
print(dataset[select])

print('\nSelecionar multiplos:\n')
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])

print('\nSelecionar usando query:\n')
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))