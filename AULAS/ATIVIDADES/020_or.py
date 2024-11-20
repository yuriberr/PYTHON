entrada = input('[E]ntrar ou [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:    
        print('Bem vindo!\nAcesso permitido')
 
else:
    print('Até logo! \nSaindo do sistema')

# Avaliação de curto circuito OR
senha_or = input('Digite a senha: ') or 'Sem senha'
print(senha_or)