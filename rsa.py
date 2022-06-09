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
            e=b
            print("s:"+str(s))
            print("r:"+str(r))
            print("x:"+str(x))
            print("y:"+str(y))
            print("a:"+str(a))
            print("b:"+str(b))
            print("phi(n):"+str((a-1)*(b-1)))
            print("e:"+str(e))
            print("x2:"+str(x2))
            print("x1:"+str(x1))
            print("y2:"+str(y2))
            print("y1:"+str(y1))
            print("\n")
    r=a
    x=x2
    y=y2
    return(r,x,y)


def esc(x,a,n):
    w= (pow(x,a)%n)
    return(w)



print("Wynik ost:"+str(rsa(int(input("Podaj p:")),int(input("Podaj q:")))))

#print("Wynik ost:"+str(rsa(4864,3458)))
#print(esc(5,117,119)) phi = p-1*q-1
#print("w:"+str(func(5,117,119)))
#= e-1 mod φ(n).
