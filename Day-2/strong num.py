#program to find whether the given number is strong or not(145=1!+4!+5!=145)
def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        return "strong number"
    else:
        return"not a strong number"
n=int(input())
print(strong(n))
