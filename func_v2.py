import numpy as np
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def func(x):
    return 3 * x ** 3 + 3 * x ** 2 + x + 1

a = -1  
b = 1  # Верхня межа

x = np.linspace(-1, 1, 100)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.axhline(max(y), color='black', linestyle="--", linewidth=1.5)
ax.axhline(min(y), color='black', linestyle="--", linewidth=1.5) 
ax.axvline(x=a, color='black', linestyle="--", linewidth=1.5) 
ax.axvline(x=b, color='black', linestyle="--", linewidth=1.5)

ix =np.linspace(a, b, 100)
iy = func(ix)
ax.fill_between(ix, iy, color='yellow', alpha=0.5)

ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.set_title('Графік інтегрування f(x) , від ' + str(a) + ' до ' + str(b))

plt.grid()
plt.show()
