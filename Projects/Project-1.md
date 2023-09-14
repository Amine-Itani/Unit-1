# Crypto Wallet

![](22ROOSE-master768.gif)  
<sub>Illustration for Glenn Harvey</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will to design and make a ———— for a client who is Ms. Sato. The ——– will about ———— and is constructed using the software ———. It will take  ———- to make and will be evaluated according to the criteria ———.

** add a description of your coin and citation **

Justify the tools/structure of your solution

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger will offer useful statistics about whether Ms. Sato has profited today, her most profitable day by day change, and her total amount in USD compared to intial investement. It will also predict value in a month based on yesterday to today.
5. The electronic ledger will organize transactions by month.
6. The electronic ledger will be secured with a password and username that will be set by the user.

# Criteria B: Design

## System Diagram
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/0c3a44a5-2766-4cff-a0c1-b9269334df81)
<sub>Fig. 1 Shows the system diagram. Red box at the left represents the input hardware (keybaord). Red box at the right represents the output hardware (screen). In between, we can find the processing in the big overarching box (Windows 11, 16GB RAM, 12th Gen Intel), the coding language used (Python 3.10.11) in the smaller box, and the potential python and csv files that will be used in the smallest box. 

## Flow Diagrams
### Login system

![unnamed](https://github.com/Amine-Itani/Unit-1/assets/123438294/eddfa485-33c6-4cce-abac-b16e8b561686)
<sub>Flow diagram for the registration system. Note: there is some Python code in the operations.

## Record of Tasks
| Task No | Planned Action                           | Planned Outcome                                                                          | Time estimated | Target completion date | Criterion |
|---------|------------------------------------------|------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1       | Create system diagram                    | To have a clear idea of the hardware and software requirements for the proposed solution | 10 min         | Sep 13                 | B         |
| 2       | Create a flow diagram for login functoin | A flow diagram                                                                           | 10 min         | Sep 14                 | B         |
| 3       | Create code for login funciton           | Login code tested and funcitonal                                                         | 20 min         | Sep 14                 | C         |

# Criteria C: Development

## Login System
My client requires a system to protect their private data. I thought about using a login system to accomplish this requirement using an if condition and a for loop.
The flow diagram for the diagram is show in ***Figure 2**. In the first line of the code I am defining a function called try_login with two inputs, name and password both are type string. 
The output of the function is boolea because I only need a True if the user and password exist in the database file.
'''.py
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
'''
