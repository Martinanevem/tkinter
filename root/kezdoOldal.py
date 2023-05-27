from tkinter import *
from AUTH import *
from menu import *
from kezdes import start

import os

def keep_window_on_top(window):
    window.attributes('-topmost', True)



def bejelentkezes():
    ablak1.destroy()
    authAblak(bejelentkezes=True)
def regisztracio():
    authAblak(regisztracio=True)
def vendeg():
    ablak1.destroy()
    authAblak(regisztracio=False)






ablak1=Tk()
keep_window_on_top(ablak1)
ablak1.title("Folytatás mint...")
ablak1.minsize(width=400,height=200)
ablak1.columnconfigure(0, weight=1)
ablak1.columnconfigure(3, weight=1)
ablak1.rowconfigure(0, weight=1)
ablak1.rowconfigure(3, weight=1)

frame1 = Frame(ablak1, highlightbackground="grey", highlightthickness=2)
var=StringVar()
mondat=Button(frame1,textvariable=var, font=('Helvetica bold', 16), command=bejelentkezes)
var.set("Bejelentkezés")
frame1.grid(row=2,column=0, columnspan=4, pady=5, sticky="N")
mondat.grid(row=2,column=0, columnspan=4, sticky="N")
frame2 = Frame(ablak1, highlightbackground="grey", highlightthickness=2)
var1=StringVar()
mondat1=Button(frame2,textvariable=var1, font=('Helvetica bold', 16), command=regisztracio)
var1.set("Regisztráció")
frame2.grid(row=3,column=0, columnspan=4, pady=5, sticky="N")
mondat1.grid(row=3,column=0, columnspan=4, sticky="N")

frame3= Frame(ablak1, highlightbackground="grey", highlightthickness=2)
var2=StringVar()
mondat2=Button(frame3,textvariable=var2, font=('Helvetica bold', 14), command=vendeg)
var2.set("Folytatás vendégként")
frame3.grid(row=5,column=0, columnspan=4, pady=5, sticky="N")
mondat2.grid(row=5,column=0)


ablak1.mainloop()