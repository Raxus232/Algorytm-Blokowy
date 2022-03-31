
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

    K1="".join(choose_key(k1))

    k2=RL1(k1)
    K2="".join(choose_key(k2))


    k3=RL1(k2[0:4])+RL1(k2[4:8])
    K3="".join(choose_key(k3))


    k4=RL1(k3)
    K4="".join(choose_key(k4))

    k5=RL1(k4[0:4])+RL1(k4[4:8])
    K5="".join(choose_key(k5))

    k6=RL1(k5)
    K6="".join(choose_key(k6))

    k7=RL1(k6[0:4])+RL1(k6[4:8])
    K7="".join(choose_key(k7))

    k8=RL1(k7)
    K8="".join(choose_key(k8))
    return [K1,K2,K3,K4,K5,K6,K7,K8]

def mix(key,plainText,round):
    plainText = split(plainText)

    key_list = gen_keys(key)

    x1 = int(plainText[1][0])
    x2 = int(plainText[1][1])
    x3 = int(plainText[1][2])
    x4 = int(plainText[1][3])
    if(round == 1):
        k1 = int(key_list[0][0])
        k2 = int(key_list[0][1])
        k3 = int(key_list[0][2])
        k4 = int(key_list[0][3])
    if(round == 2):
        k1 = int(key_list[1][0])
        k2 = int(key_list[1][1])
        k3 = int(key_list[1][2])
        k4 = int(key_list[1][3])
    if(round == 3):
        k1 = int(key_list[2][0])
        k2 = int(key_list[2][1])
        k3 = int(key_list[2][2])
        k4 = int(key_list[2][3])
    if(round == 4):
        k1 = int(key_list[3][0])
        k2 = int(key_list[3][1])
        k3 = int(key_list[3][2])
        k4 = int(key_list[3][3])
    if(round == 5):
        k1 = int(key_list[4][0])
        k2 = int(key_list[4][1])
        k3 = int(key_list[4][2])
        k4 = int(key_list[4][3])
    if(round == 6):
        k1 = int(key_list[5][0])
        k2 = int(key_list[5][1])
        k3 = int(key_list[5][2])
        k4 = int(key_list[5][3])
    if(round == 7):
        k1 = int(key_list[6][0])
        k2 = int(key_list[6][1])
        k3 = int(key_list[6][2])
        k4 = int(key_list[6][3])
    if(round == 8):
        k1 = int(key_list[7][0])
        k2 = int(key_list[7][1])
        k3 = int(key_list[7][2])
        k4 = int(key_list[7][3])

    result1 = x1 ^ (x1 and x3) ^ (x2 and x4) ^ (x2 and x3 and x4) ^ (x1 and x2 and x3 and x4) ^k1
    result2 = x2 ^ (x1 and x3) ^ (x1 and x2 and x4) ^ (x1 and x3 and x4) ^(x1 and x2 and x3 and x4) ^ k2
    result3 = 1 ^ x3 ^ (x1 and x4) ^ (x1 and x2 and x4) ^ (x1 and x2 and x3 and x4) ^ k3
    result4 = 1 ^ (x1 and x2) ^ (x3 and x4) ^ (x1 and x2 and x4) ^ (x1 and x3 and x4) ^ (x1 and x2 and x3 and x4) ^ k4
    L1=plainText[0]
    R1= plainText[1]
    sBlok = str(result1)+str(result2)+str(result3)+str(result4)

    B1 = str(int(L1[0]) ^ int(sBlok[0]))+str(int(L1[1]) ^ int(sBlok[1]))+str(int(L1[2]) ^ int(sBlok[2]))+str(int(L1[3]) ^ int(sBlok[3]))
    print("Runda: "+ str(round))
    print("x1: "+ str(x1))
    print("x2: "+ str(x2))
    print("x3: "+ str(x3))
    print("x4: "+ str(x4))

    print("L: " + str(L1))
    print("R: " + str(R1))
    print("SBLOK: " + str(sBlok))
    print("XOR: " + str(B1))
    #return B1+L1
    return R1+B1

def decimalToBinary(n):
    return str(bin(n).replace("0b",""))

def binaryToDecimal(n):
    return str(int(n,2))

def cipher(key,plainText):
    R1 = mix(key,plainText,1)
    R2 = mix(key,R1,2)
    R3 = mix(key,R2,3)
    R4 = mix(key,R3,4)
    R5 = mix(key,R4,5)
    R6 = mix(key,R5,6)
    R7 = mix(key,R6,7)
    R8 = mix(key,R7,8)
    R8 = str(R8[4:8])+str(R8[0:4])
    return R1,R2,R3,R4,R5,R6,R7,R8
    #return R8

def encipher(key,plainText):
    R1 = mix(key,plainText,8)
    R2 = mix(key,R1,7)
    R3 = mix(key,R2,6)
    R4 = mix(key,R3,5)
    R5 = mix(key,R4,4)
    R6 = mix(key,R5,3)
    R7 = mix(key,R6,2)
    R8 = mix(key,R7,1)
    R8 = str(R8[4:8])+str(R8[0:4])
    return R1,R2,R3,R4,R5,R6,R7,R8
    #return R8


key = "10011101"
plainText = "10010101"


def main():
    key = str(input("Podaj klucz: ")) #wprowadzanie zmiennej
    plainText = str(input("Podaj tekst jawny: ")) #wprowadzanie zmiennej
    if (len(key) != 8):
        print("Klucz musi być być długości 8 bitów")
        quit()
    if (len(plainText) != 8):
        print("Tekst jawny musi być być długości 8 bitów")
        quit()
    print("Szyfrogram to: "+str(cipher(key,plainText)))
def debug():
        #print("Tekst jawny: "+str(plainText))
        #print("Klucz: "+str(key))
        #print("Klucze: "+ str(gen_keys(key)))
        #print("R1-8: "+str(cipher(key,plainText)))
        #dec2bin = binaryToDecimal(str(input("test")))
        #print(dec2bin)
        #input("Nacisnij przycisk aby zakonczyc")
        print("Odszyfrowanie")
        print("R1-8: "+str(encipher("10010101",'10111111')))
        input("Nacisnij przycisk aby zakonczyc")
if __name__ == "__main__":
    #main()
    debug()
