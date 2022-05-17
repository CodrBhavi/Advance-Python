# AssertionError Program in Python
try:
    x = 0
    y = 0
    assert y!=0, "Invalid Operation"
    print(x/y)
except AssertionError as msg:
    print(msg)
    