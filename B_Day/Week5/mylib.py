def congruence(a, b, n):
    # ENTER EQUATION
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

    # EXTENDED EUCLIDEAN ALGORITHM AND PRINT STEPS
    p = [0] * (len(q) + 1)
    p[0] = 0
    p[1] = 1
    for i in range(2, len(q) + 1):
        tmp = p[i - 2] - p[i - 1] * q[i - 2]
        p[i] = mod(tmp, n2)

    # FIND X
    r = p[len(p) - 1]
    x0 = (r * b) // gcd
    x = mod(x0, n2 // gcd)
    return x


# MOD CALCULATOR
def mod(tmp, n2):
    if tmp < 0:
        while tmp < 0:
            tmp += n2
        return tmp % n2
    elif tmp > 0:
        return tmp % n2
