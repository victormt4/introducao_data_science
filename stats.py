import numpy as np

ano = np.loadtxt(fname='data/carros-anos.txt', dtype=int)
km = np.loadtxt(fname='data/carros-km.txt', dtype=int)
valor = np.loadtxt(fname='data/carros-valor.txt')

dataset = np.column_stack((ano, km, valor))

print('\nMédia:\n')
print(np.mean(dataset[:, 1:], axis=0))  # Calculando a média da quilometragem e valor ignorando o ano

print('\nDesvio padrão:\n')
print(np.std(dataset[:, 1:], axis=0))

print('\nSomatório:\n')
print(np.sum(dataset, axis=0))
print(dataset[:, 1].sum())  # somente quilometragem
