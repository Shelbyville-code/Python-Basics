#Built-in functions/Standard library functions

x= max(67,90,27,5,12)
print("The maximum number is",x)

y=min(60,45,13,25,7,5)
print("The minimum number is",y)

z=pow(2,3)
print("The power of 2 is",z)

#User defined functions
def greeting():
    print("Hello world!")
greeting()#calling a function

def school():
    print("My coding school is eMobilis")
school()

#Parameter and argument
def add(num1,num2):
    print(num1+num2)

add(10,5)
add(35,15)

print()

def student(fullname,course,gender):
    print(fullname,course,gender)

student("Mary Mbotela","MIT","Female")
student("Marty Munich","MIT","Male")
student("Thomas Shelby","MIT","Male")
student("Jack Reacher","MIT","Male")
student("Susan Carter","MIT","Female")

print()

def employees(fullname,email,age,position,salary,marriage):
    print(fullname,email,age,position,salary,marriage)

print("Fintech Employees")
employees("Thomas Shelby","shelby@gmail.com",28,"CEO",524000.00,"Single")
employees("Arthur Shelby","arthur@gmail.com",31,"Managing Director",400000.00,"Married")
employees("Finn Shelby","finn34@gmail.com",26,"Assistant Managing Director",312000.00,"Single")
employees("Elizabeth Harmon","lizzy@gmail.com",28,"Sales Manager",300000.00,"Single")
employees("Jack Reacher","richie@gmail.com",35,"Accountant",2500000.00,"Single")
