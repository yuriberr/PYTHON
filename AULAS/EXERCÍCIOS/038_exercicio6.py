#       012345678910
nome = 'Luiz Otávio'

indice = len(nome)
print(nome)
print(indice)
print(nome[3])

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}' 
    indice += 1

novo_nome += '*'    
print(novo_nome)
    
