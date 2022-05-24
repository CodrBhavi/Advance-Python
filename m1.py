# Method Overloading
from multipledispatch import dispatch

@dispatch(int,int)
def num(first,second):
    result = first + second
    print(result)

@dispatch(int,int,int)
def num(first,second,third):
    result = first + second * third
    print(result)

@dispatch(str,str,str,str,str)
def num(first,second,third,fourth,fifth):
    result = first + second + third + fourth + fifth    
    print(result)

num(95,5)
num(10,2,4)
num("Python ","is ","easy ","to ","Learn")
