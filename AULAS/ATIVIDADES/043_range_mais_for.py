"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(3, 20, 3)
# Será contabilizado os numeros de 3 a 20, pulando de 3 em 3, no print da variavel criada pelo FOR: numero
for numero in numeros:
    print(numero)
# fim do laço   
print('\n\n')
print('-0'*10, end='-')
print('\n\n')

numeros = range(20, 3, -2) #Cuidar o range para o start ser maior que o stop, para que o step seja negativo.
# será contabilizado os numeros de 20 a 3, pulando de -2 em -2, no print da variavel criada pelo FOR: numero
for numero in numeros:
    print(numero)

