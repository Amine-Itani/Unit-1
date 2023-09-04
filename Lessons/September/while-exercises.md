import random
"""
count = 0
i = 0

while count < 1000:
    if i%7 == 0 and i%6 == 0:
        print(f"{i} is a multiple of 6 and 7")
        count += 1
    i += 1
"""
secret_number = random.randint(1,100)
user_guess = int(input("Please enter an integer between 1-100"))

attempts = 0
while secret_number != user_guess:
    print(f"Sorry, {user_guess} is not the correct guess")
    user_guess = int(input("Please try again"))
    if user_guess > secret_number:
        print(f"{user_guess} is bigger than the secret number")
    else:
        print(f"{user_guess} is smaller than the secret number")
    attempts += 1
