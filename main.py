import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import pyautogui
import os
import subprocess
import nltk
import sys
from chat import chatbot
 
engine = pyttsx3.init()
r = sr.Recognizer()

 
engine.setProperty('rate', 150)  
engine.setProperty('volume', 0.9)  
 
engine.say("Hello, I am RoboPy, How can I help You?")
print("RoboPy:Hello, I am RoboPy, How can I help You?")
engine.runAndWait()  

def tasks(text):
    pass_text = nltk.sent_tokenize(text)
    textarr = [nltk.word_tokenize(sentence) for sentence in pass_text]
     
    for words in textarr:
     
     if "roblox" in words and "open" in words:
        print("RoboPy:Opening the roblox....")
        engine.say("Opening the roblox....")
        engine.runAndWait()
        path_to_application = 'C:\\Users\\inno\\AppData\\Rhaoaming\\Microsoft\\Windows\\Start Menu\\Programs\\Roblox\\Roblox Player.lnk'
        os.system('start "" "' + path_to_application + '"')
     else:
        response = chatbot(text)
        print("RoboPy:",response)
        engine.say(response)
        engine.runAndWait()
    
while True:
    print("listening....")
    with sr.Microphone() as source:
     audio_text = r.listen(source)
     recognize_text = r.recognize_google(audio_text, language='en-IN')
     
     
    try:
      print("You:",recognize_text)
      if "close" in recognize_text and "chat" in recognize_text:
       print("RoboPy:Ending The chat..........")
       engine.say("Ending the chat....")
       engine.runAndWait()
       break
      else:
       tasks(recognize_text)
    except:
      print("RoboPy:Sorry, I did not get that")
      engine.say("sorry, I did not get that")
      engine.runAndWait()
 
 

  
