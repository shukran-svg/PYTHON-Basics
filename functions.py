#functions
import random
from os import write

import my_functions

with open("data.txt", "w") as file:
 #   file.write("99\n")
 #  file.write("68\n")

    #\n line break
 for temp in range(100):
    x = random.randint(-10,65)
    file.write(str(x)+"\n")

with open("data.txt", "r") as file:
         content = file.read()
         print(content)


         #install
         #use


