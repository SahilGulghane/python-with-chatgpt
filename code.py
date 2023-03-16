import speech_recognition as sr
from gtts import gTTS
import openai
from pygame import mixer
import time
import smtplib, ssl
import os
import var

r = sr.Recognizer()
my_mic = sr.Microphone(device_index=0)  # my device index is 0
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source)  # reduce noise
    audio = r.listen(source)  # take voice input from the microphone

# chat-gpt key
openai.api_key = var.key
# module usage
model_engine = "text-davinci-003"
prompt = r.recognize_google(audio)
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
)
response = completion.choices[0].text
language = 'en'
# convert  text to mp3 file
myobj = gTTS(text=response, lang=language, slow=False)
myobj.save("welcome.mp3")
# Playing the converted file
mixer.init()
mixer.music.load("welcome.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)

language = 'en'
# convert  text to mp3 file
myobj = gTTS(text="response collected what to want to do email , print in console , copy or should i repeat",
             lang=language, slow=False)
myobj.save("welcome2.mp3")
mixer.init()
mixer.music.load("welcome2.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)

with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source)  # reduce noise
    audio = r.listen(source)  # take voice input from the microphone
    my_string = r.recognize_google(audio)
# to print
if my_string == "print in console":
    print(response)

# to email
elif my_string == "mail me":
        language = 'en'
        # convert  text to mp3 file
        myobj = gTTS(text="please enter receiver email address",
                     lang=language, slow=False)
        myobj.save("welcome23.mp3")
        mixer.init()
        mixer.music.load("welcome23.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)
        s = input("email id:")
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "sahilgulghane22@gmail.com"
        receiver_email = s
        password = var.gkey
        message = response
        Subject: "Hi there"
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("done")

# to repeat
elif my_string == "repeat":
    mixer.init()
    mixer.music.load("welcome.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

# to copy to clipboard
elif my_string == "copy":
    def addToClipBoard(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)
    addToClipBoard(response)
