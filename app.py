import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()     # создание объекта

""" RATE"""
rate = engine.getProperty('rate')   # получение сведений о текущей скорости речи
print(rate)                         # печать текущей скорости речи
engine.setProperty('rate', 125)     # установка новой скорости голоса

"""VOLUME"""
volume = engine.getProperty('volume')   # получение информации о текущем уровне громкости (min = 0 и max = 1)
print(volume)                           # печать текущей уровень громкости
engine.setProperty('volume', 1.0)       # установка уровня громкости от 0 до 1

"""VOICE"""
voices = engine.getProperty('voices')   # Задать голос по умолчанию

engine.setProperty('voice', 'ru')

for voice in voices:
    if voice.name == 'Anna':
        engine.setProperty('voice', voice.id)   # Попробовать установить предпочтительный голос
engine.say('Привет мир: ' )


if __name__ == '__main__':

    engine.runAndWait()
    engine.stop()
