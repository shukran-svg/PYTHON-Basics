# oop

# properties + functions = methods
# class is a blueprint for creating objects,
#book title,price,isbn

class Book:
    #constructor == function
    def __init__(self, book_name, price, isbn):
          self.title = book_name
          self.price = price
          self.isbn = isbn
    def print_details(self):
        print("Title" ,self.title)
        print("Price"  ,self.price)
        print("ISBN" ,self.isbn)
        print("--------------")
    def apply_discount(self, discount):
        self.price = self.price * (1 - discount/100)

        print ("Discount applied/New price is. New price: ", self.price)


b1 = Book("Python Programming", 100, "1234567890")
b2 = Book("Java Programming", 150, "0987654321")
b1.apply_discount(10)
b1.print_details()
b2.print_details()
print(b1, b1.title, b1.price, b1.isbn)
print(b2, b2.title, b2.price, b2.isbn)


#variable created from a class data+ functions
