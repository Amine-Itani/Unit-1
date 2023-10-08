# Quiz 016
Easy one this time around. It's nice to have a break every once in a while.
## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/a18f922b-a782-4604-9250-3c37f71e72ca)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
def averageLength(words):
    sum = 0
    avg = 0
    for x in words:
        sum += len(x.strip())
    avg = sum/len(words)
    return avg

trial = averageLength(["Computer Science", "Art"])
print(trial)
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/f4d20dea-0243-45ad-aa6c-7a9a3700927c)
<sub>Fig. 2 shows results of program

## Flowchart
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/3a120ca1-41a4-4975-8f3a-3082500c05c2)

<sub>Fig. 3 shows flowchart of program
