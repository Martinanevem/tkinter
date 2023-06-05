import tkinter as tk
import random
import pyrebase
import os

from time import sleep

config = {
    "apiKey": "AIzaSyCsLNLdZWJ5RtPeXSdOraiE83g87HOAW_w",
    "authDomain": "authfortkinter.firebaseapp.com",
    "projectId": "authfortkinter",
    "databaseURL": "https://authfortkinter-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "authfortkinter.appspot.com",
    "messagingSenderId": "132997432044",
    "appId": "1:132997432044:web:b3f5e167ae61b0f5c0dbc9"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

jelenleg_itt_vagy = os.path.dirname(os.path.abspath(__file__))
a_mappa_helye = os.path.join(jelenleg_itt_vagy, '..', '..')
a_mappa_helye = os.path.normpath(a_mappa_helye)
a_fajl_helye = os.path.join(a_mappa_helye, 'adatok.txt')
jelenlegi_user = open(a_fajl_helye, "r", encoding="UTF-8")

user = jelenlegi_user.readline()

FPS = 12
# -------------
OSSZES_PONT = 0  # adatbázis miatt!
SZEL = 640
MAG = 640
MERET = 50
HATTER = "#000000"

class Kigyo:
    def __init__(self):
        self.hossz = 3
        self.koord = [(150, 150), (150, 160), (150, 170)] # Modified coordinates
        self.negyzetek = []

    def kigyo_letrehozasa(self, v):
        for x, y in self.koord:
            negyzet = v.create_rectangle(
                x, y, x + MERET, y + MERET,
                fill="WHITE", tag="kigyo"
            )
            self.negyetek.append(negyzet)

class Etel:
    def __init__(self):
        x = random.randint(0, SZEL // MERET - 1) * MERET
        y = random.randint(0, MAG // MERET - 1) * MERET
        self.koord = [x, y]

        v.create_oval(x, y, x + MERET, y + MERET, fill="RED", tag="etel")

import tkinter as tk
import random
import pyrebase
import os

config = {
        "apiKey": "AIzaSyCsLNLdZWJ5RtPeXSdOraiE83g87HOAW_w",
        "authDomain": "authfortkinter.firebaseapp.com",
        "projectId": "authfortkinter",
        "databaseURL": "https://authfortkinter-default-rtdb.europe-west1.firebasedatabase.app/",
        "storageBucket": "authfortkinter.appspot.com",
        "messagingSenderId": "132997432044",
        "appId": "1:132997432044:web:b3f5e167ae61b0f5c0dbc9"
        }

firebase = pyrebase.initialize_app(config)
database = firebase.database()

jelenleg_itt_vagy = os.path.dirname(os.path.abspath(__file__))
a_mappa_helye = os.path.join(jelenleg_itt_vagy, '..', '..')
a_mappa_helye = os.path.normpath(a_mappa_helye)
a_fajl_helye = os.path.join(a_mappa_helye, 'adatok.txt')
jelenlegi_user = open(a_fajl_helye, "r", encoding="UTF-8")

user = jelenlegi_user.readline()

FPS = 12
# -------------
OSSZES_PONT = 0  # adatbázis miatt!
SZEL = 640
MAG = 480
MERET = 50
HATTER = "#000000"

class Kigyo:
    def __init__(self):
        self.hossz = 3
        self.koord = [(0, 0)] * self.hossz
        self.negyzetek = []

    def kigyo_letrehozasa(self, v):
        for x, y in self.koord:
            negyzet = v.create_rectangle(
                x, y, x + MERET, y + MERET,
                fill="WHITE", tag="kigyo"
            )
            self.negyzetek.append(negyzet)

class Etel:
    def __init__(self):
        x = random.randint(0, SZEL // MERET - 1) * MERET
        y = random.randint(0, MAG // MERET - 1) * MERET
        self.koord = [x, y]

        v.create_oval(x, y, x + MERET, y + MERET, fill="RED", tag="etel")

def kovetkezo_kor(k, e):
    global is_game_over
    if is_game_over:
        return

    x, y = k.koord[0]

    if i == "fel":
        y -= MERET
    elif i == "le":
        y += MERET
    elif i == "balra":
        x -= MERET
    elif i == "jobbra":
        x += MERET

    k.koord.insert(0, (x, y))

    negyzet = v.create_rectangle(x, y, x + MERET, y + MERET, fill="WHITE")
    k.negyzetek.insert(0, negyzet)

    if utkozes_vizsgalat(k):
        jatek_vege()
    else:
        if x == e.koord[0] and y == e.koord[1]:
            pont_novel()
            v.delete("etel")
            e = Etel()
        else:
            del k.koord[-1]
            v.delete(k.negyzetek[-1])
            del k.negyzetek[-1]

        ablak.after(1000 // FPS, kovetkezo_kor, k, e)

def utkozes_vizsgalat(k):
    x, y = k.koord[0]
    if x < 0 or x >= SZEL or y < 0 or y >= MAG or y < 0:
        jatek_vege()
    for testresz in k.koord[1:]:
        if x == testresz[0] and y == testresz[1]:
            jatek_vege()
    return False

def irany_valtoztatas(uj_irany):
    global i
    
    if uj_irany == 'balra' and i != 'jobbra':
        i = uj_irany
    elif uj_irany == 'jobbra' and i != 'balra':
        i = uj_irany
    elif uj_irany == 'fel' and i != 'le':
        i = uj_irany
    elif uj_irany == 'le' and i != 'fel':
        i = uj_irany

def jatek_vege():
    global OSSZES_PONT, is_game_over
    is_game_over = True

    if user != "Vendég":  # de csak ha nem vendég
        jelenlegi_pont_snake_OSSZES = database.child('Kigyos_jatek_OSSZES').child(user).get().val()
        if jelenlegi_pont_snake_OSSZES is None:
            jelenlegi_pont_snake_OSSZES = 0
        else:
            jelenlegi_pont_snake_OSSZES = int(jelenlegi_pont_snake_OSSZES)
        uj_pont_snake_OSSZES = jelenlegi_pont_snake_OSSZES + 1
        database.child('Kigyos_jatek_OSSZES').child(user).set(uj_pont_snake_OSSZES)




        jelenlegi_pont = database.child('Osszes_pontszam').child(user).get().val()
        if jelenlegi_pont is None:
            jelenlegi_pont = 0
        else:
            jelenlegi_pont = int(jelenlegi_pont)
        uj_pont = jelenlegi_pont + 1
        database.child('Osszes_pontszam').child(user).set(uj_pont)

        # csak az akasztofa ranglistan:
        jelenlegi_pont_snake = database.child('Kigyos_jatek').child(user).get().val()
        if jelenlegi_pont_snake is None:
            jelenlegi_pont_snake = 0
        else:
            jelenlegi_pont_snake = int(jelenlegi_pont_snake)
        uj_pont_snake = jelenlegi_pont_snake + OSSZES_PONT
        
        database.child('Kigyos_jatek').child(user).set(uj_pont_snake)

    v.delete(tk.ALL)
    szoveg = f"Pontjaid: {OSSZES_PONT}\nKezdéshez: SPACE"
    v.create_text(SZEL / 2, MAG / 2, font=('consolas', 15), text=szoveg, fill="WHITE", tag="vege")
    OSSZES_PONT = 0
    ablak.unbind("<Left>")
    ablak.unbind("<Right>")
    ablak.unbind("<Up>")
    ablak.unbind("<Down>")

def pont_novel():
    global pontok, OSSZES_PONT
    pontok += 1
    OSSZES_PONT += 1
    pont_cimke.config(text="Pontok: {}".format(pontok))

def kezdj_jatek():
    global pontok, is_game_over
    v.delete(tk.ALL)
    ablak.update()

    pontok = 0
    is_game_over = False
    ujra_gomb.pack_forget()
    pont_cimke.config(text="Pontok: {}".format(pontok))
    k = Kigyo()
    e = Etel()
    k.kigyo_letrehozasa(v)
    irany_valtoztatas(uj_irany="le")
    kovetkezo_kor(k, e)
    irany_valtoztatas(uj_irany="le")
    ablak.update()

    ablak.bind("<Left>", lambda event: irany_valtoztatas('balra'))
    ablak.bind("<Right>", lambda event: irany_valtoztatas('jobbra'))
    ablak.bind("<Up>", lambda event: irany_valtoztatas('fel'))
    ablak.bind("<Down>", lambda event: irany_valtoztatas('le'))

ablak = tk.Tk()
ablak.title("Kigyo Jatek")
pontok = 0
i = 'le'
is_game_over = False

v = tk.Canvas(ablak, bg=HATTER, height=MAG, width=SZEL)
v.pack()

ablak.update()

ablak_szel = ablak.winfo_width()
ablak_mag = ablak.winfo_height() + 30
ablak_x = (ablak.winfo_screenwidth() // 2) - (ablak_szel // 2)
ablak_y = (ablak.winfo_screenheight() // 2) - (ablak_mag // 2)
ablak.geometry(f'{ablak_szel}x{ablak_mag}+{ablak_x}+{ablak_y}')

ablak.bind("<space>", lambda event: kezdj_jatek())

pont_cimke = tk.Label(ablak, font=('consolas', 20), text="Pontok: 0", bg=HATTER, fg="WHITE")
pont_cimke.pack()

ujra_gomb = tk.Button(ablak, text="Újra", font=('consolas', 15), command=kezdj_jatek)
ujra_gomb.pack_forget()


v.create_text(SZEL / 2, MAG / 2, font=('consolas', 20), text="Kezdéshez: SPACE", fill="WHITE", tag="Kezdéshez: SPACE")
ablak.mainloop()