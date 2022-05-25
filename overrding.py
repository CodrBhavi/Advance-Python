# Method Overrding
class Parent:
    def property(self):
        print("Cash + Gold + Land")
    def marry(self):
        print("Laxmibai")

class Child(Parent):
    def marry(self):
        print("Kriti Sanon")

ch1 = Child()
ch1.property()
ch1.marry()
