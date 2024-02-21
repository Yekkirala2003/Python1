a,b,c,d=map(int,input().split(" "))
e=a-a*c//100
f=b-b*d//100
if e<f:
    print("first")
elif e>f:
    print("second")
else:
    print("any")
