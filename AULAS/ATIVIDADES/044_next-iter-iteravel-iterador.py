""" 
COMO FUNCIONA O FOR:

Iteravel: Um objeto que implementa o método __iter__ que retorna um iterador.
Iterador: Um objeto que implementa o método __next__ que retorna o próximo item da sequência.
Next: Retorna o próximo item de um objeto iterador.
iter(): Retorna um iterador a partir de um objeto iterável.

Iterável -> str, range, list, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Yuri')

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))


texto = 'Yuri'
iterador = iter(texto)

"""
for letra in texto:
    print(letra)
"""

while True:
    try:
        letra = next(iterador)  # Vai pegar o próximo item do iterador.
        print(letra)
    except StopIteration:  # Quando o iterador chegar ao fim, ele vai lançar essa exceção.
        break
    
print('\nFim do laço\n')