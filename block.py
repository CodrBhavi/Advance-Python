# Exception Handling
import sys
def linux_interaction():
    assert('linux' in sys.platform), 'Function can only run on linux system'
    print("Do someting")
try:
    linux_interaction()
except:
    print("Linux Function was not executed")
try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("The linux_interaction function was not executed")
