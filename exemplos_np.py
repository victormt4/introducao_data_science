import numpy as np

kms = np.loadtxt(fname='data/carros-km.txt', dtype=int)
anos = np.loadtxt(fname='data/carros-anos.txt', dtype=int)

print('\nArray multidimensional:\n')
multi_arr = np.array([kms, anos])
print(multi_arr)

# Operações

print('\nMédias:\n')
ano_atual = 2020
# km_media = kms / (ano_atual - anos)  # executa km / (2020 - ano) para cada item do vetor
km_media = multi_arr[0] / (ano_atual - multi_arr[1])
print(km_media)

print('\nIdades dos carros:\n')
idades = ano_atual - anos
print(idades)

print('\nIdades maiores que 20:\n')
idades = idades[idades > 20]
print(idades)

print('\nAno fabricação maior que 2015 multidimensional:\n')
multi_arr = multi_arr[:, multi_arr[1] > 2015]
print(multi_arr)

# Atributos do Numpy
print('\nDimensões:\n')
print(multi_arr.shape)

print('\nQuantidade de dimensões:\n')
print(multi_arr.ndim)

print('\nQuantidade de elementos:\n')
print(multi_arr.size)

print('\nTipo dos dados:\n')
print(multi_arr.dtype)

# print('\nArray transposto:\n')
# print(multi_arr.T)

# Métodos

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print('\nConvertendo para lista do Python:\n')
print(arr.tolist())

print('\nAlterando formato do array:\n')
print(arr.reshape((5, 2), order='C'))

print('\nAdicionando dimensão:\n')
multi_arr_new = multi_arr.copy()
multi_arr_new.resize((3, multi_arr_new[1].size), refcheck=False)
multi_arr_new[2] = multi_arr_new[0] / (ano_atual - multi_arr_new[1])  # Calculando quilometragem media para a dimensão
print(multi_arr_new)
