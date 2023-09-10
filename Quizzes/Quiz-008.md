# Quiz 008
This code counts how many times it takes to generate a random number < 15

## Code

```py
import random
num = 100
count = 0
while num >= 15:
    num = random.randint(1,101)
    count += 1
print(f"The number is now <15. It is {num} \n It took {count} iterations")
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/f3db7ae8-113a-4296-8ff0-57fdab0125c2)
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/b4562a2b-3c70-402f-9516-24cc4e0aa8ba)
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/70805392-44b0-429b-a3b0-ba591c988be9)
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/749324dc-88a5-4f1e-a026-5e867d3b184d)
<sub>Fig.1 shows results of the program

## Flowchart
![unnamed](https://github.com/Amine-Itani/Unit-1/assets/123438294/40a91e98-0ee2-4c86-bff6-6dc5c3e75533)
<sub>Fig.2 shows results of the program
