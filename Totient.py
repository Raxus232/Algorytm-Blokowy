def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    print(p)
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def totient(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]

        return len(n)


print(totient(int(input("Podaj liczbę: "))))
