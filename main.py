# Я призываю тебя, прийди жи на мой зов
import speech_recognition
import os


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Читай репчик у тебя 10 секунд для этого")
            audio = recognizer.listen(microphone, 10, 10)

            with open("result-record.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("А куда?")
            return

        # использование online-распознавания через Google
        try:
            print("Твои слова:")
            recognized_data = recognizer.recognize_google(
                audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("А откуда?")

    return recognized_data


if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        voice_input = record_and_recognize_audio()
        os.remove("result-record.wav")

        print(voice_input)
