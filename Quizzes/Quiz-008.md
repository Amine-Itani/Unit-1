# Quiz 008
This code takes an integer input and turns it into different iterations of power from pico (10^-12) to tera (10^12)

## Code

```py
# define variable
num = input("Please enter a number")
units = [" Kilo", " Mega", " Giga", " Tera"]
powers = ["000", "000000", "0000000000", "000000000000"]
units2 = ["Mili", "Micro", "Nano", "Pico"]
powers2 = ["00", "00000", "00000000", "00000000000"]


# functions
for x in range(len(units)):
    output = f"{num}{powers[x]}{units[x]}"
    print(output)

for x in range(len(units2)):
    output2 = f"0.{powers2[x]}{num}{units[x]}"
    print(output2)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/1ea71709-6db4-4609-ac4f-13b695e31081)
<sub>Fig.1 shows results of the program

## Flowchart
![unnamed](https://github.com/Amine-Itani/Unit-1/assets/123438294/2c2c1bf5-32bb-4007-a3cc-c29f36c6ef34)
<sub>Fig.2 shows results of the program
