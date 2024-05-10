#write a  program to print n natural numbers using recursion
def printing(n):
   if n<1:
       return 1
   else:
        return n+printing(n-1)
        print(n)
n=int(input())
printing(n)
