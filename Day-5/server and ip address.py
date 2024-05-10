d= {}
n,m=map(int,input().split())#n=no of i/p,m=search items
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
for i in range(m):
    k1,v1=map(str,input().split())#k1=main,v1=ip address
    for i in d:
        if d[i] == v1[:-1]:#to remove semicolon which is given in test cases.for searching.comparing dictionary value and searching value
            print(f"{k} {v1} #(i)")
