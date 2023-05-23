import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math

import os


def test():

    os.chdir("./matek")

    tollat_fel = False
    szin = "black"


    canvas_width = 800
    canvas_height = 600
    turtle_size = 40
    turtle_step = 10

    window = tk.Tk()
    window.title("Turtle - a teknősbéka")
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    '''
    canvas.configure(bg="yellow")
    canvas.update()
    '''

    # Teknoc kep letrehozasa
    turtle_image = Image.open("turtle.gif")
    turtle_image = turtle_image.resize((turtle_size, turtle_size), Image.ANTIALIAS)

    # canvas + turtle
    turtle = canvas.create_image(canvas_width/2, canvas_height/2, image=None)

    # forgatas
    turtle_x = canvas_width/2
    turtle_y = canvas_height/2
    turtle_angle = 0

    def move_forward(event):
        global turtle_x, turtle_y
        turtle_x += turtle_step * math.cos(math.radians(turtle_angle))
        turtle_y -= turtle_step * math.sin(math.radians(turtle_angle))
        canvas.coords(turtle, turtle_x, turtle_y)
        if not tollat_fel:
            canvas.create_line(turtle_x, turtle_y, turtle_x - turtle_step * math.cos(math.radians(turtle_angle)), turtle_y + turtle_step * math.sin(math.radians(turtle_angle)), fill=szin)
    def move_backward(event):
        global turtle_x, turtle_y
        turtle_x -= turtle_step * math.cos(math.radians(turtle_angle))
        turtle_y += turtle_step * math.sin(math.radians(turtle_angle))
        canvas.coords(turtle, turtle_x, turtle_y)
        if not tollat_fel:
            canvas.create_line(turtle_x, turtle_y, turtle_x + turtle_step * math.cos(math.radians(turtle_angle)), turtle_y - turtle_step * math.sin(math.radians(turtle_angle)), fill=szin)

    def rotate_left(event):
        global turtle_angle
        turtle_angle = (turtle_angle + 10) % 360
        rotated_image = turtle_image.rotate(turtle_angle)
        turtle_photo = ImageTk.PhotoImage(rotated_image)
        canvas.itemconfig(turtle, image=turtle_photo)
        canvas.image = turtle_photo

    def rotate_right(event):
        global turtle_angle
        turtle_angle = (turtle_angle - 10) % 360
        rotated_image = turtle_image.rotate(turtle_angle)
        turtle_photo = ImageTk.PhotoImage(rotated_image)
        canvas.itemconfig(turtle, image=turtle_photo)
        canvas.image = turtle_photo

    def tollat_fel_def(event):
        global tollat_fel
        tollat_fel = not tollat_fel

        

    def szinpaletta(event):
        szinpaletta_ablak = tk.Tk()

        def szin_modositas(szin2):
            global szin
            szin = szin2
            vege()
        
        def hatterszin_modositas(szin2):
            canvas.configure(bg=szin2)
            canvas.update()
        
        def vege():
            szinpaletta_ablak.destroy()
        
        def tollat_fel():
            global tollat_fel
            tollat_fel = not tollat_fel
            vege()


        #4 szín lesz
        elso_szin = tk.Button(szinpaletta_ablak, text="", bg="BLUE", font=('Helvetica bold', 36), command=lambda: szin_modositas("BLUE"))
        elso_szin.grid(row=1, column=1, rowspan=5)

        masodik_szin = tk.Button(szinpaletta_ablak, text="", bg="RED", font=('Helvetica bold', 36), command=lambda: szin_modositas("RED"))
        masodik_szin.grid(row=1, column=2, rowspan=5)

        harmadik_szin = tk.Button(szinpaletta_ablak, text="", bg="GREEN", font=('Helvetica bold', 36), command=lambda: szin_modositas("GREEN"))
        harmadik_szin.grid(row=1, column=3, rowspan=5)

        negyedik_szin = tk.Button(szinpaletta_ablak, text="", bg="BLACK", font=('Helvetica bold', 36), command=lambda: szin_modositas("BLACK"))
        negyedik_szin.grid(row=6, column=1, rowspan=5)

        otodik_szin = tk.Button(szinpaletta_ablak, text="", bg="YELLOW", font=('Helvetica bold', 36), command=lambda: szin_modositas("YELLOW"))
        otodik_szin.grid(row=6, column=2, rowspan=5)

        hatodik_szin = tk.Button(szinpaletta_ablak, text="", bg="ORANGE", font=('Helvetica bold', 36), command=lambda: szin_modositas("ORANGE"))
        hatodik_szin.grid(row=6, column=3, rowspan=5)

        elso_opcio = tk.Button(szinpaletta_ablak, text="Tollat fel (k)", bg="GRAY", font=('Helvetica bold', 12), command=lambda: tollat_fel())
        elso_opcio.grid(row=13, column=1, columnspan=2)

        szoveg = tk.Label(szinpaletta_ablak, text="Háttérkép színe", font=('Helvetica bold', 16))
        szoveg.grid(row=1, column=5)

        elso_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="BLUE", font=('Helvetica bold', 16), command=lambda: hatterszin_modositas("BLUE"))
        elso_hatterszin.grid(row=2, column=4, padx=10, pady=10)

        masodik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="RED", font=('Helvetica bold', 16), command=lambda: hatterszin_modositas("RED"))
        masodik_hatterszin.grid(row=2, column=5, padx=10, pady=10)

        harmadik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="GREEN", font=('Helvetica bold', 16), command=lambda: hatterszin_modositas("GREEN"))
        harmadik_hatterszin.grid(row=2, column=6, padx=10, pady=10)

        negyedik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="BLACK", font=('Helvetica bold', 16), command=lambda: hatterszin_modositas("BLACK"))
        negyedik_hatterszin.grid(row=3, column=4, rowspan=5, padx=10, pady=10)

        otodik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="YELLOW", font=('Helvetica bold', 16), command=lambda: hatterszin_modositas("YELLOW"))
        otodik_hatterszin.grid(row=3, column=5, rowspan=5, padx=10, pady=10)

        hatodik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="ORANGE", font=('Helvetica bold', 16), command=lambda: hatterszin_modositas("ORANGE"))
        hatodik_hatterszin.grid(row=3, column=6, rowspan=5, padx=10, pady=10)


        szinpaletta_ablak.mainloop()





    #billentyu parancsok
    canvas.focus_set()
    canvas.bind("<Up>", move_forward)
    canvas.bind("<Down>", move_backward)
    canvas.bind("<Left>", rotate_left)
    canvas.bind("<Right>", rotate_right)
    canvas.bind("<c>", szinpaletta)
    canvas.bind("<k>", tollat_fel_def)

    #  a kezdo teknoc kepe
    turtle_photo = ImageTk.PhotoImage(turtle_image)
    canvas.itemconfig(turtle, image=turtle_photo)
    canvas.image = turtle_photo

    def show_info_messagebox():
        info_window = tk.Toplevel(window)
        info_window.title("Turtle")
        info_window.geometry("250x200")  # Set the info_window size to 300x300

        # Center the info_window on the screen
        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (250 / 2))
        y_coordinate = int((screen_height / 2) - (250 / 2))
        info_window.geometry(f"250x200+{x_coordinate}+{y_coordinate}")

        info_label = tk.Label(info_window, text="Figyelem! \nA színpaletta megváltozott! \nÚj billentyű (c) megnyomásával hozhatod be! \n \n Tollat fel: (k) billentyű", padx=20, pady=20)
        info_label.pack(expand=True)

        ok_button = tk.Button(info_window, text="OK", command=info_window.destroy, fg="blue", height=2, width=10)
        ok_button.pack(pady=10)

        # Force the info_window to be on top
        info_window.attributes("-topmost", True)


    show_info_messagebox()

    window.mainloop()
