# Creating a Phone Class
class Phone:
    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("I am making a Call")
    def play_game(self):
        print("I am playing a Game")

# Creating an object of Phone Class
# p1 = Phone()

# # Calling the Functions of Phone Class
# p1.make_call()

# p1.play_game()

# Creating a second object of Phone Class
p2 = Phone()
# Calling the New Features of Phone Class
p2.set_color("Green")

p2.set_cost(5000)

print(p2.show_color())

print(p2.show_cost())

