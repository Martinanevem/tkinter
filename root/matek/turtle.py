import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import os


class Turtle:
    def __init__(self):
        self.tollat_fel = False
        self.szin = "black"
        self.canvas_width = 800
        self.canvas_height = 600
        self.turtle_size = 40
        self.turtle_step = 10

        self.window = tk.Tk()
        self.window.title("Turtle - a teknősbéka")
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        current_directory = os.path.dirname(os.path.abspath(__file__))
        kepek_folder_path = os.path.join(current_directory, '..', 'kepek')
        kepek_folder_path = os.path.normpath(kepek_folder_path)
        image_file_path = os.path.join(kepek_folder_path, 'turtle', 'turtle.gif')

        '''
        self.canvas.configure(bg="yellow")
        self.canvas.update()
        '''

        # Teknoc kep letrehozasa
        self.turtle_image = Image.open(image_file_path)
        self.turtle_image = self.turtle_image.resize((self.turtle_size, self.turtle_size), Image.ANTIALIAS)

        # canvas + turtle
        self.turtle = self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, image=None)

        # forgatas
        self.turtle_x = self.canvas_width / 2
        self.turtle_y = self.canvas_height / 2
        self.turtle_angle = 0

        self.canvas.focus_set()
        self.canvas.bind("<Up>", self.move_forward)
        self.canvas.bind("w", self.move_forward)
        self.canvas.bind("<Down>", self.move_backward)
        self.canvas.bind("s", self.move_backward)
        self.canvas.bind("<Left>", self.rotate_left)
        self.canvas.bind("a", self.rotate_left)
        self.canvas.bind("<Right>", self.rotate_right)
        self.canvas.bind("d", self.rotate_right)
        self.canvas.bind("<c>", self.szinpaletta)
        self.canvas.bind("<k>", self.tollat_fel_def)

        #  a kezdo teknoc kepe
        turtle_photo = ImageTk.PhotoImage(self.turtle_image)
        self.canvas.itemconfig(self.turtle, image=turtle_photo)
        self.canvas.image = turtle_photo

    def move_forward(self, event):
        self.turtle_x += self.turtle_step * math.cos(math.radians(self.turtle_angle))
        self.turtle_y -= self.turtle_step * math.sin(math.radians(self.turtle_angle))
        self.canvas.coords(self.turtle, self.turtle_x, self.turtle_y)
        if not self.tollat_fel:
            self.canvas.create_line(
                self.turtle_x,
                self.turtle_y,
                self.turtle_x - self.turtle_step * math.cos(math.radians(self.turtle_angle)),
                self.turtle_y + self.turtle_step * math.sin(math.radians(self.turtle_angle)),
                fill=self.szin
            )

    def move_backward(self, event):
        self.turtle_x -= self.turtle_step * math.cos(math.radians(self.turtle_angle))
        self.turtle_y += self.turtle_step * math.sin(math.radians(self.turtle_angle))
        self.canvas.coords(self.turtle, self.turtle_x, self.turtle_y)
        if not self.tollat_fel:
            self.canvas.create_line(
                self.turtle_x,
                self.turtle_y,
                self.turtle_x + self.turtle_step * math.cos(math.radians(self.turtle_angle)),
                self.turtle_y - self.turtle_step * math.sin(math.radians(self.turtle_angle)),
                fill=self.szin
            )

    def rotate_left(self, event):
        self.turtle_angle = (self.turtle_angle + 10) % 360
        rotated_image = self.turtle_image.rotate(self.turtle_angle)
        turtle_photo = ImageTk.PhotoImage(rotated_image)
        self.canvas.itemconfig(self.turtle, image=turtle_photo)
        self.canvas.image = turtle_photo

    def rotate_right(self, event):
        self.turtle_angle = (self.turtle_angle - 10) % 360
        rotated_image = self.turtle_image.rotate(self.turtle_angle)
        turtle_photo = ImageTk.PhotoImage(rotated_image)
        self.canvas.itemconfig(self.turtle, image=turtle_photo)
        self.canvas.image = turtle_photo

    def tollat_fel_def(self, event):
        self.tollat_fel = not self.tollat_fel

    def szinpaletta(self, event):
        szinpaletta_ablak = tk.Tk()

        def szin_modositas(szin2):
            self.szin = szin2
            vege()

        def hatterszin_modositas(szin2):
            self.canvas.configure(bg=szin2)
            self.canvas.update()

        def vege():
            szinpaletta_ablak.destroy()

        def tollat_fel():
            self.tollat_fel = not self.tollat_fel
            vege()

        # 4 szín lesz
        elso_szin = tk.Button(szinpaletta_ablak, text="", bg="BLUE", font=('Helvetica bold', 36),
                              command=lambda: szin_modositas("BLUE"))
        elso_szin.grid(row=1, column=1, rowspan=5)

        masodik_szin = tk.Button(szinpaletta_ablak, text="", bg="RED", font=('Helvetica bold', 36),
                                 command=lambda: szin_modositas("RED"))
        masodik_szin.grid(row=1, column=2, rowspan=5)

        harmadik_szin = tk.Button(szinpaletta_ablak, text="", bg="GREEN", font=('Helvetica bold', 36),
                                  command=lambda: szin_modositas("GREEN"))
        harmadik_szin.grid(row=1, column=3, rowspan=5)

        negyedik_szin = tk.Button(szinpaletta_ablak, text="", bg="BLACK", font=('Helvetica bold', 36),
                                  command=lambda: szin_modositas("BLACK"))
        negyedik_szin.grid(row=6, column=1, rowspan=5)

        otodik_szin = tk.Button(szinpaletta_ablak, text="", bg="YELLOW", font=('Helvetica bold', 36),
                                command=lambda: szin_modositas("YELLOW"))
        otodik_szin.grid(row=6, column=2, rowspan=5)

        hatodik_szin = tk.Button(szinpaletta_ablak, text="", bg="ORANGE", font=('Helvetica bold', 36),
                                 command=lambda: szin_modositas("ORANGE"))
        hatodik_szin.grid(row=6, column=3, rowspan=5)

        elso_opcio = tk.Button(szinpaletta_ablak, text="Tollat fel (k)", bg="GRAY", font=('Helvetica bold', 12),
                               command=lambda: tollat_fel())
        elso_opcio.grid(row=13, column=1, columnspan=2)

        szoveg = tk.Label(szinpaletta_ablak, text="Háttérkép színe", font=('Helvetica bold', 16))
        szoveg.grid(row=1, column=5)

        elso_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="BLUE", font=('Helvetica bold', 16),
                                    command=lambda: hatterszin_modositas("BLUE"))
        elso_hatterszin.grid(row=2, column=4, padx=10, pady=10)

        masodik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="RED", font=('Helvetica bold', 16),
                                       command=lambda: hatterszin_modositas("RED"))
        masodik_hatterszin.grid(row=2, column=5, padx=10, pady=10)

        harmadik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="GREEN", font=('Helvetica bold', 16),
                                        command=lambda: hatterszin_modositas("GREEN"))
        harmadik_hatterszin.grid(row=2, column=6, padx=10, pady=10)

        negyedik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="BLACK", font=('Helvetica bold', 16),
                                        command=lambda: hatterszin_modositas("BLACK"))
        negyedik_hatterszin.grid(row=3, column=4, rowspan=5, padx=10, pady=10)

        otodik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="YELLOW", font=('Helvetica bold', 16),
                                      command=lambda: hatterszin_modositas("YELLOW"))
        otodik_hatterszin.grid(row=3, column=5, rowspan=5, padx=10, pady=10)

        hatodik_hatterszin = tk.Button(szinpaletta_ablak, text="", bg="ORANGE", font=('Helvetica bold', 16),
                                       command=lambda: hatterszin_modositas("ORANGE"))
        hatodik_hatterszin.grid(row=3, column=6, rowspan=5, padx=10, pady=10)

        szinpaletta_ablak.mainloop()

    def show_info_messagebox(self):
        info_window = tk.Toplevel(self.window)
        info_window.title("Turtle")
        info_window.geometry("250x200")

        screen_width = info_window.winfo_screenwidth()
        screen_height = info_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (250 / 2))
        y_coordinate = int((screen_height / 2) - (250 / 2))
        info_window.geometry(f"250x200+{x_coordinate}+{y_coordinate}")

        info_label = tk.Label(info_window,
                              text="Figyelem! \nA színpaletta megváltozott! \nÚj billentyű (c) megnyomásával hozhatod be! \nTollat fel: (k) billentyű. \nMozgás: Nyilak vagy WASD",
                              padx=20, pady=20)
        info_label.pack(expand=True)

        ok_button = tk.Button(info_window, text="OK", command=info_window.destroy, fg="blue", height=2, width=10)
        ok_button.pack(pady=10)

        info_window.attributes("-topmost", True)

    def start(self):
        self.show_info_messagebox()
        self.window.mainloop()
        

if __name__ == "__main__":
    turtle = Turtle()
    turtle.start()
