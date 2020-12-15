def main():
    input_ = int(input('Enter: '))
    num2text(input_)


def num2text(input_):
    my_list = split_text(input_)
    

def split_text(input_):
    num = str(input_)
    mod = len(num) % 3
    my_list = []
    index = mod + 3
    if mod > 0:
        my_list.append(num[0:mod])
        for i in range(len(num) // 3):
            my_list.append(num[mod:index])
            mod = index
            index = index + 3
    else:
        for i in range(len(num) // 3):
            my_list.append(num[mod:index])
            mod = index
            index = index + 3
    return my_list

main()
