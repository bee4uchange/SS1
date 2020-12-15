def main():
    name = list(map(str, input('Enter name: ').split(' ')))
    print('Initials: ' + name[0][0] + '. ' + name[1][0] + '. ' + name[2][0])

main()