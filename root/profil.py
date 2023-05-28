from tkinter import *
import pyrebase

def profil_szerkesztes(jelszo, bio, hely):
    with open("adatok.txt", "r", encoding="UTF-8") as fajl:
        nev = fajl.readline().strip()
    print(jelszo, bio, hely, nev)
    def mentes():

        
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


        mentendo = bemutatkoz_ki.get()
        mentendo_nev = jelszo_ki.get()
        jelszo_ki.delete(0, END)
        jelszo_ki.insert(0, mentendo_nev)
        bemutatkoz_ki.delete(0, END)
        bemutatkoz_ki.insert(0, mentendo)

        jelszo_eloszor = jelszo_ki.get()
        jelszo_masodszor = jelszo_ki2.get()

        if jelszo_eloszor != jelszo_masodszor:
            hiba = "A két jelszó nem egyezik!"
        else:
            if len(jelszo_eloszor) < 8:
                try:
                    hiba.destroy()
                except:
                    hiba = Label(ablak, fg="RED", text="Sajnos nem elég hosszú jelszó!").grid(row=5, column=1, columnspan=3)
            elif not any(char.isdigit() for char in jelszo_eloszor) or not any(char.isalpha() for char in jelszo_eloszor) or not any(char.isupper() for char in jelszo_eloszor) \
            or jelszo_eloszor.isspace():
                try:
                    hiba.destroy()
                except:
                    hiba = Label(ablak, fg="RED", text="Nem elég erős jelszó!").grid(row=5, column=1, columnspan=3)
            else: #ekkor végre mindent jól csinált a felhasználó
                database.child('Users').child(nev).set(jelszo_eloszor)
                jelszo_ki.delete(0, END)
                jelszo_ki2.delete(0, END)
                sikeres = Label(ablak, fg="GREEN", text="Sikeres jelszóváltoztatás!").grid(row=5, column=1, columnspan=3)


    ablak = Toplevel()
    ablak.title("Profilbeállítás")
    ablak.geometry("500x400")

    jelszo = Label(ablak, text="Új jelszó")
    jelszo2 = Label(ablak, text="Új jelszó újra")
    jelszo_ki = Entry(ablak, show="*")
    jelszo_ki2 = Entry(ablak, show="*")
    bemutatkoz = Label(ablak, text="Bemutatkozás")


    bemutatkoz_ki = Entry(ablak, text="")
    bemutatkoz_ki.insert(0, bio)

    szerk = Button(ablak, text="Alkalmazás 🖊", command=mentes)
    ranglista = Label(ablak, text="Jelenlegi ranglista helyezés:")
    ranglista_ki = Label(ablak, text=hely+1)

    jelszo.grid(row=1, column=1)
    jelszo2.grid(row=2, column=1)
    jelszo_ki.grid(row=1, column=2)
    jelszo_ki2.grid(row=2, column=2)
    bemutatkoz.grid(row=3, column=1)
    bemutatkoz_ki.grid(row=3, column=2)
    szerk.grid(row=2, column=3)
    ranglista.grid(row=4, column=1)
    ranglista_ki.grid(row=4, column=2)