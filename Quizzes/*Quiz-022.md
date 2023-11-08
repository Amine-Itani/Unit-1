# Quiz 022

## Input & Output

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
from matplotlib import pyplot as plt

# crate the lists x and y
y = []
x = []
for num in range(-10, 10):
    x.append(num)
    y.append(2*((num + 5)**2))

plt.plot(x, y, 'r', linewidth=2)
plt.title("Graph of the equation $f(x)=2(x+5)^2$")
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/e25de5f1-7722-4322-b750-358034761703)

<sub>Fig. 2 shows results of program

## Circuit

<sub>Fig. 3 shows flowchart of program
