import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных для диаграммы рассеяния
num_points = 100  # Количество точек для диаграммы рассеяния
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.scatter(x_data, y_data, alpha=0.7, edgecolors='black')
plt.title("Диаграмма рассеяния для двух наборов случайных данных")
plt.xlabel("X данные")
plt.ylabel("Y данные")
plt.show()