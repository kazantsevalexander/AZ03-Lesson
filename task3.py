from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import matplotlib.pyplot as plt

# Настройка Selenium WebDriver
driver = webdriver.Firefox()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(3)  # Даем время странице загрузиться

# Сбор данных о диванах
sofa_data = []
while True:
    sofas = driver.find_elements(By.CLASS_NAME, 'product-card__info')
    for sofa in sofas:
        name = sofa.find_element(By.CLASS_NAME, 'product-card__title').text
        try:
            price_text = sofa.find_element(By.CLASS_NAME, 'product-card__price').text
            price = int(price_text.replace(" ", "").replace("₽", ""))
        except:
            price = None  # Пропускаем, если цена не найдена
        if price is not None:
            sofa_data.append({"Name": name, "Price": price})

    # Проверка на наличие кнопки "Следующая страница" и переход на неё
    try:
        next_button = driver.find_element(By.CLASS_NAME, 'pagination__item--next')
        next_button.click()
        time.sleep(2)  # Задержка на случай перезагрузки страницы
    except:
        break  # Прерываем, если нет кнопки следующей страницы

driver.quit()

# Сохранение данных в CSV
df = pd.DataFrame(sofa_data)
df.to_csv('sofa_prices.csv', index=False)

# Обработка данных: нахождение средней цены
mean_price = df['Price'].mean()
print(f"Средняя цена дивана: {mean_price:.2f} рублей")

# Построение гистограммы цен
plt.hist(df['Price'], bins=30, edgecolor='black')
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена, руб.")
plt.ylabel("Количество")
plt.show()
