"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [inicio : final : passo] [i:f:p]
Obs.: a função len retorna a quantidade de caracteres da string

"""
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[0:5])
print(len(variavel[1:5]))  # len conta quantos caractéres tem
print(variavel[0:9:2])  # De 0 a 9 pulando de 2 em 2
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[::1 ])
