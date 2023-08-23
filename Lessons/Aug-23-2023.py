"""
# This is a comment
# Get input from the user

first_name = input("Please enter your first name ")

#output

print("Hello", first_name)

# other types of variables

school = "uwcisak" 
year = 2023
height = 178.7 
is_smart = True

last_name = input("Please enter your last name")

email = (f"{year}.{first_name}.{last_name}@{school}.jp")
print(email)
"""
message = "Welcome to the smartest temperature converter!"
print(message)
print("#"*len(message))
print()

fahrenheit = input("Please enter the temperature in farenheit")
#before converting we need to validate that the user knows how to reload
if fahrenheit.isdecimal() == True:
    celcius = (int(fahrenheit) - 32) * 5/9
    print(f"This temperauture is {celcius} C!")
else:
    print("WRONG INPUT. USE DECIMAL NUMBERS")
