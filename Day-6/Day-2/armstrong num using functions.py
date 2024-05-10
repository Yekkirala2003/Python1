#write a python program to print a armstrong number in a range using functions
def armstrong(n,m):
 for i in range(n,m+1):#100-1001
  sum=0
  x=i#100=101
  while i>0:
     temp=i%10
     sum+=temp**3
     i//=10
  if sum == x:#1==100,2=101
         print(x)
n,m=int(input()),int(input())#100-1000
armstrong(n,m)
