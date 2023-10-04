import random
final = ''
with open('poprehadzovany_text1_vstup.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        without_spaces = line.replace('\n','')
        x = without_spaces.split(' ')
        for i in x:
            if len(i) > 2:
                f = random.sample(i[1:-1],len(i)-2)
                res = "".join(f)
                final += i[0] + res + i[-1] + ' '
            else:
                final += i +' '
        final = final.rstrip(' ')
        final += '\n'
    print(final)
with open('Poprehadzovaný_text1.txt','w',encoding= 'utf-8') as fp:
    fp.write(final)