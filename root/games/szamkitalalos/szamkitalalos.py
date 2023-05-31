import tkinter as tk

import random

#globalis valtozok
number=0
attempts=0
difficulty=0

#játék
def generalas():
    #random szam alapjan kiirja a random szamnot
    global number
    number = random.randint(1,difficulty)

def kitalaltae():
    global attempts
    #input
    guess=int(entry.get())
    entry.delete(0, tk.END)
    #probalkozasok hozzaadasa
    attempts+=1
    #osszehasonlitas
    if guess==number:
        #nyert
        label.config(text=f'Kitaláltad a számot ennyi próbálkozás után:{attempts}')
        #vege
        entry.config(state=("disabled"))
       
    elif guess<number:
        #kisebb
        label.config(text="A számod kisebb, mint a szám. Próbáld újra!")
    elif guess>number:
         label.config(text="A számod nagyobb, mint a szám. Próbáld újra!")

    def nehezsegvaltas():
        global difficulty
    global attempts
    
    #reset
    attempts=0
    generalas()
    
    
def beallitas():
    global settings, spin 
    settings=tk.Toplevel(root)
    settings.title("Beállítások")
    settings.geometry("200x100")
    tk.Label(settings,text="A nehézség:").pack()
    spin= tk.Spinbox(settings,from_=10, to=100)
    spin.pack()
    difficulty=int(spin.get())
    tk.Button(settings,text="Alkalmazás",command=nehezsegvaltas).pack()
    label.config(text=(f'A nehézség jelenleg: {difficulty}'))
    entry.config(state="normal")

root=tk.Tk()
root.title("Számkitaláló")
root.geometry("300x200")
label=tk.Label(root,text=f'Adj egy számot 1 és {difficulty} között!')
entry=tk.Entry(root)
entry.pack()
Check=tk.Button(root,text="Csekkol", command=kitalaltae)
Check.pack()
menu=tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="Beállítások",command=nehezsegvaltas)

root.mainloop()