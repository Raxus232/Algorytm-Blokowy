import binascii
# p = 11 # wylosoana liczba
# q = 19 #  wylosowana liczba
# a = 5 #  losowo wybrana liczba naturalna NWD(a,n) = 1
# n = (p*q)
#
# x0 = (a**2)%n
# x1 = (x0**2)%n
# x2 = (x1**2)%n
# x3 = (x2**2)%n
# x4 = (x3**2)%n
# x5 = (x4**2)%n
# x6 = (x5**2)%n
#
#
# print(n)
# print("x0: "+str(x0))
# print("x1: "+str(x1))
# print("x2: "+str(x2))
# print("x2: "+str(x2))
# print("x3: "+str(x3))
# print("x4: "+str(x4))
# print("x5: "+str(x5))
# print("x6: "+str(x6))
#
#

#57 53 42
#  m  010101110101001101000010
# XOR
# k  101010101010101010101010 - swqoje
# c
# zamienic na hexa wynik xorowania
r = 24
p = 11 # wylosoana liczba
q = 23 #  wylosowana liczba
a = 97 #  losowo wybrana liczba naturalna NWD(a,n) = 1
s = a
n = (p*q)

table = []
def rec(a,i):
    if(i <= r):
        temp = (a**2)%n
        table.append(temp)
        a = temp
        i+=1
        return rec(a,i)

rec(a,0)
table = table[0:len(table)]
table_k =[]

def decimalToBinary(n):
    return '{:0>8}'.format(str(bin(int(n)))[2:])


def is_od(table_x):
    for i in range(1,len(table)):
        if(table_x[i] % 2 == 1):
            table_k.append(1)
        elif(table_x[i] % 2 == 0):
            table_k.append(0)
print("x1-x24: "+str(table))
is_od(table)
print()
table_k = list(table_k)
print("k1-k24: "+str(table_k))
k_hex_1 = ''.join(str(e) for e in table_k[0:8])
k_hex_2 = ''.join(str(e) for e in table_k[8:16])
k_hex_3 = ''.join(str(e) for e in table_k[16:24])
print()
print("k1-k24(HEX):  "+str(hex(int(str(k_hex_1), 2)))[2:].upper()+"  "+str(hex(int(str(k_hex_2), 2)))[2:].upper()+"  "+str(hex(int(str(k_hex_3), 2)))[2:].upper())



compare_string = decimalToBinary(ord("W"))+decimalToBinary(ord("S"))+decimalToBinary(ord("B"))



compare_string = list(compare_string)

c_list = []
print("debuug")
for i in range(0,24):
    print(table_k[i])
    print(compare_string[i])

    result = int(table_k[i]) ^ int(compare_string[i])
    print(result)
    c_list.append(result)
print("debuug")
print("WSB w UTF-8: "+str(compare_string))
print("c1-c24:  "+str(c_list))

c1_hex = str(c_list[0])
c2_hex = ""
c3_hex = ""

for i in c_list[0:7]:
    c1_hex += str(c_list[i])

for i in c_list[8:16]:
    c2_hex += str(c_list[i])

for i in c_list[16:24]:
    c3_hex += str(c_list[i])
print(c1_hex)
print(c2_hex)
print(c3_hex)

print(str(hex(int(str(c1_hex), 2)))[2:].upper())
print(str(hex(int(str(c2_hex), 2)))[2:].upper())
print(str(hex(int(str(c3_hex), 2)))[2:].upper())
