# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o 
# -6-5-4-3-2-1 
nome = 'Otávio'
# print(nome[2]) # retorna: á
# print(nome[-4]) # retorna: á
print('vio' in nome)
print('zero' in nome)
print('t' in nome)
print('c' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)
# CHECAGEM DE ITENS DE UMA STRING
print(10 * '- ')
print(10 * ' |')
print(10 * '- ')
nome_2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_2:
    print(f'{encontrar} está em {nome_2}.')
else:
        print(f'{encontrar} não está em {nome_2}.')