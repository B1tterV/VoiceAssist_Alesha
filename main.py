import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import datetime
import locale
import re
import calc
# import music

locale.setlocale(locale.LC_TIME, 'ru_RU')
CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
VISUAL_STUDIO_PATH = 'C:/Users/Nithen/AppData/Local/Programs/Microsoft VS Code/Code.exe'
STEAM_PATH = 'C:/Program Files (x86)/steam/Steam.exe'
wikipedia.set_lang("ru")
alex = pyttsx3.init()

rate = alex.getProperty('rate')  # Скорость произношения
alex.setProperty('rate', rate - 20)

volume = alex.getProperty('volume')  # Громкость голоса
alex.setProperty('volume', volume - 0.8)

voices = alex.getProperty('voices')

alex.setProperty('voice', 'ru')  # Задать голос по умолчанию

for voice in voices:  # Попробовать установить предпочтительный голос
    if voice.name == 'Pavel':
        alex.setProperty('voice', voice.id)
        break


def say_text(text):
    print(text)
    alex.say(text)
    alex.runAndWait()


def wait_command():
    r = sr.Recognizer()
    r.energy_threshold = 100
    with sr.Microphone(device_index=2) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=1)  # настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        print(f'Вы сказали: {query.lower()}')
    except Exception as e:
        print(e)
        print("Не могу распознать ваш голос.")
        return "None"
    return query


if __name__ == '__main__':

    clear = lambda: os.system('cls')
    clear()

    while True:
        query = wait_command().lower()

        if 'алекс' in query:
            query = query.replace("алекс", "")

            if 'википедия' in query:
                say_text('Ищу в википедии...')
                query = query.replace("википедия", "")
                try:
                    wikiResults = wikipedia.summary(query, sentences=3)
                    say_text("Согласно Википедии ")
                    print(wikiResults)
                    say_text(wikiResults)
                except Exception as e:
                    print(e)
                    say_text("Я нашел несколько результатов. Скажите более подробно что вы ищите.")

            elif 'открой' in query or 'запусти' in query:
                query = query.replace("открой", "")
                query = query.replace("запусти", "")

                if 'youtube' in query:
                    say_text("Приятного просмотра\n")
                    webbrowser.get(CHROME_PATH).open_new_tab("youtube.com")

                elif 'google' in query:
                    say_text("Открываю\n")
                    webbrowser.get(CHROME_PATH).open_new_tab("google.com")

                elif 'вижак' in query or "visual studio" in query:
                    os.startfile(VISUAL_STUDIO_PATH)

                elif 'стим' in query or "steam" in query:
                    os.startfile(STEAM_PATH)

            elif 'скажи' in query:
                query = query.replace("скажи", "")

                if 'дату' in query:
                    strTime = datetime.datetime.now().strftime("%A %d. %B %Y")
                    say_text(f"Сейчас {strTime}")

                elif 'время' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    say_text(f"Сейчас {strTime}")

            elif 'посчитай' in query:
                query = query.replace('посчитай', '')

                if '+' in query or 'плюс' in query:

                    x = re.findall('[0-9]+', query)
                    print(f'result - {x}')

                    say_text(calc.plus(int(x[0]), int(x[1])))