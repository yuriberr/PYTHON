a = 'AAA'
b = 'BBB'
c = 1.2

string = '1 = {1} | 2 = {2:.2f} | 3 = {0}'
formato = string.format(a, b, c)
# formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)