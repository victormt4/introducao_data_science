import numpy as np

kms = np.loadtxt('data/carros-km.txt')
anos = np.loadtxt('data/carros-anos.txt', dtype=int)

km_media = kms / (2019 - anos)  # executa km / (2020 - ano) para cada item do vetor

print(km_media)