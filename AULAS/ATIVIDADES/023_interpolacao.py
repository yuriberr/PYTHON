"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""
nome = 'Yuri'
preco = 1000.958652
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500))
