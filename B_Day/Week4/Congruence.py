def main():
    # Enter the equation
    eq = input('Enter equation: ')
    if ' ' in eq:
        eq = eq.replace(' ', '')
    if 'x' in eq:
        eq = eq.replace('x', 'X')
    a = int(eq[:eq.index('*')])
    b = int(eq[eq.index('=') + 1:eq.index('(')])
    n = int(eq[eq.index('d') + 1:eq.index(')')])
    if a > n:
        a = a % n

    # Calculate GCD and Quotient
    q = []
    n2 = n
    while a != 0:
        q.append(n // a)
        tmp = a
        a = n % a
        n = tmp
    gcd = n
    print('GCD:', gcd)
    print('Quotient:', q)

    # Extended Euclidean Algorithm
    p = [0] * (len(q) + 1)
    p[0] = 0
    p[1] = 1
    for i in range(2, len(q) + 1):
        tmp = p[i - 2] - p[i - 1] * q[i - 2]
        p[i] = mod(tmp, n2)

    r = p[len(p) - 1]
    x0 = (r * b) // gcd
    x = mod(x0, n2 // gcd)
    print('X:', x)


# Mod cal
def mod(tmp, n2):
    if tmp < 0 and -tmp < n2:
        return n2 + tmp
    elif tmp < 0 and -tmp > n2:
        tmp = -tmp % n2
        return n2 - tmp
    elif tmp > 0:
        return tmp % n2


main()
