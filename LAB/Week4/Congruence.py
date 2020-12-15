def main():
    # ENTER EQUATION
    print('Equation: a * X = b (mod n)')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    n = int(input('Enter n: '))
    a2 = a
    if a > n:
        a = a % n

    # CALCULATE GCD AND QUOTIENT
    q = []
    n2 = n
    while a != 0:
        q.append(n // a)
        tmp = a
        a = n % a
        n = tmp
    gcd = n
    print()
    print('qi = ' + str(q))
    print('We have d = ' + 'gcd(' + str(a2) + ', ' + str(n2) + ') = ' + str(gcd))

    # EXTENDED EUCLIDEAN ALGORITHM AND PRINT STEPS
    p = [0] * (len(q) + 1)
    p[0] = 0
    p[1] = 1
    print('- Step 0: p0 = 0')
    print('- Step 0: p1 = 1')
    for i in range(2, len(q) + 1):
        tmp = p[i - 2] - p[i - 1] * q[i - 2]
        p[i] = mod(tmp, n2)
        print('- Step ' + str(i) + ': p' + str(i) + ' = ' + str(p[i - 2]) + ' - ' + str(p[i - 1]) + '.(' + str(q[i - 2])
              + ') mod ' + str(n2) + ' = ' + str(p[i]))
    print()

    # FIND X
    r = p[len(p) - 1]
    x0 = (r * b) // gcd
    print('x0 = (r * b)/d mod (n/d) = (' + str(r) + ' * ' + str(b) + ')/' + str(gcd) + ' mod (' + str(n2) + '/'
          + str(gcd) + ')')
    x = mod(x0, n2 // gcd)
    print('x = x0 =', x)


# MOD CALCULATOR
def mod(tmp, n2):
    if tmp < 0:
        while tmp < 0:
            tmp += n2
        return tmp % n2
    elif tmp > 0:
        return tmp % n2


main()
