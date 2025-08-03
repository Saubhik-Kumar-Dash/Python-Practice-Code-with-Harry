# advanced python

"""Walrus operator"""
# n = len([1, 2, 3, 4, 5])
# if n > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)")


# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)")


"""type definition"""
# n : int = 5

# a : str = "life is a struggle"
# print(type(n))
# print(n.bit_length())

# print(type(a))
# print(a.upper())


"""match case"""
# def http_status(status): 
#     match status:  
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"  


# print(http_status(200))
# print(http_status(5007))
# print(http_status(500))
# print(http_status(403))


"""
1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

2. Write a program to print third, fifth and seventh element from a list using enumerate function.

3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
""" 

#1
# #if any file is not present
# try:
#     a = open("1.txt", "r")
#     text = a.readline()

#     b = open("2.txt", "r")
#     text = a.readline()

#     c = open("3.txt", "r")
#     text = a.readline()
    
# except FileNotFoundError:
#     print("File not found")

# print("Thank You!")

# #if anyone of the file is present

# try:
#     with open("1.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("2.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("3.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)


# print("Thank You!")

#2
"""
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)
""" 

#3
"""
n = int(input("Enter the number: "))

table = [n*i for i in range(1, 11)]
print(table)
""" 

#4
try:
    a = int(input("enter num a: "))
    b = int(input("enter num b: "))
    print(f"division is: {a/b}")
    
except ZeroDivisionError:    
   print("Infinite")
