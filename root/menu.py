from tkinter import *
import os
import subprocess

def menu(ablak1, bejelentkezve):

	def akasztofa_start():
		try:
			new_path = "./games/akasztofa"
			os.chdir(new_path)
			subprocess.run(["python", "./akasztofa.py"])
		except:
			subprocess.run(["python", "./akasztofa.py"])
		
		

	menusor=Frame(ablak1)
	menusor.grid(row=0)
	menu0=Menubutton(menusor,text="Fájlok",underline=0)
	menu1=Menubutton(menusor,text="Játékok",underline=0)
	menu2=Menubutton(menusor,text="Matematika",underline=0)
	if bejelentkezve: menu3=Menubutton(menusor,text="Profil",underline=0)
	menu4=Menubutton(menusor,text="Rólunk",underline=0)
	menu0.grid(row=0, column=0)

	menu1.grid(row=0, column=1)
	menu2.grid(row=0, column=2)
	if bejelentkezve: menu3.grid(row=0, column=3)
	menu4.grid(row=0, column=4)


	fajl=Menu(menu0, tearoff="off")
	jatek=Menu(menu1, tearoff="off")
	matek=Menu(menu2, tearoff="off")
	if bejelentkezve: profil=Menu(menu3, tearoff="off")
	rolunk=Menu(menu4, tearoff="off")

	fajl.add_command(label="Kilepes",command=ablak1.destroy)
	fajl.add_command(label="Export",command=ablak1.destroy)
	fajl.add_command(label="Import",command=ablak1.destroy)
	jatek.add_command(label="Akasztófa",command=akasztofa_start)
	jatek.add_command(label="Brick Breaker",command=ablak1.destroy)
	jatek.add_command(label="Kő, Papír, Olló",command=ablak1.destroy)
	jatek.add_command(label="Számkitalálós",command=ablak1.destroy)
	jatek.add_command(label="Snake",command=ablak1.destroy)
	jatek.add_cascade(label = "Játékok", menu = menu1)
	matek.add_command(label="Számológép")
	matek.add_command(label="Kerület Terület")
	matek.add_command(label="Turtle")
	if bejelentkezve: 
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
	if bejelentkezve: profil.config(bg="RED", fg="WHITE")
	rolunk.config(bg="RED", fg="WHITE")
	#menusorok szine
	menu0.config(menu=fajl, bg="BLACK",fg="WHITE")
	menu0.config(menu=fajl, bg="BLACK",fg="WHITE")
	menu1.config(menu=jatek, bg="BLACK",fg="WHITE")
	menu2.config(menu=matek, bg="BLACK",fg="WHITE")
	if bejelentkezve: menu3.config(menu=profil, bg="BLACK",fg="WHITE")
	menu4.config(menu=rolunk, bg="BLACK",fg="WHITE")