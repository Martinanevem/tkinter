from tkinter import *
import os
import subprocess

from profil import profil_szerkesztes

def menu(ablak1, bejelentkezve, titkos_adatok):

	#GAME részleg:
	def akasztofa_start():
		try:
			new_path = "./games/akasztofa"
			os.chdir(new_path)
			subprocess.run(["python", "./akasztofa.py"])
		except:
			subprocess.run(["python", "./akasztofa.py"])
	#GAME részleg vége-------------------------------------
	
	#MATEK részleg
	def turtle_start():
		try:
			new_path = "./matek"
			os.chdir(new_path)
			subprocess.run(["python", "./turtle.py"])
		except:
			subprocess.run(["python", "./turtle.py"])
	#MATEK részleg vége------------------------------------

	def profil_start():
		try:
			subprocess.run(["python", "./profil.py"])
		except:
			subprocess.run(["python", "./profil.py"])
		
		

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
	sub_menu = Menu(jatek, tearoff=0)
	sub_menu.add_command(label='Indítás',command=akasztofa_start)
	sub_menu.add_command(label='Statisztikák')
	jatek.add_cascade(
		label="Akasztófa",
		menu=sub_menu
	)

	sub_menu1 = Menu(jatek, tearoff=0)
	sub_menu1.add_command(label='Indítás')
	sub_menu1.add_command(label='Statisztikák')
	jatek.add_cascade(
		label="Brick Breaker",
		menu=sub_menu1
	)
	sub_menu2 = Menu(jatek, tearoff=0)
	sub_menu2.add_command(label='Indítás')
	sub_menu2.add_command(label='Statisztikák')
	jatek.add_cascade(
		label="Kő, Papír, Olló",
		menu=sub_menu2
	)

	sub_menu3 = Menu(jatek, tearoff=0)
	sub_menu3.add_command(label='Indítás')
	sub_menu3.add_command(label='Statisztikák')
	jatek.add_cascade(
		label="Számkitalálós",
		menu=sub_menu3
	)
	sub_menu4 = Menu(jatek, tearoff=0)
	sub_menu4.add_command(label='Indítás')
	sub_menu4.add_command(label='Statisztikák')
	jatek.add_cascade(
		label="Snake",
		menu=sub_menu4
	)
	
	jatek.add_cascade(label = "Játékok", menu = menu1)
	matek.add_command(label="Számológép")
	matek.add_command(label="Kerület Terület")
	matek.add_command(label="Turtle", command=turtle_start)
	if bejelentkezve: 
		profil.add_command(label="Testreszabás", command=lambda:profil_szerkesztes(titkos_adatok[0], titkos_adatok[1], titkos_adatok[2]))
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