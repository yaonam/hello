import time
import speech_recognition as sr

def callback(recognizer, audio):
    try:
        print("Google thinks you said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print('------------')
        # print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r1 = sr.Recognizer()
# r2 = sr.Recognizer()
# r1.pause_threshold = 0.5
m = sr.Microphone()
with m as source:
    print('Calibrating...')
    r1.adjust_for_ambient_noise(source, duration = 0.7) # Calibrate
    # r2.adjust_for_ambient_noise(source, duration = 0.7) # Calibrate
    print('Listening...')

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r1.listen_in_background(m, callback, phrase_time_limit=2)
# `stop_listening` is now a function that, when called, stops background listening

# # do some unrelated computations for 5 seconds
# for _ in range(50): time.sleep(0.1)  # we're still listening

# # calling this function requests that the background listener stop listening
# stop_listening(wait_for_stop=False)

# do some more unrelated things
while True: pass  # we're not listening anymore

# while True:
#     listen = r1.listen_in_background(m, callback)
#     time.sleep(2)
#     listen(wait_for_stop=False)
    # listen = r2.listen_in_background(m, callback)
    # time.sleep(2)
    # listen(wait_for_stop=False)
    # l2 = r.listen_in_background(m, callback)
    # time.sleep(2)
    # l2(wait_for_stop=False)