import math
#import Totient.py


def rsa(a,b):
    if (b == 0):
        r=a
        x = 1
        y=0
        return(r,x,y)
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while(b>0):
            s = math.floor(a/b)
            r = a-(s*b)
            x = x2-(s*x1)
            y = y2-(s*y1)
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
            print("s:"+str(s))
            print("r:"+str(r))
            print("x:"+str(x))
            print("y:"+str(y))
            print("a:"+str(a))
            print("b:"+str(b))
            print("x2:"+str(x2))
            print("x1:"+str(x1))
            print("y2:"+str(y2))
            print("y1:"+str(y1))
            print("\n\n")
    r=a
    x=x2
    y=y2
    return(r,x,y)

#print("Wynik ost:"+str(rsa(107,293)))
print("Wynik ost:"+str(rsa(4864,3458)))
#
# # Python program for the extended Euclidean algorithm
# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x
#
#
# if __name__ == '__main__':
#
#     gcd, x, y = extended_gcd(30, 50)
#     print('The GCD is', gcd)
#     print(f'x = {x}, y = {y}')
#
#
# extended_gcd(107,293)
