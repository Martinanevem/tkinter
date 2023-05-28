#ne hívd meg önmagában ezt a python fájlt, csak a funkctionokat használd!

import pyrebase
from collections import OrderedDict

from tkinter import *

from kezdes import start



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




def auth_bejelentkezes(ablak1, nev, jelszo):
    global torold_ezt
    
    adatok = list()
    adatok.append(nev);adatok.append(jelszo)

    osszes_adat = database.child("Users").get().val()

    for key, value in osszes_adat.items():
        if key == adatok[0] and value == adatok[1]: #ekkor sikerült a bejelntkezés
            print("Sikerült az adatok authentikalizálása!")
            osszes_adat=database.child("Osszes_pontszam").get().val()
            bio = "Üres"
            search_key = adatok[0]
            sorted_items = sorted(osszes_adat.items(), key=lambda x: x[1], reverse=True)

            for index, (key, value) in enumerate(sorted_items):
                if key == search_key:
                    hely = index
            titkos_adatok = [adatok[0], bio, hely]
            with open("adatok.txt", "w", encoding="UTF-8") as adatok_irasa:
                adatok_irasa.write(adatok[0])
            ablak1.destroy()
            start(nev, osszes_adat, titkos_adatok)
            
            
    else:
        hiba = Label(ablak1, fg="RED", text="Helytelen felhasználónév/jelszó!").grid(row=5, column=1, columnspan=4)

def auth_regisztracio(ablak1, nev, jelszo, jelszo_ujra):
    folytatas = True
    adatok = list()
    adatok.append(nev);adatok.append(jelszo)

    user = adatok[0]
    password = adatok[1]

    osszes_adat = database.child("Users").get().val()
    for key, value in osszes_adat.items():
        if key == adatok[0]:
            hiba = Label(ablak1, fg="RED", text="Hiba történt: a felhasználónév foglalt!!!").grid(row=5, column=1, columnspan=3)
            folytatas = False
            
    if folytatas:
        if user.isspace() or len(user) < 3 or len(user) > 16:
            try:
                hiba.destroy()
            except:
                hiba = Label(ablak1, fg="RED", text="A felhasználónév helytelen!").grid(row=5, column=1, columnspan=3)
        elif jelszo != jelszo_ujra:
            try:
                hiba.destroy()
            except:
                hiba = Label(ablak1, fg="RED", text="Sajnos a két jelszó nem egyezik!").grid(row=5, column=1, columnspan=3)
        elif len(password) < 8:
            try:
                hiba.destroy()
            except:
                hiba = Label(ablak1, fg="RED", text="Sajnos nem elég hosszú jelszó!").grid(row=5, column=1, columnspan=3)
        elif not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char.isupper() for char in password) \
        or password.isspace():
            try:
                hiba.destroy()
            except:
                hiba = Label(ablak1, fg="RED", text="Nem elég erős jelszó!").grid(row=5, column=1, columnspan=3)
        else: #ekkor végre mindent jól csinált a felhasználó
            veges_adatok = {user: password}
            database.child("Users").update(veges_adatok)
            database.child("Osszes_pontszam").update({user: 0})
            database.child("Akasztofa").update({user: 0})
            database.child("Teglatoro").update({user: 0})
            database.child("Kigyos_jatek").update({user: 0})
            ablak1.destroy()


def authAblak(bejelentkezes=False, regisztracio=False):

    if bejelentkezes == True or regisztracio == True:
        def keep_window_on_top(window):
            window.attributes('-topmost', True)
        ablak1 = Tk()

        keep_window_on_top(ablak1)

        ablak1.title("Felhasználó hitelesítése")
        ablak1.geometry("400x200")

        frame1 = Frame(ablak1, highlightbackground="grey", highlightthickness=2)
        ablak1.columnconfigure(0, weight=1)
        ablak1.columnconfigure(3, weight=1)
        ablak1.rowconfigure(0, weight=1)
        ablak1.rowconfigure(3, weight=1)

        if bejelentkezes:

            loginSzoveg = Label(ablak1, text="Kérlek add meg a felhasználóneved", font=('Helvetica bold', 12))
            loginSzoveg.grid(row=1, column=1, sticky="e", padx=5, pady=5)

            loginEntry = Entry(ablak1)
            loginEntry.grid(row=1, column=2)

            loginSzoveg2 = Label(ablak1, text="Kérlek add meg a jelszavad", font=('Helvetica bold', 12))
            loginSzoveg2.grid(row=2, column=1, padx=5, pady=5)

            loginEntry2 = Entry(ablak1, show="⁇")
            loginEntry2.grid(row=2, column=2)

            gomb = Button(ablak1, font=('Helvetica bold', 16), text="Bejelentkezem!", command=lambda: auth_bejelentkezes(
                #ahol:
                ablak1 = ablak1,
                nev = loginEntry.get(),
                jelszo = loginEntry2.get()

            ))
            gomb.grid(row=3, columnspan=2, column=1)
        elif regisztracio:

            loginSzoveg = Label(ablak1, text="Kérlek add meg a felhasználóneved", font=('Helvetica bold', 12))
            loginSzoveg.grid(row=1, column=1, sticky="e", padx=5, pady=5)

            loginEntry = Entry(ablak1)
            loginEntry.grid(row=1, column=2)

            loginSzoveg2 = Label(ablak1, text="Kérlek add meg a jelszavad", font=('Helvetica bold', 12))
            loginSzoveg2.grid(row=2, column=1, padx=5, pady=5)

            loginEntry2 = Entry(ablak1, show="⁇")
            loginEntry2.grid(row=2, column=2)

            loginSzoveg3 = Label(ablak1, text="Kérlek add meg a jelszavad újra", font=('Helvetica bold', 12))
            loginSzoveg3.grid(row=3, column=1, padx=5, pady=0)

            loginEntry3 = Entry(ablak1, show="⁇")
            loginEntry3.grid(row=3, column=2)

            gomb = Button(ablak1, font=('Helvetica bold', 16), text="Regisztrálok!", command=lambda: auth_regisztracio(
                #ahol:
                ablak1 = ablak1,
                nev = loginEntry.get(),
                jelszo = loginEntry2.get(),
                jelszo_ujra = loginEntry3.get()

            ))
            gomb.grid(row=4, columnspan=2, column=1, pady=10)

            ablak1.mainloop()
    else:
        #ugye ekkor vendégként van belpéve! (False-False)
        with open("adatok.txt", "w", encoding="UTF-8") as adatok_irasa:
                adatok_irasa.write("Vendég")
        osszes_adat = database.child("Osszes_pontszam").get().val()
        start("Vendég", osszes_adat, "ÜRES")
        