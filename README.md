# python-for-data-DTA

# Файл main.py
В даному проекті я працюю з базою даних movies_metadata.csv.

У файлі main.py спочатку імпортуємо бібліотеки

# 1. Імпортування бібліотек

1) import numpy as np   - для роботи з математичними операціями 
2) import pandas as pd  - для роботи з табличними даними, CSV/Excel, створення DataFrame
3) import matplotlib.pyplot as plt  - частина яка відповідає за побудову гафіків
4) import seaborn as sns   - для статистичних графіків
5) import ast   - (Abstract Szntax Trees) для перетворення рядків у Python-об'єкти, для колонок де записані списки 


# 2. Завантаження CSV файлу

url = "data/movies_metadata.csv"
df = pd.read_csv(url)   - завантаження даних з CSV файлу у вигляді таблиці DataFrame, за допомогою бібліотеки pandas

# 3. Список команд для роботи з таблицею DataFrame

print(df.head())    - виведе перші 5 рядків
df.info()           - коротка інф-ція про DataFrame (Колонки, кількість рядків, тип об'єктів, non-null)
print(df.describe()) - статистиний опис числових колонок (count, mean, max, std, 25%)
print(df.isnull().sum())  - кількість пропущених значень (Nan) у кожній колонці 
                            (df.isnull() — створює таблицю з True/False, де True означає пропуск. .sum() — підсумовує True як 1)

# 4. Працюю зі стовпцями belongs_to_collection, homepage, tagline

print(df[["belongs_to_collection", "homepage", "tagline"]]) - вивід 3 стовпців

Потрібно замінити всі пропущені значення NaN у tagline на "without tagline", щоб у колонці не залишилось пропусків

1) Варіант виведення з заміною NaN у tagline
df["tagline"].fillna("without tagline", inplace=True)
print(df.tagline)

2) Варіант через словник
#df.fillna({"tagline":"without tagline"}, inplace=True)

3) Остаточний Варіант 
df["tagline"] = df["tagline"].fillna("without tagline")

print(df.tagline) - виводимо tagline
print(df.homepage)

Всі NaN у homepage замінюються рядком "no homepage"
df.homepage = df.homepage.fillna("no homepage")
print(df.homepage) 


Потрібно замінити всі пропуски на порожній словник {}
#print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection":"{}"}, inplace=True)
#print(df["belongs_to_collection"])

#df.info()

df.dropna(inplace=True) - Видалення рядків з пропусками
#print(df.isnull().sum())
#df.info()


# 5. Для обробки жанрів створено функцію extract_genres
def extract_genres(genre_str):  
    try:
        genres = ast.literal_eval(genre_str)
        return[genre['name'] for genre in genres]
    except ValueError:
        return []

print(df['genres'].apply(extract_genres))  - застосування функції до кожного рядку в genres
df['genres'] = df['genres'].apply(extract_genres)

------------------------------------------------

def extract_genres(genre_str): -> "[{'id': 18, 'name': 'Drama'}, {'id': 35, 'name': 'Comedy'}]"

genres = ast.literal_eval(genre_str) -> перетворює у список словників для Python
                                        [
                                            {'id': 18, 'name': 'Drama'},
                                            {'id': 35, 'name': 'Comedy'}
                                        ]


 return [] -> Проходиться по кожному елементу списку й дістає тільки назву жанру
                ['Drama', 'Comedy']

------------------------------------------------

print(df.head())     #виводжу таблицю
print(df.genres)    #жанри

all_genres = df['genres'].explode() - Щоб кожен жанр став окремим рядком
genres_counts = all_genres.value_counts() # порахувати скільки жанрів
print(genres_counts)

# 6. Побудова графіка жанрів
print(genres_counts.index)  # X
print(genres_counts.values) # Y     # кількість певного жанру  (drama 4885 з 40 000 приблизно)

#візуалізація
plt.figure(figsize=(10,6)) #задали розмір

sns.barplot(x=genres_counts.index, y=genres_counts.values)     #побудова графіку

plt.title("Count film for genres") - назва графіка
plt.xlabel("genres") - підпис по осі Х
plt.ylabel("counts") - підпис по осі Y

plt.xticks(rotation=45)    #як розміщені підписи

plt.show() - виводить графік на екран



-------------------------------------------------------------------------------------
# Файл lesson_data.py
# Створення DataFrame з словниками

1. Підключення бібліотеки pandas

import pandas as pd

2. Словник Sales з індексами months
months = ['jan', 'feb', 'mar', 'apr']   - індекси рядків
sales = {                               - словник
    'revenue':[100, 200, 300, 400],     - 'revenue' - назва колонки та значення
    'items_sold':[23, 43, 54, 65],
    'new_clients':[10, 20, 30, 40]
}

3. Створення DataFrame (Таблиця)
df = pd.DataFrame(data=sales, index=months) - за допомогою словника 
print(df) - виводимо таблицю

# Методи DataFrame
-----------------------------------------------
head(2) — виводить перші 2 рядки
tail(1) — виводить останній рядок
df.revenue — доступ до стовпця revenue як до Series
df.info() — кількість рядків/колонок, типи даних, пропуски
df.shape — кортеж (кількість_рядків, кількість_стовпців)
df.columns — список назв усіх колонок
df.describe() — статистика для числових колонок (mean, min, max, std…)
df.dtypes — тип даних кожної колонки (int64, float64, object…)
-------------------------------------------

4. Приклад помилки у типах даних '100a'
df.revenue = ['100a', '200', '300', '400'] - '100a' - не правильне значення 
print(df) - тепер не числа а str
print(df.revenue.dtypes) - вивід типу

5. Перетворення str у числа
df.revenue = pd.to_numeric(df.revenue, errors= 'coerce') - конвертує кожен елемент у число, у випадку '100a' при errors= 'coerce' -> NaN
print(df)
print(df.describe()) - статистика про revenue
print(df.revenue.dtypes)

6. Вибір рядків за індексом через Loc
print(df.loc[['feb', 'apr']]) - звернення по індексу

movies_df = pd.read_csv('data/movies_metadata.csv')
#print(movies_df.to_string())
pd.options.display.max_rows = 45000 - максимальна кількість рядків
print(pd.options.display.max_rows) - перевірка зміни значень