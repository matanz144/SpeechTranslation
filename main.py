import speech_recognition as sr
from googletrans import Translator
import gtts
import pydub
import winsound
from pydub.playback import play


def speak(my_lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        winsound.Beep(1000, 500)
        audio_input = r.listen(source)
        try:
            to_translate = r.recognize_google(audio_input, language=my_lang)
            winsound.Beep(500, 500)
            print('You said: {}'.format(to_translate))
            return to_translate
        except Exception as e:
            print('Could not recognize your speech...')
            print(e)


def translate(text, dest_language):

    translator = Translator()
    res = translator.translate(text, dest=dest_language)
    return res.text


def speechBack(text):
    filename = 'output.mp3'
    tts = gtts.gTTS(text=text, lang='en')
    tts.save(filename)
    sound = pydub.AudioSegment.from_mp3(file=filename)
    play(sound)

