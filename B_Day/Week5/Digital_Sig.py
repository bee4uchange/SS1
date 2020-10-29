import random
import mylib


def main():
    # p = 0
    # q = 1000
    # pq = []
    # for i in range(2):
    # cached_primes = [i for i in range(p, q) if isPrime(i)]
    # n = random.choice([i for i in cached_primes if p < i < q])
    # pq.append(n)
    # print(pq)
    c = 'y'
    sig_s = ''
    sig_g = ''
    message = []
    while c == 'y':
        print('1. Digital Signature' + '\n' + '2. Check' + '\n' + 'Choose one: ')
        choose = int(input())
        if choose == 2:
            key = key_gen()[1]
            c_text = list(map(int, message[1].split(' ')))
            print(c_text)
            p_text = []
            for i in c_text:
                p_text.append(decrypt(i, key[1], key[0]))
            for i in p_text:
                sig_g += i
            print('----> Original text: ', sig_g)
            if sig_g == message[0]:
                print('Verified')

        elif choose == 1:
            key = key_gen()[0]
            m = input('Message: ')
            sig = []
            p_text = []
            for i in range(len(m)):
                sig.append(ord(m[i]))
            for i in sig:
                p_text.append(sig_gen(i, key[1], key[0]))
            for i in range(len(p_text)):
                if i == len(p_text) - 1:
                    sig_s += p_text[i]
                else:
                    sig_s += p_text[i] + ' '
            message = [m, sig_s]
            print('----> Message to send: ', message)
        print('----Continue----')
        c = input()


def key_gen():
    p = 7
    q = 11
    e = 17
    n = p * q
    z = (p - 1) * (q - 1)
    d = mylib.congruence(n, 1, z)
    public_k = [n, e]
    private_k = [n, d]
    p_text = [public_k, private_k]
    return p_text


def decrypt(a, b, n):
    b_bin = str(bin(b)[2:])[::-1]
    total = 1
    list_ = partial(a, b_bin, n)
    i = 0
    while i < len(list_) - 1:
        count = mylib.mod(list_[i] * list_[i + 1], n)
        total = total * count
        i += 2

    total = mylib.mod(total, n)
    return chr(total)


def sig_gen(a, b, n):
    b_bin = str(bin(b)[2:])[::-1]
    total = 1
    list_ = partial(a, b_bin, n)
    i = 0
    while i < len(list_) - 1:
        count = mylib.mod(list_[i] * list_[i + 1], n)
        total = total * count
        i += 2

    total = mylib.mod(total, n)
    return str(total)


def partial(a, b, n):
    my_list = [a]
    for i in range(1, len(b)):
        a = pow(a, 2)
        a = mylib.mod(a, n)
        if int(b[i]) == 1:
            my_list.append(a)
    return my_list


def isPrime(num):
    prime = 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime = num
    return prime


main()
