def main():
    sentence = input('Sentence: ')

    count_v = 0
    count_c = 0
    vowels = ['u', 'e', 'o', 'a', 'i']
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            if sentence[i] in vowels:
                count_v += 1
            else:
                count_c += 1

    print('The number of vowels:', count_v)
    print('The number of consonants:', count_c)


main()
