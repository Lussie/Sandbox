# Какие эмодзи наиболее популярны в соцсетях?
# Проанализируем частоту использования эмодзи на разных платформах.

import pandas as pd


# Создаем таблицу, с которой будем работать
# Количество в млн.
data = [['Grinning', 2.26, 1.02, 87.3],
        ['Beaming', 19.1, 1.69, 150],
        ['ROFL', 25.6, 0.774, 0],
        ['Tears of Joy', 233, 7.31, 2270],
        ['Winking', 15.2, 2.36, 264],
        ['Happy', 22.7, 4.26, 565],
        ['Heart Eyes', 64.6, 11.2, 834],
        ['Kissing', 87.5, 5.13, 432],
        ['Thinking', 6.81, 0.636, 0],
        ['Unamused', 6, 0.236, 478],
        ['Sunglasses', 4.72, 3.93, 198],
        ['Loudly Crying', 24.7, 1.35, 654],
        ['Kiss Mark', 21.7, 2.87, 98.7],
        ['Two Hearts', 10, 5.69, 445],
        ['Heart', 118, 26, 1080],
        ['Heart Suit', 3.31, 1.82, 697],
        ['Thumbs Up', 23.1, 3.75, 227],
        ['Shrugging', 1.74, 0.11, 0],
        ['Fire', 4.5, 2.49, 150],
        ['Recycle', 0.0333, 0.056, 932]]
columns = ['name', 'emojixpress', 'instagram', 'twitter']
df = pd.DataFrame(data = data, columns = columns)

# количество всех эмодзи в EmojiXpress в миллионах
emojixpress_total = 1720

# количество всех эмодзи в Twitter в миллионах
twitter_total = 24500


# Функция считает сумму всех выбранных эмодзи в конкретном источнике (столбце)
def emoji_sum(df, column):
    emoji_sum = 0
    for i in df.loc[:, column]:
        emoji_sum += i
    return emoji_sum

# Функция считает, сколько в среднем сообщений с топовыми эмодзи отправляются в конкретном источнике (столбце)
def emoji_mean(df, column):
        return emoji_sum(df, column) / len(data)


# df.info()
# print(df)
# print()

print('Доля выбранных эмодзи в EmojiXpress: {:.1%}'.format(emoji_sum(df, 'emojixpress') / emojixpress_total))
print('Доля выбранных эмодзи в Twitter: {:.1%}'.format(emoji_sum(df, 'twitter') / twitter_total))
print()
print('Сколько всего топовых эмодзи отправляется в EmojiXpress (в миллионах): {: .2f}'.format(emoji_sum(df, 'emojixpress')))
print('Сколько всего топовых эмодзи отправляется в Instagram (в миллионах): {: .2f}'.format(emoji_sum(df, 'instagram')))
print('Сколько всего топовых эмодзи отправляется в Twitter (в миллионах): {: .2f}'.format(emoji_sum(df, 'twitter')))
print()
print('Сколько в среднем (в миллионах) сообщений с топовыми эмодзи отправляются в разных источниках:')
print()
print('Emojixpress, млн. | Instagram, млн. | Twitter, млн.')
print('---------------------------------------------------')
print('{: ^16.2f} | {: ^14.2f} | {: ^12.2f}'.format(emoji_mean(df, 'emojixpress'), emoji_mean(df, 'instagram'), emoji_mean(df, 'twitter')))
print()
print('Cоотношение количества конкретного эмодзи в Твиттере к его количеству в Instagram:')
print()
print('Название эмодзи  | Соотношение Твиттер/Instagram')
print('------------------------------------------------')
for row in data:
    print('{: <16} | {: >29.2f}'.format(row[0], (row[3] / row[2])))

# таблица с общей суммой каждого эмодзи, отсортированная по убыванию

for i in range(len(data)):
    data[i].append(data[i][1] + data[i][2] + data[i][3])

data.sort(key=lambda row: row[4], reverse=True)

print()
print('Cуммарное количество использований на всех платформах')
print()
print('Название эмодзи  | Суммарное использование, млн.')
print('------------------------------------------------')
for row in data:
    print('{: <16} | {: >29.2f}'.format(row[0], row[4]))

# рассчитываем индекс использования

emojixpress_mean = 0
instagram_mean = 0
twitter_mean = 0
for row in data:
    emojixpress_mean += row[1]
    instagram_mean += row[2]
    twitter_mean += row[3]

emojixpress_mean /= len(data)
instagram_mean /= len(data)
twitter_mean /= len(data)

for i in range(len(data)):
    data[i].append(
        data[i][1] / emojixpress_mean +
        data[i][2] / instagram_mean +
        data[i][3] / twitter_mean
    )


data.sort(key=lambda row: row[5], reverse=True)     # сортируем по новому столбцу по убыванию

print()
print('Название эмодзи  | Индекс использования')
print('---------------------------------------')
for row in data[:5]:    # выводим только первые пять
    print('{: <16} | {: >20.2f}'.format(row[0], row[5]))
print()
print('Выводы:')
print('- Большинство используемых эмодзи связаны с положительными эмоциями')
print('- На разных платформах самые популярные эмодзи похожи, хотя и может различаться их порядок в топе')
