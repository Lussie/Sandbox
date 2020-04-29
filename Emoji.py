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

# выведем табицу на экран
# print(df)
print('|{: ^20}|{: ^20}|{: ^20}|{: ^20}|'.format('name', 'emojixpress', 'instagram', 'twitter'))
print('-------------------------------------------------------------------------------------')
for row in df:
        print('|{: >20.2f}|{: >20.2f}|{: >20.2f}|{: >20.2f}|'.format(int(row[0]), int(row[1]), int(row[2]), int(row[3])))
print()

# количество всех эмодзи в EmojiXpress в миллионах
emojixpress_total = 1720

# количество всех эмодзи в Twitter в миллионах
twitter_total = 24500


# Функция считает сумму всех выбранных эмодзи в конкретном источнике (столбце)
def emoji_count(df, column):
    emoji_count = 0
    for i in df.loc[:, column]:
        emoji_count += i
    return emoji_count


print('Доля выбранных эмодзи в EmojiXpress: {:.1%}'.format(emoji_count(df, 'emojixpress') / emojixpress_total))
print('Доля выбранных эмодзи в Twitter: {:.1%}'.format(emoji_count(df, 'twitter') / twitter_total))
