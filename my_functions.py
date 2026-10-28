# functions
from sqlite3.dbapi2 import paramstyle


def greet():
    print("Hello,welcome to  Python")
    # use == call
#greet()
#greet()
#greet()

def greeting(user):
    print(f"Hello {user},welcome to  Python")
#greeting("Jim")
#greeting("Jack")
#greeting("Jane")

def area_circle(radius, precision =3):
    a = 22/7 * radius * radius
    result = round(a,precision)
    print(result)


#area_circle(2.9,2)
#area_circle(6.11,0)
#area_circle(8)
#named params
#area_circle(2,2)

def volume_cylinder(r, h):
    v = 22/7 * r * r * h
    return v

print (volume_cylinder(8.5,12.5))
res = volume_cylinder(6,19)
print(round(res))

#params/args



