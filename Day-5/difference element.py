l,d=map(int,input().split(" "))
l1=list(map(int,input().split()))
for i in l1:
    for j in l1 :
     if i-j==d:
         flag=1
if flag==1:
    print("True")
else:
   print("false")
    
    
