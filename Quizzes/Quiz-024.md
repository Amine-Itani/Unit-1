# Quiz 024
This quiz expands on scatterplots by making them much more readable and therefore useful. We use the numpy library to import the .polyfit method that takes x and y values and using linear regression to turn them into an ax + b linear function. This will probably the most applicable graph in projects and other situations. Also continuing base conversion, where this question asks us to convert hex to RGB. This confuses me because I thought RGB was usually expressed in hex, but I guess it can also be expressed in decimal.

## Input & Output
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/89934076-d771-45eb-9413-b965434ce3ea)

<sub>Fig. 1 shows given intput and outputs of task
## Code

```py
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('grayscale')

hum = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]
time = []

t = 0
for x in range(len(hum)):
    time.append(x)
    t += 10

# build linear model

a, b = np.polyfit(time, hum, 1)
print(a)

print(f"The linear model is Hum(%) = {a:.2f}t + {b:.2f}")
time_model = []
hum_model = []
for i in range(0, 320, 10):
    time_model.append(i/10)
    hum_model.append(a * (i/10) + b)

plt.plot(time_model, hum_model, color="orange")
plt.scatter(time, hum, color='r')
plt.title("Graph of the equation $f(x)=2(x+5)^2$")
plt.text(15, 14, f'T(t) = {a:.2f}t + {b:.2f}', fontsize= 10, color='orange')
plt.show()
```

## Evidence
![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/72aeb175-d478-4a5c-86b3-a645b3599ff7)

<sub>Fig. 2 shows results of program

## Binary Conversion
### #e6e627

red = 248, green = 248, blue = 39

![image](https://github.com/Amine-Itani/Unit-1/assets/123438294/a5e8d7a7-4553-48d3-b6c3-2723cae65dd2)

<sub>Fig. 3 shows the color represented by the RGB



