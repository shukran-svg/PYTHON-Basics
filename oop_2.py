#
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def print_details(self):
        print("Radius:", self.radius)
        print("Area:", self.get_area())
        print("perimeter:", self.get_perimeter())

c1 = Circle(5)
c2 = Circle(10)

c1.print_details()
print(c1.get_perimeter())
# copy branch
# push
# Raise pull request
# accept == merge
# deploy ==server

#TODO
