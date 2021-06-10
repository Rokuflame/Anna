import webbrowser
import json
import pyttsx3
from random import choice
import speech_recognition as sr
import wikipedia
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

def play_greetings(args: list):
    greetings = ["Привет", "Приветик", "Приветствую", "Здраствуй господин", "что здесь забыл!"]
    engine.say(choice(greetings))

def play_farewell_and_quit(args: list):
    farewell_and_quit = ["Пока", "Свидимся", "Жду тебя повелитель", "Пойду позалипаю", "Ну и проваливай"]
    engine.say(choice(farewell_and_quit))

def search_for_video_on_youtube(args: list):
    search = " ".join(args)
    webbrowser.get().open(f"https://www.youtube.com/results?search_query={search}")

def search_for_definition_on_wikipedia(args: list):
    wikipedia.set_lang('ru')
    ny = wikipedia.page(args)
    engine.say(wikipedia.summary(args, sentences=3))
    webbrowser.get().open(ny.url)


def execute_command_with_name(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды и аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в метод
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass    # print("Command not found")

# перечень команд для использования (качестве ключей словаря используется hashable-тип tuple)
# в качестве альтернативы можно использовать JSON-объект с намерениями и сценариями
# (подобно тем, что применяют для чат-ботов)
commands = {
    ("hello", "hi", "morning", "привет", "приветики", "приветствую", "здраствуй"): play_greetings,
    ("bye", "goodbye", "quit", "exit", "stop", "пока", "покеда", "прощай"): play_farewell_and_quit,
    ("search", "google", "find", "найди"): "search_for_term_on_google",
    ("video", "youtube", "watch", "видео", "ютьюб", "ютуб", "ютюб"): search_for_video_on_youtube,
    ("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
    ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): "get_translation",
    ("language", "язык"): "change_language",
    ("weather", "forecast", "погода", "прогноз"): "get_weather_forecast",
    ("facebook", "person", "run", "пробей", "контакт"): "run_person_through_social_nets_databases",
    ("toss", "coin", "монета", "подбрось"): "toss_coin",
}



def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5)    # настройка посторонних шумов
        print("Слушаю...")
        audio = r.listen(source)
    print("Услышала.")
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print(f'------------------------{query.lower()}----------------------')
        voice_input = query.lower().split(' ')
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        execute_command_with_name(command, command_options)
    except:
        print("Error")



if __name__ == '__main__':
    while True:
        record_volume()
        engine.runAndWait()
        engine.stop()



