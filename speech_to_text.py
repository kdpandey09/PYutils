import speech_recognition as s
r = s.Recognizer()
print("I am Listening you....")
# under work

with s.Microphone() as source:
    audio = r.listen(source)

    message = r.recognize_google(audio,language='eng-in', show_all =True)

    print(message)