r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)
      


