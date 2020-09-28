def main():
    print('Enter phone number in the format XXX-XXX-XXXX: ')
    phone_num = input()
    alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    num = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

    for i in range(len(phone_num)):
        if phone_num[i].isalpha():
            print(num[alp.index(phone_num[i])], end='')
        else:
            print(phone_num[i], end='')

main()