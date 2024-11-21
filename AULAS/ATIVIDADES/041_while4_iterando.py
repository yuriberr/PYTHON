phrase = 'Python is a programming language' \
    'multiparadigm' \
    'Python was created by Guido van Rossum.'

print(phrase.count('Python'))  # Conta quantas vezes aparece a palavra Python
print(phrase.count('o'))

print('')
qt_shows_most = 0
qt_letter_shows_most = ''
i = 0
while i < len(phrase):
    letter = phrase[i]
    letter_shows = phrase.count(letter)

    if letter_shows > qt_shows_most:
        qt_shows_most = qt_letter_shows_most
        qt_letter_shows_most = letter

    i += 1

    print(f'{letter}: {letter_shows}')
