a,b=map(float,input().split(" "))
if a%5==0:
   if a<b:
       print(b-a)
   else:
      print(b)
else:
    print(b)
