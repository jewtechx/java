import cowsay
import pyttsx3

engine = pyttsx3.init()
text = input("Enter script: ")
cowsay.cow(text)
engine.say(text)
engine.runAndWait()
