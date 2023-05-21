
from tkinter import *
from menu import *


def start(nev, adatok, titkos_adatok):

    ablak1=Tk()
    ablak1.title("Próba")
    ablak1.minsize(width=550,height=350)

    

    

    

    

    if nev == "Vendég" or nev == "" or nev == None: bejelentkezve = False
    else: bejelentkezve = True

    menu(ablak1, bejelentkezve, titkos_adatok)

    fnev = Label(ablak1, text=f"Üdvözöllek, {nev}!").grid(row=1, column=0)
    if not bejelentkezve:
        
        warn_szoveg_vendeg = Label(ablak1, text=f"Vendég: adataid nem lesznek mentve az adatbázisba!").grid(row=2, column=0)
    
    
    
    
    ranglista_szoveg = Label(ablak1, text="----- Jelenlegi ranglista -----", font=('Helvetica bold', 16)).grid(padx=120,row=5, column=0, columnspan=6)
    row = 7
    for key, value in sorted(adatok.items(), key=lambda x: x[1], reverse=True):
        label_key = Label(ablak1, text=key)
        label_key.grid(row=row, column=0)

        label_value = Label(ablak1, text=value)
        label_value.grid(row=row, column=1)

        row += 1

    
    ablak1.mainloop()