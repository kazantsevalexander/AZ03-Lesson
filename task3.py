import csv
import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из CSV файла и преобразование цен в числа
prices = []
with open("/Users/alexander/Documents/GitHub/AZ03-Lesson/divan_prices/divan_prices/spiders/sofa_prices.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Преобразуем цену в число, удаляя символы валюты и пробелы, если необходимо
        price = row["Price"].replace("₽", "").replace(" ", "").strip()
        if price.isdigit():
            prices.append(int(price))

# Вычисляем среднюю цену
average_price = np.mean(prices)
print(f"Средняя цена: {average_price:.2f} ₽")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, edgecolor='black')
plt.xlabel("Цена (₽)")
plt.ylabel("Количество диванов")
plt.title("Гистограмма цен на диваны")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
