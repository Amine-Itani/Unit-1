# Quiz 018
For this quiz, we used python to print out truth tables we're learning about in our second unit. This could be useful in the future!
## Input & Output

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def get_truth():
    truth = '' # define variables
    a = 0
    b = 0
    c = 0
    a_count = 0
    b_count = 0
    truth += f"| A | B | C |\n"
    for x in range(8):
        truth += f"| {a} "
        a_count += 1
        if a_count%4 == 0:
            a = int(not a)
        truth += f"| {b} "
        b_count += 1
        if b_count%2 == 0:
            b = int(not b)
        truth += f"| {c} |\n"
    return truth

table = get_truth()
print(table)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/56f5588a-424f-4de2-a70b-7dc7941ca8ad)

<sub>Fig. 2 shows results of program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/22dae095-5bcf-4598-9f61-553d5bb80d4c)
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e4ea527b-9131-4fc7-9ee0-f3fa0e2bf8d1)

<sub>Fig. 3 shows flowchart of program
