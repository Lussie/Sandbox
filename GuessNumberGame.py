# Настройки
print('Задай границы загадываемого числа')
a = int(input('Нижняя граница = '))
b = int(input('Верхняя граница = '))
print(f'Загадай число от {a} до {b}...')

# Определяем функцию, которая будет печатать правила
def print_rules():
    rules = '''
    Если я угадаю, напиши '=',
    если твое число меньше, напиши '<',
    если твое число больше, напиши '>'.
    И нажми на Enter.
    '''
    print()
    print(rules)
    print()

# Даем время подумать
import time
time.sleep(2)
print('Загадал?')
time.sleep(2)
print('Тогда начинаем!')
time.sleep(2)

print_rules()

x = 0

while True:
    x = int(a + (b-a)/2)
    print(x)
    N = input()
    if N == '>':
        a = x
    if N == '<':
        b = x
    if N == '=':
        print('Ура! Угадал!')
        break

print(f'Ты загадал число {x}')