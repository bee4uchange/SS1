def main():
    print('a^b (mod n) = ?')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    n = int(input('Enter n: '))

    b_bin = str(bin(b)[2:])[::-1]
    total = 1
    list_ = partial(a, b_bin, n)
    i = 0
    while i < len(list_) - 1:
        count = mod(list_[i] * list_[i + 1], n)
        total = total * count
        i += 2

    print('Result:', mod(total, n))


def partial(a, b, n):
    my_list = [a]
    for i in range(1, len(b)):
        a = pow(a, 2)
        a = mod(a, n)
        if int(b[i]) == 1:
            my_list.append(a)

    return my_list


def mod(tmp, n2):
    if tmp < 0:
        while tmp < 0:
            tmp += n2
        return tmp % n2
    elif tmp > 0:
        return tmp % n2


main()
