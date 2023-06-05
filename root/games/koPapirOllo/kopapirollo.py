from tkinter import*
import random

# kő = 1, papír = 2, olló = 3
ablak = Tk()
tx = Label(ablak, text="*A gép választásának helye*")
can1 = Canvas(ablak,width=15, height=15, bg='white' )
can2 = Canvas(ablak,width=15, height=15, bg='white')
can3 = Canvas(ablak, width=15, height=15, bg='white')
tippek = ["kő", "papír", "olló"]
gep_valasztas = random.choice(tippek) # ko v papir v ollúő
jatek_valasztas = Label(ablak, text="Adja meg a tippjét: ")
jatek_valasztas_ki = Entry(ablak)

ablak.mainloop()