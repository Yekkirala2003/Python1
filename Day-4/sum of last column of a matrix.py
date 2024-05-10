#write a python program to print sum of the last column in matrix
r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
print(tuple(l))
for i in  l:
    sum+=i[c-1]
print(sum)

