#write a python program to print sum of even palindromes in a a range and also print list of palindromes
def palindrome(n):
   s=str(n)
   if s==s[::-1]:
       return 1
   else:
       return 0
n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)#flag is a variable.It indicates the status of the given method
    if flag==1:
       l1.append(i)
    if n%2==0:
        if flag==1:
           l2.append(i)
print(l1)
print(sum(l1))

