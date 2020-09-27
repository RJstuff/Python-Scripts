import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volumn', 0.9)

engine.say("Hello world")
engine.say("Testing voice")

engine.runAndWait()
