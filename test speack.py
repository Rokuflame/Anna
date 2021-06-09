import pyttsx3

engine = pyttsx3.init() # создание объекта

""" RATE"""
rate = engine.getProperty('rate')   # получение сведений о текущей скорости речи
print(rate)                         # печать текущей скорости речи
engine.setProperty('rate', 125)     # установка новой скорости голоса

"""VOLUME"""
volume = engine.getProperty('volume')   # получение информации о текущем уровне громкости (min = 0 и max = 1)
print(volume)                           # печать текущей уровень громкости
engine.setProperty('volume', 1.0)       # установка уровня громкости от 0 до 1

"""VOICE"""
# Задать голос по умолчанию
voices = engine.getProperty('voices')

engine.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        engine.setProperty('voice', voice.id)

engine.say('Привет мир: ' )
engine.runAndWait()
engine.stop()