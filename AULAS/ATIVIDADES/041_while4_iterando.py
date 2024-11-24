phrase = 'aaaaoo'

i = 0
qt_shows_most = 0
qt_letter_shows_most = ''

while i < len(phrase):
    letter = phrase[i]

    if letter == ' ':
        i += 1
        continue

    letter_shows = phrase.count(letter)

    if qt_shows_most < letter_shows:
        qt_shows_most = letter_shows
        qt_letter_shows_most = letter

    i += 1
    break
print('The letter that shows the most was '
    f'"{qt_letter_shows_most}" with {qt_shows_most}x shows')
print('letter = ',qt_letter_shows_most)
    