def main():
    sentence = input('Sentence: ')
    if '  ' in sentence:
        sentence = sentence.replace('  ', ' ')
    if ' . ' in sentence:
        sentence = sentence.replace(' . ', '.')
    if '.' in sentence:
        sentence = sentence.replace('.', '. ')
    for i in range(len(sentence)):
        if i == 0:
            print(sentence[i].upper(), end='')
        elif sentence[i-2] == '.' and i > sentence.index('.'):
            print(sentence[i].upper(), end='')
        elif sentence[i-2] == '?' and i > sentence.index('?'):
            print(sentence[i].upper(), end='')
        elif sentence[i-2] == '!' and i > sentence.index('!'):
            print(sentence[i].upper(), end='')
        elif sentence[i-2] == '...' and i > sentence.index('...'):
            print(sentence[i].upper(), end='')
        else:
            print(sentence[i], end='')

main()
