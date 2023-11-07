# Quiz 018
For this quiz, we used python to print out truth tables we're learning about in our second unit. This could be useful in the future! <br>
We also have to write down the circuit and truth table for the **equation (b): Light = S<sub>1</sub>S<sub>2</sub> + (S<sub>2</sub> + S<sub>3</sub>(notS<sub>1</sub>))S<sub>1</sub>**
## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/6609673b-5fc3-47ae-8556-500e09c6478b)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def get_truth():
    truth, a, b, c = '| A | B | C |\n', 1, 1, 1 # define variables, consolidated to one line, starts at 1 for indexing
    for x in range(8):
        if x % 4 == 0: # switch on every 4
            a = int(not(a))
        if x % 2 == 0: # switch on every 2
            b = int(not(b))
        c = int(not(c)) # switch everytime
        truth += f'| {a} | {b} | {c} |\n' # append to returned var

    return truth

table = get_truth() # test funtion
print(table)


```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/56f5588a-424f-4de2-a70b-7dc7941ca8ad)

<sub>Fig. 2 shows results of program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/22dae095-5bcf-4598-9f61-553d5bb80d4c)
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e4ea527b-9131-4fc7-9ee0-f3fa0e2bf8d1)

<sub>Fig. 3 shows flowchart of program

## Circuit
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/b0d52543-bdda-450c-85ba-d1d6fbf5d8c6)

<sub>Fig. 4 shows circuit of equation (b)

## Truth Table
| S1 S2 S3 | S1S2 (A) | not(S1) | not(S1)S3 (B) | B + S2 (C) | S1C (D) | A + D |
|----------|----------|---------|---------------|------------|---------|-------|
| 0  0  0  |     0    |    1    |       0       |      0     |    0    |   0   |
| 0  0  1  |     0    |    1    |       1       |      1     |    0    |   0   |
| 0  1  0  |     0    |    1    |       0       |      1     |    0    |   0   |
| 0  1  1  |     0    |    1    |       1       |      1     |    0    |   0   |
| 1  0  0  |     0    |    0    |       0       |      0     |    0    |   0   |
| 1  0  1  |     0    |    0    |       0       |      0     |    0    |   0   |
| 1  1  0  |     1    |    0    |       0       |      1     |    1    |   1   |
| 1  1  1  |     1    |    0    |       0       |      1     |    1    |   1   |

<sub>Fig. 5 shows truth table of equation (b)
