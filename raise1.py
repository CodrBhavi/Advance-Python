# Raise Statement in Exception Handling
try:
    a = 10
    print(a/0)
    raise ZeroDivisionError("Can't Divde by Zero")
except ZeroDivisionError:
    print("An Exception")
    raise # To determine whether the exception was raised or not
