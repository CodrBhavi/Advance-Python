# Program to Handle multiple errors with one except statement
def fun(a):
    if a < 4:

        # Throws ZeroDivisionError for a = 3
        b = a/(a-3)

    # throws NameError if a >= 4
    print("Value of b = ",b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError occured and Handled")
except NameError:
    print("NameError occured and Handled")
