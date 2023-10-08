# Quiz 008
This code takes an integer input and turns it into different iterations of power from pico (10^-12) to tera (10^12)

## Code

```py
# define variable
num = input("Please enter a number")
unit = input(f"{num} of what? Please enter a unit")
units = [" Kilo", " Mega", " Giga", " Tera"]
powers = ["000", "000000", "0000000000", "000000000000"]
units2 = ["Mili", "Micro", "Nano", "Pico"]
powers2 = ["00", "00000", "00000000", "00000000000"]

# functions
for x in range(len(units)):
    output = f"{num}{powers[x]}{units[x]}{unit}"
    print(output)
print(f"{num} {unit}")
for x in range(len(units2)):
    output2 = f"0.{powers2[x]}{num}{units[x]}{unit}"
    print(output2)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/1fef4cb7-30e8-42bf-a1ed-2a2a4b9989b5)
<sub>Fig.1 shows results of the program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/83a2521a-d743-4353-989d-5ce4235b4283)
<sub>Fig.2 shows results of the program
