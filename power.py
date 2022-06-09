def decimalToBinary(n):
    return '{:0>8}'.format(str(bin(int(n)))[2:])

def power(x,a,n):
    a = list(str(decimalToBinary(a)))
    w=1
    t=i=0

    for t in [7,6, 5, 4,3,2,1,0]:
        w=(pow(w,2)%n)
        if(a[i]==1):
            w=w*x%n
            print(w)
    return(w)

print(power(67,5019,31351))
