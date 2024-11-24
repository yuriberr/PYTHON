
# FOR como While:

for i in range(10):
    if i == 2:
        print('Pulei o 2')
        continue
    if i == 8:
        print('Parei no 8, seu else não executará')	
        break
    for j in range(1, 8, 2):
        print(i, j)
else:
    print('For completo com sucesso!')