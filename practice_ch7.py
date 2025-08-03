"""
1.Write a program to print multiplication table of a given number using for loop.

2.Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

3.Attempt problem 1 using while loop.

4.Write a program to find whether a given number is prime or not.

5.Write a program to find the sum of first n natural numbers using while loop.

6.Write a program to calculate the factorial of a given number using for loop.

7.Write a program to print the following star pattern.
  *
 ***
***** for n = 3

8.Write a program to print the following star pattern: 
*
**
*** for n = 3

9.Write a program to print the following star pattern.
* * *
*   * for n = 3
* * *

10.Write a program to print multiplication table of n using for loops in reversed order.
"""

#1
"""
table = int(input("Enter the Number you want Multiplication Table: "))

for i in range(1, 11):
    print(f"{table} X {i} =", table * i)
"""
 
#2
"""
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S"):
        print(f"Hello {name}!")
"""

#3
"""
l = ["Harry", "Soham", "Sachin", "Rahul"]
i = 0

while i < len(l):
    if l[i].startswith("S"):
        print(f"Hello {l[i]}!")
    i += 1

n = int(input("Enter a number: "))
i = 1
while (i < 11):
    print(f"{n} X {i} = {n * i}")
    i+=1
"""

#4
"""
n = int(input("Enter the number to be checked: "))

if n <= 1:
    print(f"{n} is not Prime")
else:
    for i in range(2, n):
        if (n % i) == 0:
            print(f"{n} is not Prime")
            break
    else:
        print(f"{n} is Prime")
"""

#5
#"""
n = int(input("Enter the number: "))

i = 1
sum = 0

while (i <= n):
    sum += i
    i += 1

print(f"Sum of Ist {n} numbers =", sum)
#"""

#6
"""
n = int(input("Enter the number: "))

i = 1
fact = 1

while (i <= n):
    fact *= i
    i += 1

print(f"Factorial of {n} =", fact)
"""

#7
"""
n = int(input("Enter the number: "))
"""

"""  
for n = 3
  *
 ***
*****

for i in range(1, n+1):                 # i represents the current row number, n represent number of rows in the pyramid.
    print(" "* (n-i), end = "")         # print space before star, so it center the star for pyramid
    print("*"* (2*i-1), end = "")       # print stars based on n, 1-1, 2-3, 3-5 etc
    print("")                           #  prints a new line after each row (i.e., moves to the next line).
                                        # print() by default returns new line, we don't want that so we write end = ""
"""


"""
  *
 **
***

for i in range(1, n+1):                 
    print(" "* (n-i), end = "")         
    print("*"* (i), end = "")       
    print("")
"""


#8
"""   
*
**
***

for i in range(1, n+1):                 
    print(" "* (n), end = "")         
    print("*"* (i), end = "")       
    print("")
"""


"""
***
***
***

for i in range(1, n+1):                 
    print("*"* (n), end = "")         
    print(" "* (i), end = "")       
    print("")
"""


#9
"""
* * *
*   * 
* * *

for i in range(1, n+1):               # i represents the current row number.
    if i == 1 or i == n:              # checks whether it’s the first or last row.
        print("*"* (n), end = "")
    else:                             # for middle rows
        print("*", end = "")          # Prints the first star of the row (left border).
        print(" "* (n-2), end = "")   # Prints n - 2 spaces (because we already have a star on the left and will add one on the right).
        print("*", end = "")          # Prints the last star of the row (right border).
    print("")                         # Moves to the next line after printing one row.
"""


"""
*****
 ***
  *

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end = "")
    for k in range(2*i - 1):
        print("*", end = "")         
    print("")
"""

"""
* * * 
* *
*

for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
"""


"""  
  1
 123
12345

for i in range(1, n + 1):
        # Print spaces
    for j in range(n - i):
        print(" ", end="")
        # Print numbers
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print("")
"""


#10
"""
table = int(input("Enter the Number you want Multiplication Table: "))

for i in range(1, 11):
    print(f"{table} X {11 - i} =", table * (11 - i))
"""