import tkinter
from tkinter import ttk
from tkinter.ttk import Style, Treeview

from logica import *
from tkinter import *
from PIL import ImageTk, Image
from canvas import *
from settings import *


class Table:

    def __init__(self, root, lst, **kwargs):
        super(Table, self).__init__()
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


class Application:
    state = 0
    parity = par

    def __init__(self):

        # Window
        self.root = Tk()
        self.root.title("Hamming Code")
        # self.root.iconbitmap("IMAGENES/INTERFAZ/icono.ico")
        self.root.geometry("1315x780+103+15")
        self.root.overrideredirect(False)
        self.root.resizable(False, False)
        self.root.configure(background='#122e45')

        # Header Canvas
        self.headerCanvas = ResizingCanvas(self.root, height=95, bg=headerColor, highlightthickness=0)
        self.headerCanvas.pack(fill=X, expand=YES)

        # Body Canvas
        self.bodyCanvas = ResizingCanvas(self.root, bg=bodyColor, highlightthickness=0)
        self.bodyCanvas.pack(fill=BOTH, expand=YES)

        # Label de instruccion.
        self.headerLabel = Label(self.headerCanvas, text=label1, bg=headerColor, fg=white, font=(font, 16))
        self.headerLabel.place(x=15, y=32)

        # Entry del numero.
        self.numberEntry = Entry(self.headerCanvas, width=20, font=(font, 14), relief="flat")
        self.numberEntry.place(x=300, y=35)
        self.numberEntry.bind("<Return>", self.onEnter)

        # Toggle Button
        self.switchbtn0 = PhotoImage(file="resources/toggle_on.png")
        self.switchbtn1 = PhotoImage(file="resources/toggle_off.png")
        self.switchLabel = Label(self.headerCanvas, image=self.switchbtn0, width=85, height=85, bg=headerColor)
        self.switchLabel.bind("<Button-1>", self.switch)
        self.switchLabel.place(x=1200, y=20)

        # Toggle Label
        self.dirTxt = StringVar()
        self.dirTxt.set(par)
        self.toggleText = Label(self.headerCanvas, textvariable=self.dirTxt, justify=CENTER, anchor='center',
                                bg=headerColor, fg=white, font=(font, 12), width=8, height=1)
        self.toggleText.place(x=1200, y=9)

        # Frame Base
        self.groundFrame = Canvas(self.bodyCanvas, bg=groundFrameColor, width=450, height=150,
                                  highlightbackground="black")
        self.groundFrame.place(x=0, y=0)

        # Conversion Widgets
        self.cnvVar = StringVar("")
        self.cnvLabel = Label(self.groundFrame, textvariable=self.cnvVar, justify=LEFT, anchor="nw",
                              bg=groundFrameColor, fg=white, font=(font, 13))
        self.cnvLabel.place(x=10, y=5)

        # Conversion Widgets
        self.nrziVar = StringVar("")
        self.nzriLabel = Label(self.groundFrame, textvariable=self.nrziVar, bg=groundFrameColor, fg=white,
                               font=(font, 22, 'bold'))
        self.nzriLabel.place(x=2, y=100)

        # frame for the table
        self.tableFrame = Canvas(self.bodyCanvas, bg=groundFrameColor, width=200, height=100)
        self.tableFrame.place(x=10, y=300)

        self.tree = Treeview(self.tableFrame, selectmode="extended")
        self.tree['columns'] = ('p1', 'p2', 'd1', 'p3', 'd2', 'd3', 'd4', 'p4', 'd5', 'd6', 'd7', 'd8')

        # COLUMNAS y HEADINGS
        columns = ('p1', 'p2', 'd1', 'p3', 'd2', 'd3', 'd4', 'p4', 'd5', 'd6', 'd7', 'd8')
        for i in range(len(columns)):
            self.tree.column(columns[i], minwidth=25, width=70, stretch=NO, anchor=CENTER)
            self.tree.heading(columns[i], text=columns[i], anchor=CENTER)
        self.tree.column('#0', width=100, stretch=NO, anchor=CENTER)
        self.tree.heading('#0', text='Valor', anchor=CENTER)

        self.tree.pack(expand=NO, fill=BOTH)

        # Loop
        self.root.mainloop()

    # Funcion para detectar enter en el entry.
    def onEnter(self, event):
        self.mostrar_conversiones()
        self.mostrar_codigo_nrzi()
        self.showTable()

    def showTable(self):
        data = [(1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1),
                (1, '', 0, "", 1, '', 0, "", 0, '', 1, ''),
                ("", 0, 0, '', '', 1, 1, '', '', 0, 0, ''),
                ("", "", "", 1, 1, 0, 0, '', '', '', '', 1),
                ('', '', '', '', '', '', '', '', 0, 1, 1, 0),
                (1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0)
        ]
        desc_lst = ["Sin paridad", "p1", "p2", "p3", "p4", "Con paridad"]

        descripcion = 0
        count = 0

        for e in data:
            self.tree.insert(parent='', index='end', iid=count, text=desc_lst[descripcion],
                             values=(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11]))
            count += 1
            descripcion += 1

        # t = Table(self.tableFrame, lst)

    # Funcion para detectar click en el toggle button y para cambiar paridad.
    def switch(self, event):
        if self.state == 1:
            self.switchLabel.config(image=self.switchbtn0)
            self.dirTxt.set(par)
            self.parity = par
            self.state = 0
            print("PARIDAD :" + self.parity)

        else:
            self.switchLabel.config(image=self.switchbtn1)
            self.dirTxt.set(impar)
            self.parity = impar
            self.state = 1
            print("PARIDAD :" + self.parity)

    def mostrar_codigo_nrzi(self):
        num = self.numberEntry.get()

        if is_binary(num) == 0:
            self.nrziVar.set("")
            return

        codigo = obtener_codigo_nrzi(num, "bajo")
        resultado = ""
        print(resultado)

        for x in codigo:
            if x == "alto":
                resultado += "|¯"
            else:
                resultado += "|_"  # ㇄
        self.nrziVar.set(resultado)

    def mostrar_conversiones(self):
        self.cnvVar.set(convertir_binario_h_o_d(self.numberEntry.get()))
