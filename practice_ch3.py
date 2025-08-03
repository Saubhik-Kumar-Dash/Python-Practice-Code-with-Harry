"""
1.Write a python program to display a user entered name followed by Good Afternoon using input () function.
2.Write a program to fill in a letter template given below with name and date.
            letter = ''' 
            Dear <|Name|>, 
            You are selected! 
            <|Date|> 
            '''
3.Write a program to detect double space in a string.
4.Replace the double space from problem 3 with single spaces.
5.Write a program to format the following letter using escape sequence characters.
            letter = "Dear Harry, this python course is nice. Thanks!"
"""

#1
"""
msg = input("Enter your name: ")
print(f"{msg} Good Afternoon")
"""

#2
"""
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>", "Baba").replace("<|Date|>", "24 june 2025"))
"""
            
#3
"""
name = "Baba is is a  Monster"

print(name.find("  "))
"""

#4
"""
name = "Baba is a  Monster "

print(name.replace("  ", " "))  # this creates an new string
print(name)     # returns the same name string ; Strings are immutable
"""

#5
letter = "Dear Harry, this python course is nice. Thanks!"
letter2 = "Dear Harry,\n\tThis python course is nice. \nThanks!"
print(letter)
print(letter2)