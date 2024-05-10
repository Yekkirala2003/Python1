#to print factorial of a given number using class and methouds and recursion
class f:
   def __
   init__(self,data):
      self.data=data
      print(self.find_fact())
   def find_fact(self):
      return self.fact(self.data)
   def fact(self,n):
      if n<1:
           return 1
      else:
           return n*self.fact(n-1)#to use recursion in python we use helping function in python
obj=f(int(input()))
