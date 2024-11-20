valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor: ')

if int(valor_1) > int(valor_2):  # Tive que mudar para inteiro para não dar erro na leitura de int
    print(f'O valor 1 = {valor_1}, é maior que o valor 2 = {valor_2}')

elif int(valor_2) > int(valor_1):
    print(f'O valor 2 = {valor_2}, é maior que o valor 1 = {valor_1}')

else:
    print(f'Os valores digitados: {valor_1} e {valor_2}, são iguais!')
