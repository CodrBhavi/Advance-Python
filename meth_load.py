# Method Overloading
from multipledispatch import dispatch

@dispatch(int,int)
def product(first,second):
    result = first * second
    print(result);

@dispatch(int,int,int)
def product(first,second,third):
    result = first * second * third
    print(result);

@dispatch(str,str,str)
def product(first,second,third):
    result = first + second + third
    print(result);


product(78,45)
product(3,4,5)
product("I ","am ","Bhavam")