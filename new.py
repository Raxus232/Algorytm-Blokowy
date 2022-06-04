import math

message = int(input("Enter the message to be encrypted: "))

p = 107
q = 293
e = 67

n = p*q

def encrypt(me):
    en = math.pow(me,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c

print("Original Message is: ", message)
c = encrypt(message)
