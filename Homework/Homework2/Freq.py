def main():
    string = input("Enter a string: ")
    print("The most frequence character: ", most_frequence(string))


def most_frequence(string):
    counter = 0
    max_count = 0
    most_fre_char = ''
    for ch in string:
        for str in string:
            if ch == str:
                counter += 1
        if counter > max_count :
            max_count = counter
            most_fre_char = ch
        counter = 0
    return most_fre_char


main()