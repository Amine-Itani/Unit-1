#August 24 2023

# Exercise 1
# input full name
# output ONLY first name + Hey ___, how are you today?
"""
full_name = (input("Please enter your name"))

split_name = full_name.split()

print(f"Hey {split_name[0]}, how are you today")
"""

# Exercise 2
"""
string2 = input("Please eneter a word")

if string2[0] == string2[-1]:
    print("True")
else:
    print("False")
"""

# Exercise 3
"""
string3 = input("Please enter a word")
string3 = string3.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('o','*')
print(string3)
"""

# Exercise 4
"""
instring = input("Please enter two words with a space between")

def function(instring):
    originalwords = instring.split()
    changedwords = ' '.join(reversed(originalwords))
    return changedwords

outstring = function(instring)
print(outstring)
"""

string = input("Please enter a word")

string = string + string[-1].capitalize()

print(string)

