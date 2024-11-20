"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')

if int(hora) >= 0 and int(hora) <= 11:
    print('Bom dia!')
elif int(hora) >= 12 and int(hora) <= 17:
    print('Boa tarde!')
elif int(hora) >= 18 and int(hora) <= 23:
    print('Boa noite!')
else:
    print('Hora inválida!')