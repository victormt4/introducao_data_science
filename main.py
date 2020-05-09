import numpy as np

kms = np.loadtxt(fname='data/carros-km.txt', dtype=int)
anos = np.loadtxt(fname='data/carros-anos.txt', dtype=int)

km_media = kms / (2019 - anos)  # executa km / (2020 - ano) para cada item do vetor

print(km_media)
print(km_media.shape)  # dimensões do array