
def split(inp):
    assert len(inp)%2==0
    return inp[:int(len(inp)/2)], inp[int(len(inp)/2):]
def RL1(input):

    Lfirst = input[0 : 1]
    Lsecond = input[1 :]
    return (Lsecond + Lfirst)
def choose_key(k):
    key_list = []
    for i in range (0,len(k)):
            if i % 2 == 0:
                key_list.append(k[i])
    return key_list


def gen_keys(key):
    key = split(key)
    k1=RL1(key[0])+RL1(key[1])
    #print(k1)
    K1="".join(choose_key(k1))


    k2=RL1(k1)
    K2="".join(choose_key(k2))


    k3=RL1(k2)
    K3="".join(choose_key(k3))


    k4=RL1(k3)
    K4="".join(choose_key(k4))

    k5=RL1(k4)
    K5="".join(choose_key(k5))

    k6=RL1(k5)
    K6="".join(choose_key(k6))

    k7=RL1(k6)
    K7="".join(choose_key(k7))

    k8=RL1(k7)
    K8="".join(choose_key(k8))
    return [K1,K2,K3,K4,K5,K6,K7,K8]

key = "10110001"
#key = str(input("Podaj tekst jawny: ")) #wprowadzanie zmiennej
plainText = "01111000"
plainText = split(plainText)

key_list = gen_keys(key)
#print(key_list)
#print(key_list[0][:1]) # przyda sie
print plainText;

x1 = int(plainText[1][0])
x2 = int(plainText[1][1])
x3 = int(plainText[1][2])
x4 = int(plainText[1][3])

k1 = int(key_list[0][0])
k2 = int(key_list[0][1])
k3 = int(key_list[0][2])
k4 = int(key_list[0][3])
print(plainText[1])
result1 = x1 ^ (x1 and x3) ^ (x2 and x4) ^ (x2 and x3 and x4) ^ (x1 and x2 and x3 and x4) ^k1
result2 = x2 ^ (x1 and x3) ^ (x1 and x2 and x4) ^ (x1 and x2 and x3 and x4) ^ k2
result3 = 1 ^ x3 ^ (x1 and x4) ^ (x1 and x2 and x4) ^ (x1 and x2 and x3 and x4) ^ k3
result4 = 1 ^ (x1 and x2) ^ (x3 and x4) ^ (x1 and x2 and x4) ^ (x1 and x3 and x4) ^ (x1 and x2 and x3 and x4) ^ k4
L1=plainText[0]
R1 = str(result1)+str(result2)+str(result3)+str(result4)
print(L1)
print(R1)
print(int(L1)^int(R1))
print("eee")
