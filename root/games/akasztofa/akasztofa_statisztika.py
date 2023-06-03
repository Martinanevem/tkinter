import pyrebase
import os
from tkinter import *

ablak1 = Tk()

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


jelenlegi_pont = database.child("Akasztofa").get().val()

ranglista_szoveg = Label(ablak1, text="Akasztófa ranglista", font=('Helvetica bold', 16)).grid(padx=120,row=5, column=0, columnspan=2)
row = 7
for key, value in sorted(jelenlegi_pont.items(), key=lambda x: x[1], reverse=True):
    label_key = Label(ablak1, text=key)
    label_key.grid(row=row, column=0)

    label_value = Label(ablak1, text=value)
    label_value.grid(row=row, column=1)

    row += 1

if user != "Vendég":
    jelenlegi_pont_akasztofa = database.child('Akasztofa').get().val()

    osszes = database.child('Akasztofa_OSSZES').child(user).get().val()
    if osszes is None:
        osszes = 0
    else:
        osszes = int(osszes)
    
    nyert_ = database.child('Akasztofa').child(user).get().val()
    if nyert_ is None:
        nyert_ = 0
    else:
        nyert_ = int(nyert_)

    osszes = osszes
    nyert = nyert_
    vesztett = osszes-nyert

    search_key = user
    sorted_items = sorted(jelenlegi_pont_akasztofa.items(), key=lambda x: x[1], reverse=True)
    for index, (key, value) in enumerate(sorted_items):
        if key == search_key:
            hely = index
    szoveg = f"{hely+1}. helyen állsz az akasztófa ranglistán!"

    osszes = f"Összes játékok: {osszes}"
    nyert = f"Megnyert játékok: {nyert}"
    vesztett = f"Vesztett játékok: {vesztett}"
    a_te_statod = Label(ablak1, text="A te statisztikáid", font=('Helvetica bold', 16)).grid(padx=2,row=5, column=5, columnspan=4)
    osszes_jatek = Label(ablak1, text=osszes, font=('Helvetica bold', 12)).grid(row=7, column=5)
    osszes_jatek = Label(ablak1, text=nyert, font=('Helvetica bold', 12)).grid(row=8, column=5)
    osszes_jatek = Label(ablak1, text=vesztett, font=('Helvetica bold', 12)).grid(row=9, column=5)
    hely = Label(ablak1, text=szoveg, font=('Helvetica bold', 9)).grid(row=10, column=5)


ablak1.mainloop()