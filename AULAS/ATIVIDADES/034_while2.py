"""
loop
laço
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Digite seu nome ou "sair": ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
print('Acabou!')    
