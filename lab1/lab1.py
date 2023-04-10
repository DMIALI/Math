import matplotlib.pyplot as plt
import numpy as np
from math import *
from matplotlib.patches import Rectangle


def colors(n):
    hex_color_range = []
    hex_color_edgecolor = []
    for i in range(n):
        fraction = i / (n - 1)

        r1, g1, b1 = 236, int(173 * fraction), 255
        r, g, b = 47, int(226 * fraction), 237

        g = 255 if g > 255 else g
        g1 = 255 if g1 > 255 else g

        hex_color_range.append('#{:02x}{:02x}{:02x}'.format(r, g, b))
        hex_color_edgecolor.append('#{:02x}{:02x}{:02x}'.format(r1, g1, b1))

    return hex_color_range, hex_color_edgecolor


# Вводим тип разбиения
type_of_splitting = input('Введите тип разбиения: ')
n = int(input('Введите число точек разбиения: '))
x = np.arange(0, 1.001, 0.001)
mas = [i / n for i in range(0, n)]
y = np.exp(x)
color, edgecolor = colors(n)
sum_of_integral = 0

# Создаем график
fig, ax = plt.subplots()

ax.set_facecolor('black')
fig.set_facecolor('black')
ax.plot(x, y, color='white')
ax.tick_params(colors='white')
plt.ylim(0, 3)

ax.set_title('График функции $y = e^{x}$', color='white', fontsize = 15)
ax.set_xlabel('x', color='white')
ax.set_ylabel('y', color='white')
ax.spines['left'].set(color='white')
ax.spines['bottom'].set(color='white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
if type_of_splitting.lower() == 'left' or type_of_splitting.lower() == 'l':
    plt.text(0.0, 2.5, r'$Оснащение \  левое$', color='white', fontsize=15)
    for i in mas:
        sum_of_integral += exp(i) / n
        ax.add_patch(Rectangle((i, 0), 1 / n, exp(i), facecolor=color[mas.index(i)], edgecolor=edgecolor[-mas.index(i)], lw=1 / n))
elif type_of_splitting.lower() == 'right' or type_of_splitting.lower() == 'r':
    plt.text(0.0, 2.5, r'$Оснащение \  правое$', color='white', fontsize = 15)
    for i in mas:
        sum_of_integral += exp(i + 1/n) / n
        ax.add_patch(
            Rectangle((i, 0), 1 / n, exp(i + 1/n), facecolor=color[mas.index(i)], edgecolor=edgecolor[-mas.index(i)], lw=1 / n))
elif type_of_splitting.lower() == 'middle' or type_of_splitting.lower() == 'm':
    plt.text(0.0, 2.5, r'$Оснащение \  среднее$', color='white', fontsize=15)
    for i in mas:
        sum_of_integral += exp(i +1/(n * 2)) / n
        ax.add_patch(Rectangle((i, 0), 1 / n, exp(i +1/(n * 2)), facecolor=color[mas.index(i)], edgecolor=edgecolor[-mas.index(i)], lw=1 / n))

# Отображаем график
plt.text(0.0, 2.25, r'$\sigma_{\tau}(f, \xi) = $' + str(round(sum_of_integral, 6)), color='white', fontsize = 15)
plt.text(0.0, 2.75, r'$Число\ точек\ разбиения\ =\ $' + str(n) , color='white', fontsize = 15)
plt.show()
