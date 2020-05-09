import numpy as np

kms = np.loadtxt(fname='data/carros-km.txt', dtype=int)
anos = np.loadtxt(fname='data/carros-anos.txt', dtype=int)

print('\nArray multidimensional:')
multi_arr = np.array([kms, anos])
print(multi_arr)

print('\nMédias:')
ano_atual = 2020
# km_media = kms / (ano_atual - anos)  # executa km / (2020 - ano) para cada item do vetor
km_media = multi_arr[0] / (ano_atual - multi_arr[1])
print(km_media)

print('\nDimensões:')
print(km_media.shape)

print('\nIdades dos carros:')
idades = ano_atual - anos
print(idades)

print('\nIdades maiores que 20:')
idades = idades[idades > 20]
print(idades)

print('\nAno fabricação maior que 2015 multidimensional')
multi_arr = multi_arr[:, multi_arr[1] > 2015]
print(multi_arr)
