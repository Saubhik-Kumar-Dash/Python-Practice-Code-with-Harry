"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} who is a {self.breed} says WOOF WOOF !!")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()    
"""

    
"""
1.Create a class “Programmer” for storing information of few programmers working at Microsoft.

2.Write a class “Calculator” capable of finding square, cube and square root of a number.

3.Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

4.Add a static method in problem 2, to greet the user with hello.

5.Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

6.Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
""" 

#1
"""
class Programmer:
    def __init__(self, name, age, designation, salary):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        
    def employee(self):
        print(f"***Microsoft Programmer***")
        print(f"Name: {self.name} \nAge: {self.age} \nDesignation: {self.designation} \nSalary(per annum): {self.salary}")

a = input("Enter your name: ")
b = int(input("Enter your Age: "))
c = input("Enter your Designation in the Office: ")
d = int(input("Enter your Salary in per annum: "))

ms_prog = Programmer(a, b, c, d)
ms_prog.employee()
""" 

"""
class Programmer:
    company = "Microsoft"
    def __init__(self, name, add_pin, salary):
        self.name = name
        self.add_pin = add_pin
        self.salary = salary

p = Programmer("Roshan", 800023, 1200000)
print(p.name, p.add_pin, p.salary)
""" 

#2
"""
class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square is: {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}")
    
    def sq_root(self):
        print(f"The square root is: {self.n ** 1/2 }")

a = Calculator(int(input("Enter the Number whose square, cube, square root you want: ")))
a.square()
a.cube()
a.sq_root()
""" 

#3
"""
class Demo:
     a = 4

o = Demo()
print(o.a)
o.a = 0
print(o.a)
print(Demo.a)
""" 

#4
"""
class Calculator:
    def __init__(self, n):
        self.n = n
    
    @staticmethod
    def greet():
        print("Hello there")
    
    def square(self):
        print(f"The square is: {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}")
    
    def sq_root(self):
        print(f"The square root is: {self.n ** 1/2 }")

a = Calculator(int(input("Enter the Number whose square, cube, square root you want: ")))
a.greet()
a.square()
a.cube()
a.sq_root()
""" 

#5
"""
import random
# from random import randint
class Train:
    def __init__(self, train_no):
        self.train_no = train_no
    
    def book_ticket(self, dep, arr): 
        print(f"Ticket is booked in train no: {self.train_no}")
        print(f"Train Departure: {dep}")
        print(f"Train Arrival: {arr}")
    
    def getStatus(self, dep, arr):
        print(f"Train no: {self.train_no} is running successfully")
        print(f"Train Departure: {dep}")
        print(f"Train Arrival: {arr}")
         
    def getFare(self):
        print(f"Ticket Fare of train no:{self.train_no} is {random.randint(110, 2500)}")


t = Train(12399)
t.book_ticket("Patna", "Delhi")
t.getStatus("Patna", "Delhi")
t.getFare()
""" 

#6
import random
# from random import randint
class Train:
    def __init__(slf, train_no):
        slf.train_no = train_no
    
    def book_ticket(self, dep, arr): 
        print(f"Ticket is booked in train no: {self.train_no}")
        print(f"Train Departure: {dep}")
        print(f"Train Arrival: {arr}")
    
    def getStatus(self, dep, arr):
        print(f"Train no: {self.train_no} is running successfully")
        print(f"Train Departure: {dep}")
        print(f"Train Arrival: {arr}")
         
    def getFare(self):
        print(f"Ticket Fare of train no:{self.train_no} is {random.randint(110, 2500)}")


t = Train(12399)
t.book_ticket("Patna", "Delhi")
t.getStatus("Patna", "Delhi")
t.getFare()

"""changing the self-parameter inside a class 
to something else doesn't affect the program output"""