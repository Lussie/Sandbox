# Поиграем с данными, вычислим разные показатели

# Для начала создадим таблицу со всеми известными показателями:



total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_native = 908.7
chinese_web_part = 0.017

english_speakers = 1121
english_native = 378.2
english_web_part = 0.539

russian_speakers = 264.3
russian_native = 153.9
russian_web_part = 0.061



german_native = 76.0


top3_total = english + russian + german

print(chinese - top3_total)



chinese_speakers_part = chinese_speakers / total_speakers
chinese_web_sites = chinese_web_part * total_web
chinese_index = 1000 * chinese_web_sites / chinese_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(chinese_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(chinese_index))
print()

english_speakers_part = english_speakers / total_speakers
english_web_sites = english_web_part * total_web
english_index = 1000 * english_web_sites / english_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(english_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(english_index))
print()

russian_speakers_part = russian_speakers / total_speakers
russian_web_sites = russian_web_part * total_web
russian_index = 1000 * russian_web_sites / russian_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(russian_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(russian_index))
print()
