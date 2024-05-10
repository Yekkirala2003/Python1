#product of elements inside the matrix
r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
p=1
for i in l:
    print(i)
    for j in i:
      p=p*j
print(p)
    
    
            
