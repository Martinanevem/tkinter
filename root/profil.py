from tkinter import *

def profil_szerkesztes(jelszo, bio, hely):
    print(jelszo, bio, hely)
    def mentes():
        mentendo = bemutatkoz_ki.get()
        mentendo_nev = jelszo_ki.get()
        jelszo_ki.delete(0, END)
        jelszo_ki.insert(0, mentendo_nev)
        bemutatkoz_ki.delete(0, END)
        bemutatkoz_ki.insert(0, mentendo)

    ablak = Toplevel()
    ablak.title("Profilbeállítás")
    ablak.geometry("500x400")

    jelszo = Label(ablak, text="Új jelszó")
    jelszo_ki = Entry(ablak)
    bemutatkoz = Label(ablak, text="Bemutatkozás")


    bemutatkoz_ki = Entry(ablak, text="")
    bemutatkoz_ki.insert(0, bio)

    szerk = Button(ablak, text="Alkalmazás 🖊", command=mentes)
    ranglista = Label(ablak, text="Jelenlegi ranglista helyezés:")
    ranglista_ki = Label(ablak, text=hely+1)

    jelszo.grid(row=1, column=1)
    jelszo_ki.grid(row=1, column=2)
    bemutatkoz.grid(row=2, column=1)
    bemutatkoz_ki.grid(row=2, column=2)
    szerk.grid(row=2, column=3)
    ranglista.grid(row=3, column=1)
    ranglista_ki.grid(row=3, column=2)
