from tkinter import *
ablak1=Tk()
ablak1.title("Próba")
ablak1.minsize(width=200,height=150)
menusor=Frame(ablak1)
menusor.grid(row=0)
menu0=Menubutton(menusor,text="Fájlok",underline=0)
menu1=Menubutton(menusor,text="Játékok",underline=0)
menu2=Menubutton(menusor,text="Matematika",underline=0)
menu3=Menubutton(menusor,text="Profil",underline=0)
menu4=Menubutton(menusor,text="Rólunk",underline=0)

menu0.grid(row=0, column=0)

menu1.grid(row=0, column=1)
menu2.grid(row=0, column=2)
menu3.grid(row=0, column=3)
menu4.grid(row=0, column=4)


fajl=Menu(menu0)
jatek=Menu(menu1)
matek=Menu(menu2)
profil=Menu(menu3)
rolunk=Menu(menu4)

fajl.add_command(label="Kilepes",command=ablak1.destroy)
fajl.add_command(label="Export",command=ablak1.destroy)
fajl.add_command(label="Import",command=ablak1.destroy)
jatek.add_command(label="Akasztófa",command=ablak1.destroy)
jatek.add_command(label="Brick Breaker",command=ablak1.destroy)
jatek.add_command(label="Kő, Papír, Olló",command=ablak1.destroy)
jatek.add_command(label="Számkitalálós",command=ablak1.destroy)
jatek.add_command(label="Snake",command=ablak1.destroy)
jatek.add_cascade(label = "Játékok", menu = menu1)
matek.add_command(label="Számológép")
matek.add_command(label="Kerület Terület")
matek.add_command(label="Turtle")
profil.add_command(label="Testreszabás")
profil.add_command(label="Ranglista")
profil.add_command(label="Kijelentkezés")
rolunk.add_command(label="A programot készítette:")
rolunk.add_command(label="Basa Martin")
rolunk.add_command(label="Dóczi Adrián Márk")
rolunk.add_command(label="Bujáki Erik Attila")
#lenyilo menu szin
fajl.config(bg="RED", fg="WHITE")
jatek.config(bg="RED", fg="WHITE")
matek.config(bg="RED", fg="WHITE")
profil.config(bg="RED", fg="WHITE")
rolunk.config(bg="RED", fg="WHITE")
#menusorok szine
menu0.config(menu=fajl, bg="BLACK",fg="WHITE")
menu0.config(menu=fajl, bg="BLACK",fg="WHITE")
menu1.config(menu=jatek, bg="BLACK",fg="WHITE")
menu2.config(menu=matek, bg="BLACK",fg="WHITE")
menu3.config(menu=profil, bg="BLACK",fg="WHITE")
menu4.config(menu=rolunk, bg="BLACK",fg="WHITE")

frame1 = Frame(ablak1, highlightbackground="grey", highlightthickness=2)
var=StringVar()
mondat=Button(frame1,textvariable=var)
var.set("Bejelentkezés")
frame1.grid(row=4,column=0, pady=5, sticky="N")
mondat.grid(row=4,column=0, sticky="N")
frame2 = Frame(ablak1, highlightbackground="grey", highlightthickness=2)
var1=StringVar()
mondat1=Button(frame2,textvariable=var1)
var1.set("Regisztráció")
frame2.grid(row=5,column=0, pady=5, sticky="N")
mondat1.grid(row=5,column=0, sticky="N")

frame3= Frame(ablak1, highlightbackground="grey", highlightthickness=2)
var2=StringVar()
mondat2=Button(frame3,textvariable=var2)
var2.set("Bejelentkezés vendégként")
frame3.grid(row=6,column=0, pady=5, sticky="N")
mondat2.grid(row=6,column=0)

ablak1.mainloop()