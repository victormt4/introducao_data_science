import pandas as pd

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)

dataset = pd.read_csv('./data/db.csv', sep=';')

print('Tipos das colunas:\n')
print(dataset.dtypes)

print('\nResumo estatístico:\n')
print(dataset[['Quilometragem', 'Valor']].describe())

print('\nInfo gerais:\n')
print(dataset.info())
