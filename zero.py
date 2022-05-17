# Program to Handle NameError
try:
    print("Value of b = ",b)
except NameError:
    print("NameError Handled")
finally:
    print("Code Run Sucessfully")

