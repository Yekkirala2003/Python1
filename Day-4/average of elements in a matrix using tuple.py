#write a python program to find the average of elements in matrix using tuple
r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
print(tuple(l))
for i in  l:
    for j in i:
        sum+=j
print(sum/(r*c))
