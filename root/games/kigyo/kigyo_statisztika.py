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


jelenlegi_pont = database.child("Kigyos_jatek").get().val()

ranglista_szoveg = Label(ablak1, text="Snake ranglista", font=('Helvetica bold', 16)).grid(padx=120,row=5, column=0, columnspan=2)
row = 7
for key, value in sorted(jelenlegi_pont.items(), key=lambda x: x[1], reverse=True):
    label_key = Label(ablak1, text=key)
    label_key.grid(row=row, column=0)

    label_value = Label(ablak1, text=value)
    label_value.grid(row=row, column=1)

    row += 1

ablak1.mainloop()