# Creating a Student's Constructor Class
class Student:
    def __init__(self,name,stu_class,rollno,fav_sub):        
        self.name = name
        self.stu_class = stu_class
        self.rollno = rollno
        self.fav_sub = fav_sub

    def show_student_details(self):
        print("Student Name:",self.name)
        print("Student Class:",self.stu_class)
        print("Student Roll no.",self.rollno)
        print("Student Favourite Subject:",self.fav_sub)

s1 = Student("Bhavam",9,13,"Maths")

s1.show_student_details()

