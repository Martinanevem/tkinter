from tkinter import messagebox

def infok():
    rules = '''
    Szabályok:
    - Játékos mozgatja a kígyót (fel, le, balra, jobbra – nyilak).
    - Nehézségi szint (mozgás, hossz) növekszik a kígyó által megevett egység után.
    - A kígyó nem ütközhet magának, se a falnak.

    Általános szabályok:
    - A játék célja, hogy a kígyó minél több ételt (pontot) gyűjtsön össze.
    - Az étel megjelenik a játékterületen véletlenszerű helyeken.
    - A kígyó automatikusan mozog a kiválasztott irányba.
    - A játékos irányítja a kígyó mozgását a nyilak segítségével.
    - Ha a kígyó feje ütközik a testével vagy a falakkal, a játék véget ér.
    - A játékos pontot kap minden egyes megevett ételért.
    '''

    messagebox.showinfo("Információk", rules)

infok()
