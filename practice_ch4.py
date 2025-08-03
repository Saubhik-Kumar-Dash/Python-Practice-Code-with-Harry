"""
1.Write a program to store seven fruits in a list entered by the user.
2.Write a program to accept marks of 6 students and display them in a sorted manner.
3.Check that a tuple type cannot be changed in python.
4.Write a program to sum a list with 4 numbers.
5.Write a program to count the number of zeros in the following tuple:
        a = (7, 0, 8, 0, 0, 9)
"""

#1
"""
f = []
for i in range(1,8):
    fruits = input(f"Enter the Fruits Name {i}: ")
    f.append(fruits)

print(f)
"""

"""
fruits = []

f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)

print(fruits)
"""

#2
"""
marks = []

for i in range(1,7):
    m = int(input(f"Enter the Student's Marks {i}/6: "))
    marks.append(m)

marks.sort()
print(marks)
# print(marks.sort())     # this shows error as: You're asking Python to print the return value of sort(), which is None.
"""

#3
"""
tup = (1,5,3,4,2)

print(type(tup))
#tup.insert(6)
tup.sort()
print(tup)      # throws => AttributeError: 'tuple' object has no attribute 'sort' or 'insert'
"""

#4
"""
l = [1, 5, 8, 15]

print(sum(l))
"""

#5
"""
a = (7, 0, 8, 0, 0, 9)

n = a.count(0)
print(n)
"""