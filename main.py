import numpy as np      # з масивами та числовими обчисленнями
import pandas as pd     # для роботи з таблицями та даними (DataFrame)
import matplotlib.pyplot as plt  #pyplot для графіки (частина модулю matplotlib)
import seaborn as sns   # для стильних статистичних графіків
import ast


url = "data/movies_metadata.csv"

df = pd.read_csv(url) # df = DataFrame   # Завантажуємо CSV у DataFrame за допомогою pandas

# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())

# print(df[["belongs_to_collection", "homepage", "tagline"]])

# df["tagline"].fillna("without tagline", inplace=True)
# print(df.tagline)

#df.fillna({"tagline":"without tagline"}, inplace=True)
df["tagline"] = df["tagline"].fillna("without tagline")

#print(df.tagline)

# print(df.homepage)

df.homepage = df.homepage.fillna("no homepage")
#print(df.homepage)

#print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection":"{}"}, inplace=True)
#print(df["belongs_to_collection"])

#df.info()

df.dropna(inplace=True)
#print(df.isnull().sum())
#df.info()


#-------------------------------------------------------------------

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return[genre['name'] for genre in genres]
    except ValueError:
        return []
#print(extract_genres(df['genres'].value_counts()))
print(df['genres'].apply(extract_genres))
df['genres'] = df['genres'].apply(extract_genres)
#------------------------------------------------------------------



#print(df.head())     #виводжу таблицю
#print(df.genres)    #жанри


all_genres = df['genres'].explode()
genres_counts = all_genres.value_counts() # порахувати скільки жанрів
# print(genres_counts)

# print(genres_counts.index)  # X
# print(genres_counts.values) # Y     # кількість певного жанру  (drama 4885 з 40 000 приблизно)

#візуалізація
plt.figure(figsize=(10,6)) #задали розмір

sns.barplot(x=genres_counts.index, y=genres_counts.values)     #побудова графіку

plt.title("Count film for genres")
plt.xlabel("genres")
plt.ylabel("counts")

plt.xticks(rotation=45)    #як розміщені підписи

plt.show()