'''
Задача:
Как музыка, которая звучит по дороге на работу в понедельник утром, отличается от той,
что играет в среду или в конце рабочей недели? Возьмите данные для Москвы и Петербурга.
Сравните, что и в каком режиме слушают их жители.
'''

import pandas as pd


# следующие две строки нужны, чтобы PyCharm показывал все столбцы в ряд
pd.set_option('display.max_columns', 10) # показывать 10 столбцов; у нас в таблице 7 столбцов, но вдруг будем добавлять
pd.set_option('display.width', 320) # устанавливаем ширину показываемой области


df = pd.read_csv('music_project.csv') # считываем файл с данными

#print(df.head(10)) # просматриваем первые 10 строк, проверяем, что отображается нормально
#print(df.info()) # общая информация о таблице

# получаем перечень названий столбцов
#print(df.columns)

# переименовываем столбы
df.set_axis(['user_id', 'track_name', 'artist_name', 'genre_name', 'city', 'time', 'weekday'], axis='columns', inplace=True)
#print(df.columns)

# проверим, есть ли пропуски в таблице
#print(df.isnull().sum())

# заменяем пропуски в столбцах track_name и artist_name на 'unknown'
df['track_name'] = df['track_name'].fillna('unknown')
df['artist_name'] = df['artist_name'].fillna('unknown')
#print(df.isnull().sum())

# удаляем записи, для которые не прописан genre_name - нам они не нужны, т.к. без genre_name не могут быть использованы в анализе
df = df.dropna()
#print(df.isnull().sum())
#print(df.info)

# ищем дубликаты
#print(df.duplicated().sum())

# удаляем дубликаты, обновляем индексы
df = df.drop_duplicates().reset_index(drop=True)
#print(df.duplicated().sum())

# сохраняем список уникальных значений стобца с жанрами
genres_list = df['genre_name'].unique()
#print(genres_list)

# Создаем функцию, которая будет искать неявные дубликаты в списке жанров genres_list.
# Функция возвращает, есть ли искомое значение в списке (1), или его нет (0)
def find_genre(genre):
    count = 0
    for i in genres_list:
        if i == genre:
            count += 1
    return count

# проверяем наличие в списке genres_list различных названий жанра hiphop
#print(find_genre('hip'))   # здесь нашлой одно значение
#print(find_genre('hop'))
#print(find_genre('hip-hop'))

# создаем функцию, которая будет заменять неправильное название жанра на правильное
def find_hip_hop(df, wrong):
    df['genre_name'] = df['genre_name'].replace(wrong, 'hiphop')

# заменяем неправильное значение на правильное
find_hip_hop(df, 'hip')

# проверка
#№genres_list = df['genre_name'].unique()
#print(find_genre('hip'))

#print(df.info())
