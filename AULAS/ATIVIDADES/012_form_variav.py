nome = 'Yuri'
altura = 1.75
peso = 80.3
imc = peso / altura ** 2

# f-strings
texto = f'{nome} tem {altura:.2f} de altura, pesa {peso:.2f} quilos e seu IMC é de {imc}.'

print(texto)