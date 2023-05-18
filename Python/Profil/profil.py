from tkinter import*

def mentes():
    mentendo = eval(bemutatkoz_ki.get())
    mentendo_nev = eval(felhnev_ki.get())
    felhnev_ki.delete(0,END)
    felhnev_ki.insert(mentendo_nev)
    bemutatkoz_ki.delete(0,END)
    bemutatkoz_ki.insert(mentendo)

ablak = Tk()
#Cím és ikonok
ablak.title("Profilbeállítás")
#ablak.iconbitmap(r'andriod_1.exe')
kep = PhotoImage(file="S.png")
ablak.iconphoto(False, kep)
ablak.geometry("300x400")

#Label/Entry

felhnev = Label(ablak,text="Felhasználónév")
felhnev_ki = Entry()
bemutatkoz = Label(ablak,text = "Bemutatkozás")
bemutatkoz_ki = Entry()
szerk = Button(ablak ,text="Szerkeztés🖊", command=mentes)
ranglista = Label(ablak, text="Jelenlegi ranglista helyezés: ")
ranglista_ki = Entry()
kijelent = Button(ablak, text="Kijelentkezés🚪", command= ablak.destroy)

#Grid
felhnev.grid(row=1, column=1)
felhnev_ki.grid(row=1, column=2)
bemutatkoz.grid(row=2,column=1)
bemutatkoz_ki.grid(row=2,column=2)
szerk.grid(row=2, column=3)
ranglista.grid(row = 3, column= 1)
ranglista_ki.grid(row=3, column=2)
kijelent.grid(row=4, column=3)
ablak.mainloop()