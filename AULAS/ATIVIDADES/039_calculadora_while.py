""" Calculadora com while """

while True:

    numero_1 = (input('\nDigite um número:    '))
    if numero_1.isdigit():  # VERIFICA SE O NUMERO DIGITADO E UM NUMERO INTEIRO
        numero_2 = (input('\nDigite outro número: '))
        if numero_2.isdigit():
            operador = input('\nDigite um operador para o cálculo (+, -, *, /): ')
        
            ### CALCULOS ###
            # SOMA:
            if operador == '+':
                soma = int(numero_1) + int(numero_2)
                print(f'\n{numero_1} + {numero_2} = {soma}')
                print(f'O resultado da soma é: {soma}')

            # SUBTRAÇÃO:
            elif operador == '-':
                subtracao = int(numero_1) - int(numero_2)
                print(f'\n{numero_1} - {numero_2} = {subtracao}')
                print(f'O resultado da subtração é: {subtracao}')

            # MULTIPLICAÇÃO:
            elif operador == '*':
                multiplicacao = int(numero_1) * int(numero_2)
                print(f'\n{numero_1} X {numero_2} = {multiplicacao}')
                print(f'O resultado da multiplicação é: {multiplicacao}')

            # DIVISÃO:
            elif operador == '/':
                divisao = int(numero_1) / int(numero_2)
                print(f'\n{numero_1} / {numero_2} = {divisao}')
                print(f'O resultado da divisão é: {divisao}')
            else:
                print('Operador inválido')
                
                
        else:
            print('Isso não é um número')
    else:
        print('Isso não é um número')
    sair = input('\nDeseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
