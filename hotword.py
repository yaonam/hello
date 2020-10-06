# Uses SnowBoy to detect custom hotwords
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Caibrating...")
    r.adjust_for_ambient_noise(source, duration = 1)
    print("Listening...")
    while True:
        audio = r.listen(source, snowboy_configuration=('/voice models', ['Elim.pmdl']))
        print("I heard 'Elim!'")