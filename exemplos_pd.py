import pandas as pd

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)

print('\nCriando DataFrame\n')
# Usando uma lista de dicionário
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False,
     'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False,
     'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False,
     'Valor': 72832.16}
]
# Usando um dicionário de listas
dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}
dataset = pd.DataFrame(dados)

# Usando arquivo
dataset = pd.read_csv('./data/db.csv', sep=';', index_col=0)  # index_col: identifica a coluna do índice primário
print(dataset)

print('Tipos das colunas:\n')
print(dataset.dtypes)

print('\nResumo estatístico:\n')
print(dataset[['Quilometragem', 'Valor']].describe())

print('\nInfo gerais:\n')
print(dataset.info())

print('\nSelecionando o cabeçalho:\n')
dataset = dataset.head()
print(dataset)
