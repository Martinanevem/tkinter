from tkinter import *
from menu import *
from tabulate import tabulate

def start(nev, adatok, titkos_adatok):
    ablak1 = Tk()
    ablak1.title("Próba")
    ablak1.minsize(width=250, height=350)

    if nev == "Vendég" or nev == "" or nev == None:
        bejelentkezve = False
    else:
        bejelentkezve = True

    menu(ablak1, bejelentkezve, titkos_adatok)

    if bejelentkezve:
        fnev = Label(ablak1, text=f"Üdvözöllek, {nev}!")
        fnev.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10) 
        warn_szoveg = Label(ablak1, text=f"Adataid mentve lesznek az adatbázisba!", bg="GREEN")
        warn_szoveg.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

    if not bejelentkezve:
        fnev = Label(ablak1, text=f"{nev} vagy!")
        fnev.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
        warn_szoveg_vendeg = Label(ablak1, text=f"Adataid nem lesznek mentve az adatbázisba!", bg="RED")
        warn_szoveg_vendeg.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

    ranglista_szoveg = Label(ablak1, text="Top helyezés:", font=('Helvetica bold', 16))
    ranglista_szoveg.grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)

    rows = [[key, value] for key, value in sorted(adatok.items(), key=lambda x: x[1], reverse=True)]
    table_str = tabulate(rows, headers=["Játékos", "Pontok"], tablefmt="org")

    label_table = Label(ablak1, text=table_str, justify="left", font=("Courier", 10))
    label_table.grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 5), padx=(35, 0))

    ablak1.mainloop()
