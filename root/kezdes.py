
from tkinter import *
from menu import *

def start(nev):

    ablak1=Tk()
    ablak1.title("Próba")
    ablak1.minsize(width=550,height=350)

    

    

    

    

    if nev == "Vendég" or nev == "" or nev == None: bejelentkezve = False
    else: bejelentkezve = True

    menu(ablak1, bejelentkezve)

    fnev = Label(ablak1, text=f"Üdvözöllek, {nev}!").grid(row=1, column=0)
    if not bejelentkezve:
        
        warn_szoveg_vendeg = Label(ablak1, text=f"Vendég: adataid nem lesznek mentve az adatbázisba!").grid(row=2, column=0)
    ablak1.mainloop()

start("RandomCicaMica")