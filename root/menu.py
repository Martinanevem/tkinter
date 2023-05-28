from tkinter import *
import os
import subprocess

from profil import profil_szerkesztes


import sys

def menu(ablak1, bejelentkezve, titkos_adatok):

	#GAME részleg:
	def akasztofa_start():
		try:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games", "akasztofa")
			
			kezdoOldal_path = os.path.join(game_path, "akasztofa.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
		except:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games")
			kezdoOldal_path = os.path.join(game_path, "akasztofa.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)

	def akasztofa_statisztika():
		try:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games", "akasztofa")
			
			kezdoOldal_path = os.path.join(game_path, "akasztofa_statisztika.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
		except:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games")
			kezdoOldal_path = os.path.join(game_path, "akasztofa_statisztika.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)

	def teglatoro_start():
		try:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games", "brickBraker_teglatoro")
			
			kezdoOldal_path = os.path.join(game_path, "teglatoro.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
		except:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games")
			kezdoOldal_path = os.path.join(game_path, "teglatoro.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)

	def teglatoro_statisztika():
		try:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games", "brickBraker_teglatoro")
			
			kezdoOldal_path = os.path.join(game_path, "teglatoro_statisztika.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
		except:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games")
			kezdoOldal_path = os.path.join(game_path, "teglatoro_statisztika.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
	

	def snake_start():
		try:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games", "kigyo")
			
			kezdoOldal_path = os.path.join(game_path, "kigyo.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
		except:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games")
			kezdoOldal_path = os.path.join(game_path, "kigyo.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
	
	def snake_statisztika():
		try:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games", "kigyo")
			
			kezdoOldal_path = os.path.join(game_path, "kigyo_statisztika.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
		except:
			venv_path = "virtualis_kornyezet"
			scripts_path = os.path.join(venv_path, "Scripts")
			python_path = os.path.join(scripts_path, "python")

			game_path = os.path.join("games")
			kezdoOldal_path = os.path.join(game_path, "kigyo_statisztika.py")
			subprocess.run([python_path, kezdoOldal_path], shell=True)
	#GAME részleg vége-------------------------------------
	
	#MATEK részleg

	def turtle_start():
		try:
			subprocess.run(["python", "./matek/turtle.py"])
		except:
			subprocess.run(["python", "./matek/turtle.py"])


	#MATEK részleg vége------------------------------------

	def profil_start():
		try:
			subprocess.run(["python", "./profil.py"])
		except:
			subprocess.run(["python", "./profil.py"])
		
		

	menusor = Frame(ablak1)
	menusor.grid(row=0, sticky="ew")  # Place the frame in the first row and make it expand horizontally

	menu0 = Menubutton(menusor, text="Fájlok", underline=0)
	menu1 = Menubutton(menusor, text="Játékok", underline=0)
	menu2 = Menubutton(menusor, text="Matematika", underline=0)
	if bejelentkezve:
		menu3 = Menubutton(menusor, text="Profil", underline=0)
	else: menu3 = Menubutton(menusor, text="Profil", underline=0)
	menu4 = Menubutton(menusor, text="Rólunk", underline=0)

	menu0.grid(row=0, column=0, sticky="ew")
	menu1.grid(row=0, column=1, sticky="ew")
	menu2.grid(row=0, column=2, sticky="ew")
	if bejelentkezve:
		menu3.grid(row=0, column=3, sticky="ew")
	else: menu3.grid(row=0, column=3, sticky="ew")
	menu4.grid(row=0, column=4, sticky="ew")

	menusor.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)  # Make all columns expand to fill the available space





	fajl=Menu(menu0, tearoff="off")
	jatek=Menu(menu1, tearoff="off")
	matek=Menu(menu2, tearoff="off")
	if bejelentkezve: profil=Menu(menu3, tearoff="off")
	else: profil=Menu(menu3, tearoff="off")
	rolunk=Menu(menu4, tearoff="off")

	fajl.add_command(label="Kilepes",command=ablak1.destroy)
	fajl.add_command(label="Export",command=ablak1.destroy)
	fajl.add_command(label="Import",command=ablak1.destroy)
	sub_menu = Menu(jatek, tearoff=0)
	sub_menu.add_command(label='Információk', command=teglatoro_statisztika)
	sub_menu.add_command(label='Indítás',command=akasztofa_start)
	sub_menu.add_command(label='Statisztikák', command=akasztofa_statisztika)
	jatek.add_cascade(
		label="Akasztófa",
		menu=sub_menu
	)

	sub_menu1 = Menu(jatek, tearoff=0)
	sub_menu1.add_command(label='Információk', command=teglatoro_statisztika)
	sub_menu1.add_command(label='Indítás', command=teglatoro_start)
	sub_menu1.add_command(label='Statisztikák', command=teglatoro_statisztika)
	jatek.add_cascade(
		label="Brick Breaker",
		menu=sub_menu1
	)
	sub_menu2 = Menu(jatek, tearoff=0)
	sub_menu2.add_command(label='Információk', command=teglatoro_statisztika)
	sub_menu2.add_command(label='Indítás')
	sub_menu2.add_command(label='Statisztikák')
	jatek.add_cascade(
		label="Kő, Papír, Olló",
		menu=sub_menu2
	)

	sub_menu3 = Menu(jatek, tearoff=0)
	sub_menu3.add_command(label='Információk', command=teglatoro_statisztika)
	sub_menu3.add_command(label='Indítás')
	sub_menu3.add_command(label='Statisztikák', command=teglatoro_statisztika)
	jatek.add_cascade(
		label="Számkitalálós",
		menu=sub_menu3
	)
	sub_menu4 = Menu(jatek, tearoff=0)
	sub_menu4.add_command(label='Információk', command=teglatoro_statisztika)
	sub_menu4.add_command(label='Indítás', command=snake_start)
	sub_menu4.add_command(label='Statisztikák', command=snake_statisztika)
	jatek.add_cascade(
		label="Snake",
		menu=sub_menu4
	)
	
	
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
	else: menu3.config(menu=profil, bg="BLACK",fg="WHITE", state=DISABLED)
	menu4.config(menu=rolunk, bg="BLACK",fg="WHITE")