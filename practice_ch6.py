"""a = int(input("Enter the age: "))

if a >= 18:
    print("You are above age of consent")
    
else:
    print("You are below age of consent")
"""
"""
1.Write a program to find the greatest of four numbers entered by the user.

2.Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

3.A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

4.Write a program to find whether a given username contains less than 10 characters or not.

5.Write a program which finds out whether a given name is present in a list or not.

6.Write a program to calculate the grade of a student from his marks from the following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F

7.Write a program to find out whether a given post is talking about “Harry” or not.
"""

#1
"""
num = []
for i in range(4):
    a = int(input("Enter the Number: "))
    num.append(a)
max = max(num)
print(max)
"""

#2
"""
m1 = int(input("Enter the Marks 1: "))
m2 = int(input("Enter the Marks 2: "))
m3 = int(input("Enter the Marks 3: "))

total_percentage = (100 * (m1 + m2 + m3)) / 300

if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Marks received: ")
    print(f"{m1} / 100")
    print(f"{m2} / 100")
    print(f"{m3} / 100")
    print("Total Percentage =", round(total_percentage, 2))
    print("You passed the Exam!")
else:
    print("Marks received: ")
    print(f"{m1} / 100")
    print(f"{m2} / 100")
    print(f"{m3} / 100")
    print("Total Percentage =", round(total_percentage, 2))
    print("You failed the Exam!")
"""

#3
"""
w = input("Enter any Word: ")

# check the words: “Make a lot of money”, “buy now”, “subscribe this”, “click this”

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

if (p1 in w) or (p2 in w) or (p3 in w) or (p4 in w):
    print("You entered the SPAM phrases!")
else:
    print("Thank you for Input")
"""

#4
"""
name = input("Enter username: ")

if len(name) < 10:
    print("username contains less than 10 characters")
else: 
    print("Thank you")
"""

#5
"""
l = ['ali', 'harry', 'sam', 'pinku', 'donald']

name = input("Enter Name: ")

if name in l:
    print("you are in the list")
else:
    print("you are not in the list")
"""

#6
"""
marks = int(input("Enter the Marks: "))

if marks <= 100 and marks >= 90:
    grade = "Ex"
elif marks < 90 and marks >= 80:
    grade = "A"
elif marks < 80 and marks >= 70:
    grade = "B"
elif marks < 70 and marks >= 60:
    grade = "C"
elif marks < 60 and marks >= 50:
    grade = "D"
elif marks < 50:
    grade = "F"

print("Your grade is:",grade)
"""

#7
post = input("Enter your post: ")

if 'baba' in post.lower():
    print("Post is talking about baba")
else:
    print("Post is not talking about baba")