def try_login(name:str, password:str)->bool:
    with open("users.csv", mode='r') as f:
        data = f.readlines()
    logged_in = False
    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip() # remove \n

        if uname == name and upass == password:
            logged_in = True
            break
    return logged_in

attempts = 3
name = input("Please enter your username")
password = input("Please enter your password")
result = try_login(name=name,password=password)
while result == False and attempts > 0:
    name = input("[Error] Please enter your username")
    password = input("Please enter your password")
    result = try_login(name=name, password=password)
    attempts -= 1

if result == False:
    print("You are not authorized. Exiting")
    exit(1) # finish the program

# if True program will not exit and continues here
