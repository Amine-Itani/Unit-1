import random

def get_password()->str:
    password = ''
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for x in range(20):
        n = random.randint(0,len(symbols))
        password += symbols[n]
    return password

case1 = get_password()
print(case1)
