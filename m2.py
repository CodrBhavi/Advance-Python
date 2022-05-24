# Method Overriding
class Shape:
    data1 = "abc"
    def no_of_sides(self):
        print("My sides needed to be defined. I am from Shape Class")
    
    def two_dimensional(self):
        print("I am a 2D Object. I am from Shape Class")

class Square(Shape):
    data2 = "XYZ"
    def no_of_sides(self):
        print("I am a Square and I have 4 sides. I am from Square Class")

    def color(self):
        print("I have a Blue Color. I am from Square Class")

sq = Square()

sq.no_of_sides()
sq.two_dimensional()
sq.color()