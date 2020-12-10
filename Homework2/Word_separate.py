def main():
    sentence = input("Enter a sentence in which all of the words are"
                     "run together \nbut the first character of each word is uppercase: ")
    print(convert(sentence))


def convert(string):
    sen = string[0]

    for ch in string[1:]:
        if ch.isupper():
            sen += ' ' + ch.lower()
        else :
            sen += ch
    return sen


main()