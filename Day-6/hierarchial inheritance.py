class A:
    def hi(self):
        print("hello1")
class B(A):
    def __init__(self):
        print("hello2")
class C(A):
    def __init__(self):
        print("hello3")
obj1=B()
obj1.hi()
obj2=C()
obj2.hi()


