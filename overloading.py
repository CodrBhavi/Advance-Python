class Test:
    def m1(self):
        print("one method")
    def m1(self,a):
        print("second method")
    def m1(self,a,b):
        print("third method")

t = Test()
t.m1(10,20)
''' Note: Method Overloading is not possible in Python because if you take
          same name function with different arguments python will only 
          select last one '''
          