import tkinter as tk
from tkinter import Canvas, PhotoImage
import json
import random

from time import sleep


class Akasztofa:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Akasztófa")
        self.window.geometry("400x520")

        self.keresendo_betuk = []
        f = open('szavak.json', 'r', encoding='utf-8')
        self.szavak = json.load(f)

        kategoria_valasztas = [self.szavak["targyak"], self.szavak["allatok"]]
        self.valasztott_kategoria = random.choice(kategoria_valasztas)
        self.kategoria = self.valasztott_kategoria
        if self.kategoria == kategoria_valasztas[0]:
            self.szofaj = "Tárgy"
        elif self.kategoria == kategoria_valasztas[1]:
            self.szofaj = "Állat"

        self.szo = random.choice(self.kategoria)
        for i in self.szo:
            self.keresendo_betuk.append(i)
        self.megtalalt_betuk = []
        self.rossz_betuk = []
        self.maxTippek = 6
        self.jelenlegi_tippek = 0

        self.can1 = Canvas(self.window, width=440, height=360, bg='white')
        self.photo = PhotoImage(file='./kepek/hang5.png')
        self.item = self.can1.create_image(220, 200, image=self.photo)
        self.can1.grid(row=0, column=2, columnspan=2)

        self.label_word = tk.Label(self.window, text="_ " * len(self.szo))
        self.label_word.grid(row=1, column=2, columnspan=2)

        self.label_attempts = tk.Label(self.window, text="Tippek: 0/" + str(self.maxTippek))
        self.label_attempts.grid(row=2, column=2, columnspan=2)

        self.entry_guess = tk.Entry(self.window)
        self.entry_guess.grid(row=3, column=2, columnspan=2)

        self.leiras_segitseg = True
        self.szofaj_segitseg = True
        self.kepes_segitseg = True

        self.button_guess = tk.Button(self.window, fg="WHITE", bg="BLACK", text="Tippelek", command=self.check_guess)
        self.button_guess.grid(row=4, column=2, padx=(150, 0), pady=15)

        self.button_guess2 = tk.Button(self.window, fg="WHITE", bg="BLACK", text="Segítség", command=self.segitseg)
        self.button_guess2.grid(row=4, column=3, padx=(0, 150))

        # Additional empty label to center the buttons
        self.empty_label = tk.Label(self.window)
        self.empty_label.grid(row=4, column=1)

        self.label_feedback = tk.Label(self.window, text="")
        self.label_feedback.grid(row=5, column=2, columnspan=2)

        self.window.mainloop()

    def update_img(self):
        try:
            if self.jelenlegi_tippek == 1:
                self.photo = PhotoImage(file='./kepek/hang6.png')
            elif self.jelenlegi_tippek == 2:
                self.photo = PhotoImage(file='./kepek/hang7.png')
            elif self.jelenlegi_tippek == 3:
                self.photo = PhotoImage(file='./kepek/hang8.png')
            elif self.jelenlegi_tippek == 4:
                self.photo = PhotoImage(file='./kepek/hang9.png')
            elif self.jelenlegi_tippek == 5:
                self.photo = PhotoImage(file='./kepek/hang10.png')
            elif self.jelenlegi_tippek == 6:
                self.photo = PhotoImage(file='./kepek/hang11.png')

            self.can1.itemconfig(self.item, image=self.photo)
            self.can1.image = self.photo
        except:
            self.can1.image = self.photo = PhotoImage(file='./kepek/hang5.png')

    def check_guess(self):
        tipp = self.entry_guess.get()

        if tipp == self.szo:
            self.vege(False)

        elif len(tipp) != 1:
            self.label_feedback.config(text="Kérlek csak egy betűt írj be!")
        elif tipp in self.megtalalt_betuk or tipp in self.rossz_betuk:
            self.label_feedback.config(text="Ezzel a betűvel már próbálkoztál!")
        else:
            if tipp in self.szo:
                for i in self.keresendo_betuk:
                    if i == tipp:
                        self.keresendo_betuk.remove(i)
                if len(self.keresendo_betuk) == 0:
                    self.vege(False)
                self.megtalalt_betuk.append(tipp)
                self.update_word_label()
            else:
                self.rossz_betuk.append(tipp)
                self.jelenlegi_tippek += 1
                self.update_img()
                self.label_attempts.config(text="Tippek: {}/{}".format(self.jelenlegi_tippek, self.maxTippek))
                if self.jelenlegi_tippek == self.maxTippek:
                    self.vege(True)

            self.entry_guess.delete(0, tk.END)

        self.update_img()

    def update_word_label(self):
        displayed_word = ""
        for letter in self.szo:
            if letter in self.megtalalt_betuk:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "

        self.label_word.config(text=displayed_word)
    

    def kepes_segitseg2(self):
        if self.kepes_segitseg != False:
            self.kepes_ablak = tk.Toplevel()  # Use Toplevel instead of Tk
            self.kepes_ablak.title("Képes segítség")  # Call title as a method

            self.kepek = Canvas(self.kepes_ablak, width=440, height=360, bg='white')
            
        
            if self.szo == self.szavak["targyak"][0]: self.photo2 = PhotoImage(file='./skepek/t0.png')
            elif self.szo == self.szavak["targyak"][1]: self.photo2 = PhotoImage(file='./skepek/t1.png')
            elif self.szo == self.szavak["targyak"][2]: self.photo2 = PhotoImage(file='./skepek/t2.png')
            elif self.szo == self.szavak["targyak"][3]: self.photo2 = PhotoImage(file='./skepek/t3.png')
            elif self.szo == self.szavak["targyak"][4]: self.photo2 = PhotoImage(file='./skepek/t4.png')
            elif self.szo == self.szavak["allatok"][0]: self.photo2 = PhotoImage(file='./skepek/a1.png')
            elif self.szo == self.szavak["allatok"][1]: self.photo2 = PhotoImage(file='./skepek/a2.png')
            elif self.szo == self.szavak["allatok"][2]: self.photo2 = PhotoImage(file='./skepek/a3.png')

            self.item = self.kepek.create_image(220, 200, image=self.photo2)
            self.kepek.grid(row=0, column=2, columnspan=2)

            self.kepes_feedback = tk.Label(self.kepes_ablak, text="")
            self.kepes_feedback.grid(row=2, column=2, columnspan=2)

            for i in range(3, -1, -1):
                if i <= 0:
                    self.kepes.config(state=tk.DISABLED)
                    self.kepes_segitseg = False
                    self.kepes_ablak.destroy()
                else:
                    self.kepes_feedback.config(text=f"{i}", font=('Helvetica bold', 16))
                    self.kepes_ablak.update()
                    sleep(1)

    def leiras_segitseg2(self):
        if self.leiras_segitseg != False:
            self.leiras_ablak = tk.Toplevel()
            self.leiras_ablak.title("Leírás segítség")
        
            self.szoveg = tk.Label(self.leiras_ablak, text="", font=('Helvetica bold', 16))
            self.szoveg.grid(row=1, column=2, columnspan=2)


            if self.szo == self.szavak["targyak"][0]: self.szoveg.config(text=self.szavak["segitsegek_a_targyakhoz"]["0"])
            elif self.szo == self.szavak["targyak"][1]: self.szoveg.config(text=self.szavak["segitsegek_a_targyakhoz"]["1"])
            elif self.szo == self.szavak["targyak"][2]: self.szoveg.config(text=self.szavak["segitsegek_a_targyakhoz"]["2"])
            elif self.szo == self.szavak["targyak"][3]: self.szoveg.config(text=self.szavak["segitsegek_a_targyakhoz"]["3"])
            elif self.szo == self.szavak["targyak"][4]: self.szoveg.config(text=self.szavak["segitsegek_az_allatokhoz"]["4"])
            elif self.szo == self.szavak["allatok"][0]: self.szoveg.config(text=self.szavak["segitsegek_az_allatokhoz"]["0"])
            elif self.szo == self.szavak["allatok"][1]: self.szoveg.config(text=self.szavak["segitsegek_az_allatokhoz"]["1"])
            elif self.szo == self.szavak["allatok"][2]: self.szoveg.config(text=self.szavak["segitsegek_az_allatokhoz"]["2"])
            elif self.szo == self.szavak["allatok"][3]: self.szoveg.config(text=self.szavak["segitsegek_az_allatokhoz"]["3"])
            
            self.szoveg.update()


            self.leiras_feedback = tk.Label(self.leiras_ablak, text="")
            self.leiras_feedback.grid(row=2, column=2, columnspan=2)

            for i in range(5, -1, -1):
                if i <= 0:
                    self.leiras.config(state=tk.DISABLED)
                    self.leiras_segitseg = False
                    self.leiras_ablak.destroy()
                else:
                    self.leiras_feedback.config(text=f"{i}", font=('Helvetica bold', 16))
                    self.leiras_ablak.update()
                    sleep(1)


            self.leiras_ablak.mainloop()

    def szofaj_segitseg2(self):
        if self.szofaj_segitseg != False:
            self.szofaj_ablak = tk.Toplevel()
            self.szofaj_ablak.title("Leírás segítség")
        
            self.szoveg2 = tk.Label(self.szofaj_ablak, text="", font=('Helvetica bold', 16))
            self.szoveg2.grid(row=1, column=2, columnspan=2)

            kategoria_valasztas = [self.szavak["targyak"], self.szavak["allatok"]]
            self.kategoria = self.valasztott_kategoria
            if self.kategoria == kategoria_valasztas[0]:
                self.szoveg2.config(text="Tárgy")
            elif self.kategoria == kategoria_valasztas[1]:
                self.szoveg2.config(text="Állat")

            self.szoveg2.update()

            self.szofaj.config(state=tk.DISABLED)
            self.szofaj_segitseg = False


            self.szofaj_ablak.mainloop()

    def segitseg(self):
        self.ujablak = tk.Tk()
        self.ujablak.title = "Segítségkérés"
        self.frame1 = tk.Frame(self.ujablak, highlightbackground="grey", highlightthickness=2)
        self.frame1.grid(row=1, column=1)
        #típusok:
        if self.kepes_segitseg == True:
            self.kepes = tk.Button(self.frame1, text="Képes segítség", font=('Helvetica bold', 16), command=self.kepes_segitseg2)
        else:
             self.kepes = tk.Button(self.frame1, text="Képes segítség", font=('Helvetica bold', 16), state=tk.DISABLED)
        self.kepes.grid(row=1, column=1)

        if self.szofaj_segitseg == True:
            self.szofaj = tk.Button(self.frame1, text="Szófaj segítség", font=('Helvetica bold', 16), command=self.szofaj_segitseg2)
        else:
            self.szofaj = tk.Button(self.frame1, text="Szófaj segítség", font=('Helvetica bold', 16), state=tk.DISABLED)
        self.szofaj.grid(row=2, column=1)

        if self.leiras_segitseg == True:
            self.leiras = tk.Button(self.frame1, text="Leírás segítség", font=('Helvetica bold', 16), command=self.leiras_segitseg2)
        else:
            self.leiras = tk.Button(self.frame1, text="Leírás segítség", font=('Helvetica bold', 16), state=tk.DISABLED)
        self.leiras.grid(row=3, column=1)
        
        self.kepes.update()

        self.ujablak.mainloop()

    


    def vege(self, vesztett):
        if vesztett:
            self.label_feedback.config(text="Vesztettél! A szó: '{}'".format(self.szo))
        else:
            self.label_feedback.config(text="Sikeresen kitaláltad a szót: '{}'".format(self.szo))

        self.entry_guess.config(state=tk.DISABLED)
        self.button_guess.config(state=tk.DISABLED)
        self.button_guess2.config(state=tk.DISABLED)


        self.ujra = tk.Button(self.window, text="Újra", bg="GRAY", command=lambda:self.restart_game())
        self.ujra.grid(row=4, column=3, padx=(0, 0))



    def restart_game(self):
        self.window.destroy()
        self.__init__()

game = Akasztofa()