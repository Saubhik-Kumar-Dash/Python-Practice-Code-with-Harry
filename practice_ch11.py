"""class Employee:
    company = "ITC"
    def show(self):
        print(f"Name: {self.name} and Salary: {self.salary}")
        
        
# class Programmer:
#     def show(self):
#         print(f"Name: {self.name} and Salary: {self.salary}")
    
#     def showLanguage(self):
#         print(f"Name: {self.name} and Language: {self.language} ")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"Name: {self.name} and Language: {self.language} ")


a = Employee()
b = Programmer()

print(a.company, b.company)"""


# class Employee:
#     a = 1
#     @classmethod    # decorator
#     def show(cls):
#         print(f"The class attribute: {cls.a}")

# e = Employee()
# e.a = 45    # instance attribute
# e.show()    # show class attribute

# class Number:
#     def __init__(self, n):
#         self.n = n
    
#     # def __add__(self, num):
#     #     return self.n + num.n

# n = Number(1)
# m = Number(2)

# print(n+m)

"""
1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

3. Create a class ‘Employee’ and add salary and increment properties to it.
   Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

6. Write __str__() method to print the vector as follows: 7i + 8j +10k
   Assume vector of dimension 3 for this problem.

7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.
"""

#1
"""
class Vector_2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
        
class Vector_3D(Vector_2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


o = Vector_2D(1, 2)
o2 = Vector_3D(4, 3, 3)

o.show()
o2.show()
""" 

#2
"""
class Animals:
    def __init__(self):
        print("Animals")

class Pets(Animals):
    def __init__(self):
        print("Pets")

class Dog(Pets):
    
    @staticmethod
    def bark():
        print("Woof Woof Bow Bow!!")

a = Dog()
a.bark()

Pets()

Animals()
"""  

#3
# class Employee:
#     salary = 200
#     increment = 20
    
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @increment.setter
#     def increment(self, salary):
#         self.increment = ((salary/self.salary) - 1)*100

# o = Employee()
# # print(o.salaryAfterIncrement)

"""
class Employee:
    salary = 200
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

o = Employee()
o.salaryAfterIncrement = 280
print(o.increment)  # Output: 40.0
"""

#4
"""
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
"""  

#5
"""
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50
""" 

#6
"""
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50
""" 

#7
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"
    
    def __len__(self):
        return 3

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50

print(len(v1))
