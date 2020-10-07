import speech_recognition as sr
import turtle
import time

# Set the keyword here
keyword = 'Maria'

r = sr.Recognizer()

def recognize(audio):
    # Takes an audio file and returns what Google thinks was said
    try:
        words = r.recognize_google(audio)
        print("Google SR thinks you said: '" + r.recognize_google(audio) + "'")
        return words
    except sr.UnknownValueError:
        print("Google SR could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google SR service; {0}".format(e))

def bgcolor(words):
    # Changes the turtle bgcolor based on the keyword
    toggle_time = 1.5
    if keyword in words:
        turtle.bgcolor('green')
        turtle.write(words, align='center', font=('Arial', 60, 'normal'))
        time.sleep(toggle_time)
    else:
        turtle.bgcolor('red')
        turtle.write(words, align='center', font=('Arial', 60, 'normal'))
        time.sleep(toggle_time)
    turtle.reset()
    turtle.bgcolor('gray')

turtle.Turtle()
turtle.bgcolor('gray')

with sr.Microphone() as source:
    print("Caibrating...")
    r.adjust_for_ambient_noise(source, duration = 0.5)
    # Continuously listen, recognize, and wait for user input
    while True:
        print("Say something!")
        audio = r.listen(source)
        print("Processing audio...")
        words = recognize(audio)
        if words != None: bgcolor(words)
        input('Press ENTER to continue...')