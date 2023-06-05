import tkinter as tk
from math import sqrt

def gomb_megnyomas(szam):
    aktualis_kifejezes = kifejezes.get()
    kifejezes.set(aktualis_kifejezes + str(szam))

def szamitas():
    aktualis_kifejezes = kifejezes.get()
    try:
        eredmeny = eval(aktualis_kifejezes)
        kifejezes.set(str(eredmeny))
    except:
        kifejezes.set("Hiba")

def torles():
    kifejezes.set("")

def torles_egy():
    aktualis_kifejezes = kifejezes.get()
    kifejezes.set(aktualis_kifejezes[:-1])

def negyzetgyok():
    aktualis_kifejezes = kifejezes.get()
    try:
        eredmeny = sqrt(float(aktualis_kifejezes))
        kifejezes.set(str(eredmeny))
    except:
        kifejezes.set("Hiba")

def hatvanyozas():
    aktualis_kifejezes = kifejezes.get()
    kifejezes.set(aktualis_kifejezes + "**")

def gomb_letrehozas(root, szoveg, sor, oszlop, szelesseg=5, magassag=2, parancs=None):
    gomb = tk.Button(root, text=szoveg, width=szelesseg, height=magassag, bg="black", fg="white", font=("Arial", 16), command=parancs)
    gomb.grid(row=sor, column=oszlop, padx=5, pady=5)

root = tk.Tk()
root.title("Számológép")

kifejezes = tk.StringVar()
kifejezes_bemenet = tk.Entry(root, textvariable=kifejezes, bg="white", fg="black", font=("Arial", 16), justify="right", width=15)
kifejezes_bemenet.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

gomb_letrehozas(root, "7", 1, 0, parancs=lambda: gomb_megnyomas(7))
gomb_letrehozas(root, "8", 1, 1, parancs=lambda: gomb_megnyomas(8))
gomb_letrehozas(root, "9", 1, 2, parancs=lambda: gomb_megnyomas(9))
gomb_letrehozas(root, "/", 1, 3, parancs=lambda: gomb_megnyomas("/"))
gomb_letrehozas(root, "*", 1, 4, parancs=lambda: gomb_megnyomas("*"))

gomb_letrehozas(root, "4", 2, 0, parancs=lambda: gomb_megnyomas(4))
gomb_letrehozas(root, "5", 2, 1, parancs=lambda: gomb_megnyomas(5))
gomb_letrehozas(root, "6", 2, 2, parancs=lambda: gomb_megnyomas(6))
gomb_letrehozas(root, "//", 2, 3, parancs=lambda: gomb_megnyomas("//"))
gomb_letrehozas(root, "-", 2, 4, parancs=lambda: gomb_megnyomas("-"))

gomb_letrehozas(root, "1", 3, 0, parancs=lambda: gomb_megnyomas(1))
gomb_letrehozas(root, "2", 3, 1, parancs=lambda: gomb_megnyomas(2))
gomb_letrehozas(root, "3", 3, 2, parancs=lambda: gomb_megnyomas(3))
gomb_letrehozas(root, "%", 3, 3, parancs=lambda: gomb_megnyomas("%"))
gomb_letrehozas(root, "+", 3, 4, parancs=lambda: gomb_megnyomas("+"))

gomb_letrehozas(root, "√", 4, 0, parancs=negyzetgyok)
gomb_letrehozas(root, "0", 4, 1, parancs=lambda: gomb_megnyomas(0))
gomb_letrehozas(root, "**", 4, 2, parancs=hatvanyozas)
gomb_letrehozas(root, ".", 4, 3, parancs=lambda: gomb_megnyomas("."))
gomb_letrehozas(root, "=", 4, 4, parancs=szamitas)

gomb_letrehozas(root, "DEL", 1, 5, szelesseg=4, magassag=1, parancs=torles_egy)
gomb_letrehozas(root, "CLR", 2, 5, szelesseg=4, magassag=1, parancs=torles)

root.mainloop()
