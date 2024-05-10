#a sm having 5%discount for men and 7%discount for women and individual discount each item they purchase is (3*no.of items they purchase)% calculate the total billd={}
d={}
n=int(input("enter no of items: "))
for i in range(n):
    item=input("item: ")
    price=int(input("price: "))
    d[item]=price
l=[]
for i in d:
         l.append(d[i]-d[i]*(3*n)/100)
g=input("Enter Gender: ")    
if g == "male":
       bill=sum(l)-sum(l)*5/100
else:
     bill=sum(l)-sum(l)*7/100
j=0
print("items - prices:discount-prices")
for i in d:
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"total bill:{bill}")
