# Crypto Wallet
![video_image-kPdybtCNu](https://github.com/Amine-Itani/Unit-1/assets/123438294/19d4d119-67b1-4171-8160-cdea1d732153)

<sub>Illustration made with kapwing.com using Breaking Bad snapshot</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all her transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms. Sato to find past transactions or important statistics about the currency. Ms. Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Design Statement

I will to design and make an electronic ledger for Ms. Sato who is interested in crypto curency trading, and I've chosen KlimaDAO for her. The algorithm will organize Ms. Sato's transaction while providing useful statistics and security. The ledger is constructed using the software Python 3.10.11 and will take about 3 weeks to complete.

## Proposed Solution & Justification

Considering Ms. Sato's problem, the ledger will provide user-friendly and easy-to-understand functions that allow Ms. Sato to learn important statistics about the currency she's invested in as well as organize her transactions in a comprehensible way. It will also fetch real-time information about the crypto from the Web, helping Ms. Sato make informed decisions on her finances, and the ledger will be kept secure via a login system. Moreover, using Python is beneficial for Ms. Sato because it's a high-level (easy to understand) language that allowed her developer to code it quickly, therefore delivering it to her earlier than he would have using another language and avoiding prolonging her suffering with her spreadsheet. It also compiles quickly, reducing the time Ms. Sato would have to wait to get her ledger running, and is free, keeping the developer from having to pass down any costs on Ms. Sato.

## What is KlimaDAO, and why should Ms. Sato use it?
KlimaDAO<sup>1</sup> is a decentralized autonomous organization and cryptocurrencies with many different benefits over other cryptocurrencies, which are the reason why the developer chose it for Ms. Sato.  
KlimaDAO is a cryptocurrency based on carbon crediting, and contributes to collecting funds for carbon offseting projects everytime it is traded. Many big polluting companies (such as airlines) invest in cryptocurrencies such as KlimaDAO in order to offset the carbon they produce.

### Benefits of KlimaDAO:

- **Profit**🤑: As the effects of climate change become more and more evident, the general public pushes companies to explore more ways of becoming carbon neutral, and carbon crediting is the perfect solution to that problem. Companies find it much easier to invest in carbon crediting cryptos like KlimaDAO instead of other solutions, driving the price of these cryptocurrencies up. This means huge return on investment for Ms. Sato.<sup>2</sup>
- **Transperency**🤝: The mechanisms of KlimaDAO are all open-source and verified by external sources, guaranteeing Ms. Sato (as much as is reasonably possible) that the crypto she is investing in is not a scam. Websites mascarading as trustworthy cryptos have become increasingly popular, and the developer wants to make sure that Ms. Sato is getting the most reliable cryptocurrency she can.<sup>3</sup>
- **Environmentalism**🌱: Most cryptocurrencies till this day use a lot of processing power in order to crypt and decypt individual instinces of their coin in the blockchain. This uses a lot of energy, and accelerates climate change, especially if the source of that energy is fossil fuel. Assuming that Ms. Sato cares about environmental issues, investing in KlimaDAO instead of other cryptocurrencies can help her avoid having a negative impact on the environment.<sup>4</sup> 

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
<sub>**Fig. 1** Shows the system diagram. Red box at the left represents the input hardware (keybaord). Red box at the right represents the output hardware (screen). In between, we can find the processing in the big overarching box (Windows 11, 16GB RAM, 12th Gen Intel), the coding language used (Python 3.10.11) in the smaller box. In the smallest box, we have the Python file that runs the code and the Python libraries (ledger_lib.py made by developer and others external) that it pulls from. We also have the csv files the program stores information in such as user verification and balances.

## Flow Diagrams
### Simple Login
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/fb9e7b07-d922-453c-9d70-419cb902ea71)<br>
<sub> **Fig. 2** shows the flow diagram for the login system. 
#### Explanation
Important to note that the user is logged out by default, and that Ms. Sato set the username and password with the developer before receiving her program, therefore they are already in the csv file. The way the simple login works is that it looks at all the lines in the csv file containing the username and password and compares that to the users input. If both parameters match, the program will continue, and if either or both do not match, the program will terminate.
### Validate and Return User Input
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/6fb85e55-db79-45fc-b236-a5d0cc6334a6) <br>
<sub> **Fig. 3** shows the flow diagram for taking in and validating user input. 
#### Explanation
The parameters to meet depend on the function the validation is working with and are defined accordingly. The function could be checking if the input is within a certain raneg of integers (used for menu selecting) or could be checking if it is an integer in the first place (used for deposit.withdrawal)
### Looping Function Chooser
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/741d2205-2baa-4826-b898-4f6435f78579)<br>
<sub> **Fig. 4** shows how the program loops and runs a function based on user input, unless they choose to exit the program. 
#### Explnation
This function is built on a while loop and many if statements. When the while loop is running, it will check if the input of the user is between 1 and 6, and will run the respective functions depending on the value of the user input. 6 is exit, so it will break out of the while loop and terminate the program. Values between 1 and 5 each run their own function then end by returning the choice as -1, which is outside of 1-6. This makes the while loop start over and gives the user the option to choose another function or exit with 6.

## Record of Tasks
| Task No | Planned Action                           | Planned Outcome                                                                          | Time estimated | Target completion date | Criterion |
|---------|------------------------------------------|------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1       | Create system diagram                    | To have a clear idea of the hardware and software requirements for the proposed solution | 10 min         | Sep 13                 | B         |
| 2       | Create a flow diagram for login functoin | A flow diagram                                                                           | 10 min         | Sep 14                 | B         |
| 3       | Create code for login funciton           | Login code tested and funcitonal                                                         | 20 min         | Sep 14                 | C         |

# Criteria C: Development
## Tools Used
- If statememts
- For loops
- While loops
- Open with and read lines (csv files)
- Taking User Input
- Web Scraping --> BeautifulSoup 4<sup>5</sup> (made by Leonard Richardson), scraped from crypto.com<sup>8</sup>
- Default Dictionary<sup>6</sup> (module originally made by Raymond Hettinger)
- ASCII squares multiplication --> graphs in terminal<sup>7</sup> (originally by Bob Bemer)
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
Ms. Sato requires a system to protect their private data. I thought about using a login system to accomplish this using a while loop and if statements. This login system is good because it allows for attempts to be made in the case of typos, and returns feedback (errors). The while loops continues when access is false and attempts > 0, and asks for user input, which the if statements check with the csv file where usernames and passwords are saved (more on reading csv files in a later function) to verify them. The while loop also decreases attempts by 1 from 3 to eventually stop the program if too many attempts (>3) are made. If access is true, the if statements will allow the program to keep going. The flow diagram for a simpler version of this function can be found in **Fig. 2**.

### Deposits and Withdrawals
```.py
import datetime
def deposit(choice):
    '''
    This function appends a deposit or withdrawal to the csv file with the date it was commited.
    :return: Thank you message (feedback) and main menu
    '''
    multiplier = 1 # If withdrawal, the multiplier is set to -1, turning the number appended negative
    word_choice = 'withdrawal'
    # These are determined by simple if statements that take user input that are omitted here
    amount = take_validate_user_input(msg=f"{deposit_prompt} {word_choice}:", menu="")
    date = datetime.date.today()  # creating the date with the datetime imported function
    with open('ledger.csv', mode='a') as f:  # appending deposit/withdrawal
        line = f"{date},{amount * multiplier}\n" 
        f.writelines(line) # writing lines in csv file
    print(f"\n{yellow}Klima conversion: {amount} USD --> {round(amount / klima_price)} KLIMA today{end_code}\n{green}Saved.{end_code} " # klima_price is web scraped
          f"Thank you for recording your transaction in this ledger. Hope to see you again soon!\nThis deposit was made on {date}\n{green_seperator}")  # User Feedback
```
This function allows Ms. Sato to deposit or withdrawal money from her ledger. This function is practical doesn't need Ms. Sato to input a negative number if she withdraws, as it does that automcatically when the withdraw function is picked. The user feedback is also accurate as it chooses between including deposit or withdraw in further messages after the choice is made by the user. When Ms. Sato withdrawals money, she enters an integer that is validated by another function (more on that later), just as she would for withdrawals. The way the algorith differentiates between taking in and taking out money is through multiplying the input value by -1 if Ms. Sato chooses withdrawal. The variable klima_price is web scrapped, which will be covered in another explanation, and the datetime function is imported. The function also uses the 'with' and 'open' functions to read the csv file and defines mode as a to append user inputs. The flow diagram for this function can be found in **Figure 3**.

### Take and Validate User Input
```.py
def take_validate_user_input(msg, menu):
    '''
    This function takes in user input and validates it is an integer or prints an error.
    :return: The value/Error Message
    '''
    option = input(msg)
    while not option.isdigit(): # when option is not a digit
        print(f'\n{bold_red}ERROR. Please input one of the options displayed above{end_code}\n{red_seperator}')
        main_menu(menu, 0) # print menu
        option = input(msg) # ask for input again
    return int(option)
```
Although this function is quite simple, it is the blueprint of all other input validations that happen in this program. It is important because it makes sure that all other functions receive imputs that are in the right range and type. It also returns user feedback as errors. It uses a while loop that only exits if the input is the same as what is expected. As the while loop continues, it asks and waits for user input, keeping it from looping forever. In other validation, it functions this same, but instead checks if the input is in a given list of choices. The flow diagram for this function can be found in **Fig. 3**

### Web Scraping
```.py
from bs4 import BeautifulSoup
def klimadao_price():
    '''
    This function fetches the conversion rate of KlimaDAO to USD whenever the program is run
    :return: The price of KlimaDAO to USD now
    '''
    url = "https://crypto.com/price/klimadao" # Website used
    page = requests.get(url) # Requesting specifically the page to inspect it's lines
    soup = BeautifulSoup(page.text, 'html5lib') # Using parser and that page as text to set soup as the whole html of the page
    output = soup.find('span', class_ ="chakra-text css-13hqrwd").text.strip('$ USD') # .find method returns specific part of html code asked for in class_ argument
    return output 
```
This is a function that fetches the rate of KlimaDAO on the dollar from the internet. It is pragmatic because it doesn not need to open the browser and wait 5-10 seconds as many other parsers and web scrapers have to. It also strips the return of all html code but keeps the dash sign in order to differentiate between positive and negative numbers. It does this by by having imported the function BeautifulSoup<sup>5</sup>, which is a web scraper made by Leonard Richardson to allow programmers to access information on the web through Python. The function created for the ledger request the page as text from a url specified (in this case: https://crypto.com/price/klimadao), and parces the texts with the html parcer 'html5lib', turning the text from the instance requested into an html page under the variable 'soup'. The method .find then goes through  the html code and returns only that which is specified in the parameter class_. A similar function and tool is used in predicting Ms. Sato's return on investment. The flow diagram for this function can be found in **Figure 5**

### Deafult Dictionary Sums
```.py
from collections import defaultdict
def sum_by_date():
    '''
    This function sums the transactions of every day into a balance for that day.
    :return: Every day's respective balance
    '''
    date_sums = defaultdict(int) # create dictionary with unique, editable, pairs
    with open('ledger.csv', mode='r') as f: # reading and extracting balances from csv file
        data = f.readlines()
    for line in data: # for loop that iterates for every entry in the csv file
        date, amount = line.strip().split(',')
        date_sums[date] += int(amount) # add extracted amount to the second value in the dictionary pair
    return date_sums
```
This function creates a dictionary with a sum of all transactions from a day paired with that date. The defaultdict<sup>6</sup> allows us to avoid any errors if the csv file has misinputs and also makes entering values into it easier, as we do not need to specify which pair each value has to go in. That is instead done through indexing. 
### Graphing
```.py
def day_balance():
    '''
    This function prints colored graphs with warnings in case of poor finances.
    :return: the graph
    '''
    # ommited: defining graph and warning message variables
    date_sum = sum_by_date()
    print(f"{blue}Your earning/loss by day.{end_code} Earning is printed in {green}green{end_code}, and loss is printed in {red}red{end_code}.")
    for date, total in date_sum.items(): # ommited: if statements that adds warning message
        if total < 0:
            graph_var = f'{red}▩{end_code}'
            total *= -1
        else:
            graph_var = f"{green}▩{end_code}"
        graph += f"{date}: {graph_var * (total // 10)}{total} USD {warning}\n"
    return graph
```
This functions prints a graph that shows Ms. Sato's earning or loss by day. This means that if she were to take out 2000 usd and deposit 1000 on a given day, the graph would show -1000, regardless of transactions made on other days. This will help her keep trak of her financial stability better. This function meets Ms. Sato's need for useful, comprehensive, statistics well because the color of the graph changes depending on whether she is earning or losing money. It also prints a warning message if she is more than $400 USD in debt on a given day. The graph is made through reading the default dictionary created in sum_by_date function, finding the balance of that day, and multipliying them with a square "▩" from the ASCII code<sup>7</sup>. Before multiplication though, we divide the multiplier by 10 to keep the graph manageable in the terminal.

## Citations
1. DAO, Klima. “Introducing Klimadao.” KlimaDAO, Mar. 2023, docs.klimadao.finance/.
2. DAO, Klima. “Frequently Asked Questions about Klima Infinity.” KlimaDAO, 2023, www.klimadao.finance/blog/klima-infinity-faqs. 
3. DAO, Klima. “Klimadao Impact Report: Analysis of the Base Carbon Tonne.” KlimaDAO, 2023, www.klimadao.finance/blog/klimadao-analysis-of-the-base-carbon-tonne.
4. Kolesnikov, Nicole. “60+ Bitcoin Mining and Energy Statistics Updated for 2023 - Techopedia.” Technopedia, 2023, www.techopedia.com/bitcoin-mining-and-energy-statistics.
5. Richardson, Leonard. “Beautiful Soup Documentation¶.” Beautiful Soup Documentation - Beautiful Soup 4.12.0 Documentation, 2004, www.crummy.com/software/BeautifulSoup/bs4/doc/.
6. Hettinger, Raymond. “Defaultdict in Python.” GeeksforGeeks, GeeksforGeeks, 10 Jan. 2023, www.geeksforgeeks.org/defaultdict-in-python/.
7. Bemer, Bob. “Square Symbols.” Alt Codes Symbols, 2021, www.alt-codes.net/square-symbols.
8. .Com, Crypto. “Klimadao Price: Klima Price, USD Converter, Charts.” Https://Crypto.Com/Price/Klimadao, 5 Oct. 2023, crypto.com/price/klimadao. 
