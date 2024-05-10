#write a python program to make encryption and decryption with a key value using functions
def encrypt(s,k):
    s1=""
    for i in s:
        x=ord(i)+k
        s1+=chr(x)
    print(s1)
def decrypt(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)
    print(s1)
k=int(input("enter the key value:"))
s=input("enter string:")
o=input("select operation:")
if o =="encrypt":
  encrypt(s,k)
elif o=="decrypt":
    decrypt(s,k)
else:
  print("error")
        
