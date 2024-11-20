nome = input('Qual seu nome? ')
print(f'Olá, {nome}! \nVamos fazer alguns cálculos simples.\n\n')

numero_1 = input('Digite um número: ') # RECEBEM COMO STRING
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) #TRANSFORMANDO STRING EM INT
int_numero_2 = int(numero_2)

string = 'Você digitou {0} e {1}.'
formato = string.format(numero_1, numero_2)

print(formato)

print('A soma dos números é', int(numero_1) + int(numero_2))
print(f'A soma FORMATADA dos números é {int_numero_1 + int_numero_2}') #FORMATADO COM INT
