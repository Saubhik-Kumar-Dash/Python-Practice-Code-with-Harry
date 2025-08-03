"""
1.Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
2.Write a program to input eight numbers from the user and display all the unique numbers (once).
3.Can we have a set with 18 (int) and '18' (str) as a value in it?
4.What will be the length of following set s: 
        s = set() 
        s.add(20) 
        s.add(20.0) 
        s.add('20') # length of s after these operations?
5.s = {} What is the type of 's'?
6.Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
7.If the names of 2 friends are same; what will happen to the program in problem 6?
8.If languages of two friends are same; what will happen to the program in problem 6?
9.Can you change the values inside a list which is contained in set S? 
        s = {8, 7, 12, "Harry", [1,2]}
"""

#1
"""
translation = {             # key:value pair
    "botal": "bottle",
    "namaste": "hello",
    "sher": "Lion"
}

meaning = input("Enter the word you want meaning of: ")
print(translation)
print(translation[meaning])
print(type(translation))
"""

#2
"""
num = set()     # in sets, no repetition allowed
f1 = input("Enter Number 1: ")
num.add(int(f1))
f2 = input("Enter Number 2: ")
num.add(int(f2))
f3 = input("Enter Number 3: ")
num.add(int(f3))
f4 = input("Enter Number 4: ")
num.add(int(f4))
f5 = input("Enter Number 5: ")
num.add(int(f5))
f6 = input("Enter Number 6: ")
num.add(int(f6))
f7 = input("Enter Number 7: ")
num.add(int(f7))
f8 = input("Enter Number 8: ")
num.add(int(f8))

print(num)  # print only unique values
"""

#3
"""
# we can have a set with 18 (int) and '18' (str) as a value in it
a = {'1', '55', 'abc', 'efg', '4560', 'abcde'} 
a.add(18)       #int
a.add("18")     #str
print(a, type(a))
"""

#4
"""
s = set()  
s.add(20) 
s.add(20.0)     # 20 == 20.0 so both are same
s.add('20')
print(s)        # len = 2
"""

#5
"""
s = {}
s1 = {'1', '2', 'abc', 'de'}
s2 = set()
print(type(s))      # this is dict
print(type(s1))     # this is set
print(type(s2))     # this is set
"""

#6
"""
d = {}

#a
name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

#b
for i in range(4):
    name = input("Enter friend name: ")
    lang = input("Enter language name: ")
    d.update({name: lang})
print(d)
"""

#7
#If the names of 2 friends are same;
#if names (key) are same, update() will update the value of name (language) 1st occurred, other name will not come in the dictionary

#8
#If languages of two friends are same;
#if languages (value) are same, it will add key:value pair normally

#9
s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 8     # TypeError: unhashable type: 'list

#1: we can't change value inside a list contained in set
#2: we cannot even have a list inside a set 

"""correct method to include list like structure inside set:
    s = {8, 7, 12, "Harry", (1, 2)}  # ✅ Tuples are immutable and hashable

But you still cant use indexing like s[4] because sets are unordered 
collections and do not support indexing.

for an indexable collection:
    s = [8, 7, 12, "Harry", [1, 2]]
    s[4][0] = 8  # Changes [1, 2] to [8, 2]
    print(s)     # Output: [8, 7, 12, 'Harry', [8, 2]]
"""