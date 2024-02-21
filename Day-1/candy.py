n,c=map(int,input().split(" "))
if c>=n:
    np=0
else:
    d=n-c
    if d%4==0:
        np=d//4
    else:
        np=(d//4)+1
print(np)
