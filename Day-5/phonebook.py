#phone book and numbers
n=int(input())
d={}
for i in range(n):
    key=input("key: ")
    value=input("value: ")
    d[key]=value
m=int(input("No of search items: "))
for i in range(m):
    s=input()
    if s in d:
        print(s,d[s])
    else:
        print("not found")
