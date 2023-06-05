from tkinter import messagebox

def infok():
    rules = '''
    Szabályok:
    - A játék célja, hogy eltörjük az összes téglát a játékterületen.
    - A játékos egy kis labdát irányít, amelyet egy padlóra helyezett paddle segítségével ütöget, és ezzel eltöri a téglákat.
    - Ha a labda elhagyja a játékterületet (azaz leesik a paddle-ről), akkor az életvesztéssel jár, és a játékosnak új labdát kell elindítania.
    - A játékos pontot kap minden egyes eltört tégláért.
    '''

    messagebox.showinfo("Információk", rules)

infok()
