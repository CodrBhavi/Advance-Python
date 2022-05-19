# Creating an Employee's Constructor
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_employee_details(self):
        print("Name of Employee is ",self.name)
        print("Age of Employee is ",self.age)
        print("Salary of Employee is ",self.salary)
        print("Gender of Employee is ",self.gender)

e1 = Employee('Sam',22,100000,'Male')

e1.show_employee_details()
