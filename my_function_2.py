def add(x, y, z):
    return x + y + z


#res = add(10, 20, 30)
#print(res)

def addition(*nums):
   # total = sum(nums)
    total = 0
    for num in nums:
        total = total + num
    return total

# key and word arguments **kwargs
def save(**data):

    with open("values.txt", "w") as file:

        for key, value in data.items():
         file.write(f"{key} = {value}\n")
save(dob='12-02-2000', name= 'Jim' , age='20',color ='Black')

#def some_function(name,*scores,**details):
    #pass
def cylinder(r, h):
    """
    calculate surface area and volume of cylinder
    :parameters:
    radius and height of the cylinder
    :returns: surface area and volume of the cylinder

    """

    v=22/7 * r * r * h
    sa=22/7* r **2 * + 2*22/7*r*h
    return sa, v

surf_area, volume = cylinder(8.5, 12.5)
print(surf_area,volume)

sum([1,2,3])
#lambda functions

def divide(a, b):
    return a / b

divi = lambda x, y: x / y
area_circle = lambda r: 22/7 * r * r
print (divi(45,7))
res=area_circle(5)
print(res)



















#some_function("Jim", 90, 100, 67.88, 89, 56, 78, color = "Black", age = 20, dob = "12/12/2000")


#(age = 20,dob = "12/12/2000",name = "Jim")


#print(addition(9, 10, 100, 67.88, 89, 56, 78))
#print(addition(90, 100))
#data ={"name": "Jim", "age": "20", "dob": "12/12/2000"}
#[123]
#for item in data.items():
# for _,v in data.items():
#print(v)













