entrada = input('[E]ntrar ou [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida:    
        print('Bem vindo!\nAcesso permitido')
elif entrada == 'E' and senha != senha_permitida:
        print('Senha incorreta! \nPor segurança, estamos saindo do sistema!') 
elif entrada == 'S':
    print('Até logo! \nSaindo do sistema')
else:
    print('Digito inválido! \nTente novamente usando [E]ntrar ou [S]air.')

