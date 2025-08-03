"""
1.Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

2.The game() function in a program lets a user play a game and returns the score as an integer. 
  You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
  You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

3.Write a program to generate multiplication tables from 2 to 20 and write it to the different files. 
  Place these files in a folder for a 13 – year old.

4.A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

5.Repeat program 4 for a list of such words to be censored.

6.Write a program to mine a log file and find out whether it contains ‘python’.

7.Write a program to find out the line number where python is present from ques 6.

8.Write a program to make a copy of a text file “this. txt”

9.Write a program to find out whether a file is identical & matches the content of another file.

10.Write a program to wipe out the content of a file using python.

11.Write a python program to rename a file to “renamed_by_ python.txt.
"""

#1
"""
f = open("poems.txt", "r")
text = f.readline()

if "twinkle" in text:
    print("Yes, twinkle is present")
else:
    print("No, twinkle is not present")
f.close()
"""

#2
"""
import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)   # generating my score randomly
    
    # fetch hiscore from file as an int
    with open("Hi-score.txt") as f:
        hiscore = f.read()
        # if file is not empty, take that as an hiscore and convert it into int
        if hiscore != "":
            hiscore = int(hiscore) 
        else:
            hiscore = 0     # if file is empty, hiscore = 0
                
    print(f"Your score: {score}")
    # if generated score is higher, write that in the file (not append)
    if score > hiscore:
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))     # write can only happen if value is in str
    
    return score
        
game()
""" 

#3
"""
def generateTable(n):
    #  empty string table used to accumulate the lines of the multiplication table as a single string.
    table = ""  
        
    # generate the multiplication table, Each line of the multiplication table is created
    # string is appended to the table string using +=.
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    # opens (or creates) a text file using with open(...),  file path is "table_2_to_25/table_{n}.txt"
    with open(f"table_2_to_25/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 25):
    generateTable(i)
""" 

#4 #5
"""
words = ["Donkey", "bad", "ganda"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:    
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)
""" 

#6 #7
"""
lineno = 1
with open("log.txt") as f:
    line = f.readlines()
for i in line:
    if "python" in i:
        print(f"Yes! python is present in line no.: {lineno}")
        break
    lineno += 1
    
else:
    print("Nope! python is not present")
""" 

#8
"""
with open("file.txt") as f:
    content = f.read()

with open("file2.txt", "w") as f:
    f.write(content)
""" 

#9 
"""
with open("file.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Files are identical")
else:
    print("Not Identical")
""" 

#10
"""
with open("file2.txt", "w") as f:
    f.write("")
""" 

#11
with open("f1.txt") as f:
    c = f.read()
    
with open("renamed_by_ python.txt", "w") as f:
    c = f.write(c)