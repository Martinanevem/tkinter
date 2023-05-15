
vannak_adatok = False
felhasznalonev = ""; jelszo=""

def felhasznalo(felhasznalonev, jelszo):
    print(felhasznalonev, jelszo)


def regisztracio():
    felhasznalonev = "teszt" #be kell kérni EVAL -al!
    jelszo = "JELSZO!!!" #be kell kérni EVAL -al!

    if jelszo is not None and jelszo != "" and jelszo != " ":
        if jelszo != jelszo.isalpha():
            with open ("adatok.json", "w", encoding="UTF-8") as adatok:
                adatok.write(felhasznalonev + ";" +  jelszo)
                felhasznalo(felhasznalonev, jelszo)
        else:
            #irassa ki, hogy számnak is kell benne lennie!
            pass
    else:
        #irassa ki, hogy nem lehet üres!
        pass

def bejelentkezes():
    osszes_adat = []
    with open("adatok.json", "r", encoding="UTF-8") as adatok:
        sor = adatok.readline()
        while sor:
            osszes_adat.append(sor.split(";"))
            sor = adatok.readline()
        adatok.close()

    for i in osszes_adat:
        felhasznalonev = i[0]
        jelszo = i[1]

    if len(osszes_adat) != 0:
        felhasznalo(felhasznalonev, jelszo)
    else:
        print("Még nincs felhasználó az adatokban!") #át kell írni hibára -> irányítsa át a regisztrációhoz
        regisztracio()

if __name__ == "__main__":
    bejelentkezes()