def main():
    sentence = input("Enter a sentence: ")
    print(convert(sentence))


def convert(string):
    sen = ''
    list_string = string.split(" ")
    for str in list_string:
        str = str.upper()
        sen += str[1:len(str)] + str[0] + 'AY '
    return sen


main()