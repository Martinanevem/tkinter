import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

import os

# Create a Tkinter window
window = tk.Tk()
window.title("Hangman")

# Initialize game variables
szo = "hangman"  # The word to be guessed
megtalalt_betuk = []
rossz_betuk = []
maxTippek = 6  # Maximum number of allowed guesses
jelenlegi_tippek = 0







label_word = tk.Label(window, text="_ " * len(szo))
label_word.pack()

label_attempts = tk.Label(window, text="Attempts: 0/" + str(maxTippek))
label_attempts.pack()

entry_guess = tk.Entry(window)
entry_guess.pack()

def update_img():
    global jelenlegi_tippek

def check_guess():
    global jelenlegi_tippek


    tipp = entry_guess.get()



    if len(tipp) != 1:
        label_feedback.config(text="Please enter a single letter!")
    elif tipp in megtalalt_betuk or tipp in rossz_betuk:
        label_feedback.config(text="You have already guessed that letter!")
    else:
        if tipp == szo:
            vege(False)
        elif tipp in szo:
            megtalalt_betuk.append(tipp)
            update_word_label()
        else:
            rossz_betuk.append(tipp)
            jelenlegi_tippek += 1
            update_img() #hívja meg!
            label_attempts.config(text="Attempts: {}/{}".format(jelenlegi_tippek, maxTippek))
            if jelenlegi_tippek == maxTippek:
                vege(True)

        entry_guess.delete(0, tk.END)
    
    update_img()

def update_word_label():
    displayed_word = ""
    for letter in szo:
        if letter in megtalalt_betuk:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    label_word.config(text=displayed_word)

def vege(vesztett):
    if vesztett:
        label_feedback.config(text="You lost! The word was '{}'".format(szo))
    else:
        label_feedback.config(text="Congratulations! You guessed the word '{}'".format(szo))

    entry_guess.config(state=tk.DISABLED)
    button_guess.config(state=tk.DISABLED)

# Create Tkinter button and label for feedback
button_guess = tk.Button(window, fg="WHITE", bg="BLACK", text="Tippelek", command=check_guess)
button_guess.pack()

label_feedback = tk.Label(window, text="")
label_feedback.pack()

# Start the Tkinter event loop
window.mainloop()
