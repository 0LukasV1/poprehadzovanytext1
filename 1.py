import random

final = ''

with open('poprehadzovany_text1_vstup.txt', 'r', encoding='utf-8') as fp:
    lines = fp.readlines()
    for line in lines:
        without_spaces = line.replace('\n', '')
        words = without_spaces.split(' ')
        for word in words:
            if len(word) > 2:
                middle_part = random.sample(word[1:-1], len(word) - 2)
                shuffled_word = word[0] + ''.join(middle_part) + word[-1]
                final += shuffled_word + ' '
            else:
                final += word + ' '
        final = final.rstrip(' ')
        final += '\n'

print(final)

with open('Poprehadzovaný_text1.txt', 'w', encoding='utf-8') as fp:
    fp.write(final)