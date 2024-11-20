"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_int = input('Digite um número inteiro: ')

if num_int.isdigit():
    if int(num_int) % 2 == 0:
        print(f'{num_int} é par')
    else:
        print(f'{num_int} é impar')
else:
    print('Isso não é um número')