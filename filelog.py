# Exception Handling using File Handling
try:
    with open('text.txt') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
