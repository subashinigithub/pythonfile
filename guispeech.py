from tkinter import font
import webbrowser as wb
import speech_recoginition as sr
import pyttsx3
def main1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something.......")
        audio=r.listen(source)
    try:
        print("Recognizing Now....")
        text=str(r.recognize_google(audio))
        label_font=font.Font(weight="bold",family='Times New Roman',size=10)
        