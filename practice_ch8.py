"""
1.Write a program using functions to find greatest of three numbers.

2.Write a python program using function to convert Celsius to Fahrenheit.

3.How do you prevent a python print() function to print a new line at the end.

4.Write a recursive function to calculate the sum of first n natural numbers.

5.Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
6.Write a python function which converts inches to cms.

7.Write a python function to remove a given word from a list ad strip it at the same time.

8.Write a python function to print multiplication table of a given number.
"""

#1
"""
def max_num():
    num = []
    for i in range(3):
        a = int(input("Enter the Number: "))
        num.append(a)
    return max(num)
  
print(max_num())
"""

#2
# °F = (°C * 1.8) + 32
"""
def conv():
    c = int(input("Enter temperature in Celsius: "))
    f = (c * 1.8) + 32
    
    return f

print(conv())
"""

#3
"""
print("a")
print("a")
print("c", end="")
print("d", end="")
"""

#4
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(f"Factorial of {num} is =", factorial(num))
"""

"""
def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

num = int(input("Enter the Number: "))
print(f"Sum of 1st {num} numbers is =",sum(num))
""" 

#5
"""def star(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print("\r")

a = int(input("Enter the number: "))
star(a)
""" 

"""def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)

pattern(5)
"""

#6
"""
def conv():
    inch = int(input("Enter the length in Inches: "))
    cm = inch * 2.54
    
    return cm

print(conv())
""" 

#7
"""
def strip(l, word):
    n = []
    for item in l:
        if not item == word:
            n.append(item.strip(word))
    return n

l = ["Hari", "Rohan", "Harry", "an"]
print(strip(l, "an"))
""" 

#8
def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

table(int(input("Enter the number you want a table: ")))

