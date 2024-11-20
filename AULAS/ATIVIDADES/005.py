print(1 + 1)
print('a' + 'b')

#print('a' + 1) # erro, python só soma int com float
print(int('1'), type(int('1'))) # checa o tipo depois da conversão para int
print(int('1') + 1.23) # transforma para int para depois fazer a soma

print(bool('')) #bool sem valor vira False
print(bool('a')) #bool com qualquer valor vira True

print(str('1') + 'b') # transforma para str para depois concatenar