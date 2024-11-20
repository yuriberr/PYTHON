entrada = input('[E]ntrar ou [S]air: ')

if entrada == 'E':
    senha = input('Senha: ')
    senha_permitida = '123456'
    if senha == senha_permitida:
        print('Bem vindo!\nAcesso permitido')
    else:
        print('Senha incorreta! \nPor segurança, estamos saindo do sistema!')    
elif entrada == 'S':
    print('Até logo! \nSaindo do sistema')
else:
    print('Digito inválido! \nTente novamente usando [E]ntrar ou [S]air.')