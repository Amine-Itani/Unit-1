# Quiz 004
The function of this piece of code was to take a given integer and count how many factors it had. The modulus operator, for loops, and if statements came in handy here.

## Code

```py
in_number = int(input("Please enter a number"))
factors = []
for i in range(1, in_number):
    if in_number % i == 0:
        factors.append(i)
print(factors)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/06b1853b-3a30-4541-8535-62ca9af67634)

<sub>Fig.1 shows results of the program

## Flowchart
![Quiz004](https://github.com/Amine-Itani/Unit-1/assets/123438294/14ff5464-238c-4db7-b932-49a8e42dddd7)
<sub>Fig.2 shows results of the program
