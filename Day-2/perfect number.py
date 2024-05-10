#write a python program to check whther the given num is perfect or not
n=int(input())
c=0
for i in range(1,n):
    if n%i==0:
        c=c+i
if c==n:
    print("perfect number")
else:
    print("not a perfect number")
