import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def infok():
    rules = '''
    Szabályok:
    - Windows az alapértelmezett támogatott rendszer, de ez a script-ben átírható.
    - Amennyiben a betű nem szerepel a kitalálandó szóban, úgy egy akasztófa egy része kerül lerajzolásra.
    - Maximális hibakorlát 10, vagyis fix 10 betűt ronthat.
    - 3 extrás segítség jár a játékhoz (alapértelmezetten be vannak kapcsolva):
        - szófaj: megmondja a szófaját az adott elemről.
        - leírás: egy rövid ismertetőt ad az adott véletlenszerűen kiválaszott elemről.
        - kép: egy rövid ideig (2-3 mp) egy képet jelenít meg, melyeket a "Kepek" mappában találsz.
    - Minden segítséget csak egyszer használhatsz fel a játék során, melyet a "/segítség" beírásával aktiválhatsz.
    - A szavakat a "szavak.json" nevű fájlban találhatod meg.
    - Befejezni akkor fogja a felhasználó, ha az összes betűt kitalálja.

    Hogyan kell játszani:
    1. Elindítás: A "Játék indítása" menüponttal indíthatod el a játékot.
    2. A szó kitalálása: A játék során meg kell találnod a rejtett szót.
    3. Betűk megadása: A betűket a billentyűzeten keresztül vagy a gombok segítségével adhatod meg.
    4. Segítség használata: Ha segítségre van szükséged, a "/segítség" parancsot írd be.
    5. Játék vége: A játék akkor ér véget, ha az összes betűt kitalálod, vagy eléred a maximális hibakorlátot.

    Jó szórakozást a játékhoz!
    '''

    messagebox.showinfo("Információk", rules)

infok()
