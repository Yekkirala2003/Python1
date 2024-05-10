n,x=map(int,input().split(" "))
d=n*x
if d%4==0:
    ns=d//4
    print(ns)
else:
    ns=(d//4)+1
    print(ns)
    
