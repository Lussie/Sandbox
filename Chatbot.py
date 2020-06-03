BOT_CONFIG = {

    'intents': {

        'hello': {
            'examples': ['Привет', 'Добрый день', 'Здравствуйте!', 'Шалом'],
            'responses': ['Привет, юзер!', 'Здравствуй']
        },
        'goodbye': {
            'examples': ['Пока', 'Всего доброго', 'До свидания'],
            'responses': ['Пока', 'Счастливо!']
        },
        'thanks': {
            'examples': ['Спасибо', 'Спасибо большое!', 'Сэнкс', 'Благодарю!'],
            'responses': ['Вам спасибо!'],
        },
        'whatcanyoudo': {
            'examples': ['Что ты умеешь?', 'Расскажи что умеешь'],
            'responses': ['Отвечать на вопросы. Просто напиши )']
        },
        'name': {
            'examples': ['Как тебя зовут?', 'Твое имя?'],
            'responses': ['Меня зовут бот. Просто бот.']
        },
        'weather': {
            'examples': ['Какая погода в Москве?', 'Какая погода?'],
            'responses': ['Погода так себе...']
        }
    },

    'failure_frases': [
        'Я не знаю, что ответить',
        'Не поняла вас',
        'Простите, не поняла вас',
        'Я на такое не умею отвечать',
        'Переформулируйте, пожалуйста'
    ]
}

import random
from nltk.metrics.distance import edit_distance

def get_intent(text):
    intents = BOT_CONFIG['intents']

    for intent, value in intents.items():
        for example in value['examples']:

            # боремся с опечатками:
            # 1. приводим все слова введенные и в примерах к написанию строчными буквами,
            # 2. рассчитываем растояние Ливенштейна между введенным текстом и примерами
            dist = edit_distance(text.lower(), example.lower())
            l = len(example)
            similarity = 1 - dist / l
            if similarity > 0.6:
                return intent

def get_response_by_intent(intent):
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])

def get_failurefrase():
    return random.choice(BOT_CONFIG['failure_frases'])


def generate_answer(text):
    # NLU
    intent = get_intent(text)

    # Make Answer

    # by script
    if intent:
        response = get_response_by_intent(intent)
        return response

    # use generative model
    # ToDo

    # use stub
    failure_phrase = get_failurephrase()
    return failure_phrase

while True:
    text = input('Введите вопрос: ')
    answer = generate_answer(text)
    print(answer)