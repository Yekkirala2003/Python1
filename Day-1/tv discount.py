a,b=map(int,input().split(" "))
c,d=map(int,input().split(" "))
if a-c < b-d:
    print("first")
elif a-c> b-d:
    print("second")
else:
    print("any")
