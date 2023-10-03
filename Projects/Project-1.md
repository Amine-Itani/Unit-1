# Crypto Wallet
![video_image-kPdybtCNu](https://github.com/Amine-Itani/Unit-1/assets/123438294/19d4d119-67b1-4171-8160-cdea1d732153)

<sub>Illustration made with kapwing.com using Breaking Bad snapshot</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all her transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms. Sato to find past transactions or important statistics about the currency. Ms. Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Design Statement

I will to design and make an electronic ledger for Ms. Sato who is interested in crypto curency trading, and I've chosen KlimaDAO for her. The algorithm will organize Ms. Sato's transaction while providing useful statistics and security. The ledger is constructed using the software Python 3.10.11 and will take about 3 weeks to complete.

## Proposed Solution

Considering Ms. Sato's problem, the ledger will provide user-friendly and easy-to-understand functions that allow Ms. Sato to learn important statistics about the currency she's invested in as well as organize her transactions in a comprehensible way. It will also fetch real-time information about the crypto from the Web, helping Ms. Sato make informed decisions on her finances, and the ledger will be kept secure via a login system. Moreover, using Python is beneficial for Ms. Sato because it's a high-level (easy to understand) language that allowed her developer to code it quickly, therefore delivering it to her earlier than he would have using another language and avoiding prolonging her suffering with her spreadsheet. It also compiles quickly, reducing the time Ms. Sato would have to wait to get her ledger running, and is free, keeping the developer from having to pass down any costs on Ms. Sato.

## What is KlimaDAO, and why should Ms. Sato use it?

KlimaDAO is a decentralized autonomous organization and cryptocurrencies with many different benefits over other cryptocurrencies, which are the reason why the developer chose it for Ms. Sato.  
KlimaDAO is a cryptocurrency based on carbon crediting, and contributes to collecting funds for carbon offseting projects everytime it is traded. Many big polluting companies (such as airlines) invest in cryptocurrencies such as KlimaDAO in order to offset the carbon they produce.

### Benefits of KlimaDAO:

- **Profit**🤑: As the effects of climate change become more and more evident, the general public pushes companies to explore more ways of becoming carbon neutral, and carbon crediting is the perfect solution to that problem. Companies find it much easier to invest in carbon crediting cryptos like KlimaDAO instead of other solutions, driving the price of these cryptocurrencies up. This means huge return on investment for Ms. Sato.
- **Transperency**🤝: The mechanisms of KlimaDAO are all open-source and verified by external sources, guaranteeing Ms. Sato (as much as is reasonably possible) that the crypto she is investing in is not a scam. Websites mascarading as trustworthy cryptos have become increasingly popular, and the developer wants to make sure that Ms. Sato is getting the most reliable cryptocurrency she ca.
- **Environmentalism**🌱: Most cryptocurrencies till this day use a lot of processing power in order to crypt and decypt individual instinces of their coin in the blockchain. This uses a lot of energy, and accelerates climate change, especially if the source of that energy is fossil fuel. Assuming that Ms. Sato cares about environmental issues, investing in KlimaDAO instead of other cryptocurrencies can help her avoid having a negative impact on the environment.

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger displays the basic description of the cyrptocurrency selected.
3. The electronic ledger allows user to enter, withdraw and record transactions.
4. The electronic ledger will offer useful statistics about whether Ms. Sato has profited today, her most profitable day by day change, and her total amount in USD compared to intial investement. It will also predict value in a month based on yesterday to today.
5. The electronic ledger will connect to an API to fetch the price of KlimaDAO upon opening any of the ledgers sub-menus.
6. The electronic ledger will be organized with tables and graphs.

# Criteria B: Design

## System Diagram
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e859bd2d-13e6-4756-983c-efcfa0ba84e3)
<sub>Fig. 1 Shows the system diagram. Red box at the left represents the input hardware (keybaord). Red box at the right represents the output hardware (screen). In between, we can find the processing in the big overarching box (Windows 11, 16GB RAM, 12th Gen Intel), the coding language used (Python 3.10.11) in the smaller box. In the smallest box, we have the Python file that runs the code and the Python libraries (ledger_lib.py made by developer and others external) that it pulls from. We also have the csv files the program stores information in such as user verification and balances.

## Flow Diagrams
### Login system

<sub>**Fig. 2** Flow diagram for the registration system. Note: there is some Python code in the operations.

## Record of Tasks
| Task No | Planned Action                           | Planned Outcome                                                                          | Time estimated | Target completion date | Criterion |
|---------|------------------------------------------|------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1       | Create system diagram                    | To have a clear idea of the hardware and software requirements for the proposed solution | 10 min         | Sep 13                 | B         |
| 2       | Create a flow diagram for login functoin | A flow diagram                                                                           | 10 min         | Sep 14                 | B         |
| 3       | Create code for login funciton           | Login code tested and funcitonal                                                         | 20 min         | Sep 14                 | C         |

# Criteria C: Development

## Functions

### Login System
```.py
'''
Login system
:return: Access granted or denied
'''
while access == False and attempts > 0: #  while access false (access false by default) and check for attempts not exceeded
    name = input(f"{bold_red}ERROR.{end_code} Please enter your username again:")
    password = input("Please enter your password:")
    access = try_login(name=name, password=password) # check with csv file
    attempts -= 1 # use an attempt

if access == False: # uname or pass incorrect, attempts exceeded
    print(f"{bold_red}You are not authorized. Exiting{end_code}")
    exit(1) # end the program

if access == True: # access granted
    # continue ledger functions
```
Ms. Sato requires a system to protect their private data. I thought about using a login system to accomplish this using a while loop and if statements. The while loops continues when access is false and attempts > 0, and asks for user input, which the if statements check with the csv file where usernames and passwords are saved (more on reading csv files in a later function) to verify them. The while loop also decreases attempts by 1 from 3 to eventually stop the program if too many attempts (+3) are made. If access is true, the if statements will allow the program to keep going. The flow diagram for this function is show in **Figure 2**.

### Deposits and Withdrawals
```.py
def deposit(choice):
    '''
    This function appends a deposit or withdrawal to the csv file with the date it was commited.
    :return: Thank you message (feedback) and main menu
    '''
    multiplier = 1 # If withdrawal is picked, the multiplier is set to -1, turning the appended number in the csv file negative
    word_choice = 'withdrawal' # Word_choice variable used to correspond word in feedback msg to the action requested
    # These are determined by simple if statements that take user input that are omitted here, and validated by a different function
    amount = take_validate_user_input(msg=f"{deposit_prompt} {word_choice}:", menu="") # Take in user input
    date = datetime.date.today()  # creating the date with the datetime imported function
    with open('ledger.csv', mode='a') as f:  # appending deposit/withdrawal
        line = f"{date},{amount * multiplier}\n" # defining line as date and amount 
        f.writelines(line) # writing lines in csv file
    print(f"\n{yellow}Klima conversion: {amount} USD --> {round(amount / klima_price)} KLIMA today{end_code}\n{green}Saved.{end_code} "
          f"Thank you for recording your transaction in this ledger. Hope to see you again soon!\nThis deposit was made on {date}\n{green_seperator}")  # User Feedback
```
