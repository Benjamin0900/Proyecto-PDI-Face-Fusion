import tkinter

class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio")

        # Obtener las dimensiones de la pantalla
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calcular el tamaño mediano de la pantalla
        width = int(screen_width * 0.6)
        height = int(screen_height * 0.6)

        # Establecer el tamaño y color de la ventana de inicio
        self.master.geometry(f"{width}x{height}+{int((screen_width - width) / 2)}+{int((screen_height - height) / 2)}")
        self.master.configure(bg="#276E90")  # Color principal

        # Modificar la etiqueta
        self.label = tkinter.Label(master, text="FaceFusion", bg="#276E90", fg="#EFEFEF", font=("Helvetica", 24))  # Texto en color claro
        self.label.pack(pady=height // 4)  # Ajustar el pady para que ocupe 2/4 de la ventana

        self.start_button = tkinter.Button(master, text="Iniciar aplicación", command=self.open_main_window, bg="#0A3143", fg="#EFEFEF")  # Color oscuro, Texto en color claro
        self.start_button.pack(pady=10)

    def open_main_window(self):
        self.master.destroy()
        main_window = tkinter.Tk()
        App(main_window, 'Trippy')


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Labels
        label1 = tkinter.Label(window, text="Filters", bg="#276E90", fg="#EFEFEF")
        label1.grid(row=0, column=13, columnspan=5)

        label2 = tkinter.Label(window, text="Saving", bg="#276E90", fg="#EFEFEF")
        label2.grid(row=8, column=13, columnspan=5)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width=600, height=400, bg="#276E90")
        self.canvas.grid(row=0, column=1, rowspan=15, columnspan=5)

        # Button that lets the user take a snapshot
        self.b_snap = tkinter.Button(window, text="Snapshot", width=50, bg="#0A3143", fg="#EFEFEF")  # Color oscuro, Texto en color claro
        self.b_snap.grid(row=12, column=3, rowspan=7)

        # Button for applying the other filters!
        self.b1 = tkinter.Button(window, text="Anonimous", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b1.grid(row=1, column=13)

        self.b2 = tkinter.Button(window, text="Anime", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b2.grid(row=1, column=17)

        self.b3 = tkinter.Button(window, text="Cat", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b3.grid(row=3, column=13)

        self.b3_2 = tkinter.Button(window, text="Dog", width=10, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b3_2.grid(row=4, column=13)

        self.b4 = tkinter.Button(window, text="Jason Joker", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b4.grid(row=3, column=17)

        # note, sobel filters use the same button, multiple clicks
        self.b5 = tkinter.Button(window, text="Gold Crown", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b5.grid(row=5, column=13)

        self.b6 = tkinter.Button(window, text="Flower Crown", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b6.grid(row=5, column=17)

        self.b8 = tkinter.Button(window, text="Color/No Filter", width=15, bg="#CECFC9", fg="#276E90")  # Primer complementario, Texto en color principal
        self.b8.grid(row=7, column=17)

        self.b9 = tkinter.Button(window, text="Snap Dat!", bg="#276E90", fg="#EFEFEF")
        self.b9.grid(row=9, rowspan=2, column=13, columnspan=4)

        self.b10 = tkinter.Button(window, text="Close Program", bg="#276E90", fg="#EFEFEF")
        self.b10.grid(row=9, rowspan=2, column=17, columnspan=2)

        self.window.mainloop()

# Crear la ventana de inicio
start_page_window = tkinter.Tk()
start_page = StartPage(start_page_window)

# Iniciar el bucle principal
start_page_window.mainloop()
