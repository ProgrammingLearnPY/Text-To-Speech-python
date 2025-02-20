import tkinter as tk
from tkinter import messagebox
import gtts
import pygame


def textToSpeech():
    text = entry.get("1.0", tk.END).strip()
    if text == "":
        messagebox.showerror("Error", "Please enter some text!!!")
        return
    
    try:
        tts = gtts.gTTS(text, lang="en")
        fileName = "speech.mp3"
        tts.save(fileName)
        pygame.mixer.init()
        pygame.mixer.music.load(fileName)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

root = tk.Tk()
root.title("Text-To-Speech - ProgrammingLearn")
root.geometry("400x300")
root.resizable(False, False)

lable = tk.Label(root, text="Enter your text : ")
lable.pack(pady=10)

entry = tk.Text(root, height=5, width=40)
entry.pack(pady=10)

speakButton = tk.Button(root, text="Play Speech", bg="green", fg="white", command=textToSpeech)
speakButton.pack(pady=10)

root.mainloop()