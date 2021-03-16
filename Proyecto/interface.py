import os
from tkinter import *
from tkinter import messagebox

from hammingcode import *
from logica import *
from settings import *


##Funciones
# Funcion para detectar enter en el entry.
def onEnter(event):
    mostrar_conversiones()
    mostrar_codigo_nrzi()


# Funcion para detectar click en el toggle button y para cambiar paridad.
def switch(event):
    global parity
    if parity == 'impar':
        switchLabel.config(image=switchbtn0)
        dirTxt.set('Par')
        parity = 'par'
        # print("PARIDAD :" + parity)

    else:
        switchLabel.config(image=switchbtn1)
        dirTxt.set('Impar')
        parity = 'impar'
        # print("PARIDAD :" + parity)


def mostrar_codigo_nrzi():
    num = numberEntry.get()

    if is_binary(num) == 0:
        nrziVar.set("")
        return

    codigo = obtener_codigo_nrzi(num, "bajo")
    resultado = ""
    print(resultado)

    for x in codigo:
        if x == "alto":
            resultado += "|¯"
        else:
            resultado += "|_"  # ㇄
    nrziVar.set(resultado)


def mostrar_conversiones():
    cnvVar.set(convertir_binario_h_o_d(numberEntry.get()))


# Tabla 1.
def createTable(columnsNames, rowsNames, canvas):
    cols = []
    # Headers
    for c in range(len(columnsNames)):
        cell = Label(canvas, font=(font, 11, 'bold'), text=columnsNames[c], width=3, relief="flat", bg=white,
                     justify='center')
        cell.grid(row=0, column=c, sticky=NSEW, padx=(0, 1), pady=(1, 1))
        if c == 0:
            cell.config(bg=bodyColor)
            cell.grid(pady=(0, 1))
        cols.append(cell)
    rows1.append(cols)
    # Descriptions
    for r in range(len(rowsNames)):
        cols = []
        cell = Label(canvas, font=(font, 11, 'bold'), text=rowsNames[r], width=27, relief="flat", bg=white,
                     justify='center')
        cell.grid(row=r + 1, column=0, sticky=NSEW, padx=(1, 0), pady=(0, 1))
        if r == 0 or r == (len(rowsNames) - 1):
            cell.config(bg=tablesColor)
        cols.append(cell)
        rows1.append(cols)

    # Data
    for r in range(len(rowsNames)):
        cols = rows1[r + 1]
        for c in range(len(columnsNames) - 1):
            cell = Label(canvas, font=(font, 11), width=3, relief="flat", bg=white, justify='center')
            cell.grid(row=r + 1, column=c + 1, sticky=NSEW, padx=(1, 0), pady=(0, 1))
            if r == 0 or r == (len(rowsNames) - 1):
                cell.config(bg=tablesColor)
            if c in (0, 1, 3, 7, 15):
                cell.config(font=(font, 11, 'bold'))
            cols.append(cell)


# Fill table1
def fillTable1():
    num = numberEntry.get()  # Obtener el número.
    matrix = obtener_matriz_tabla_1(num, parity)  # Obtener matriz.
    if not matrix:
        messagebox.showerror("Error!", "El número ingresado debe ser de 12 bits.")
        return
    result = str(palabra_con_paridad(matrix))  # Resultado con paridad.

    index = 0
    for r in range(1, len(description1), 1):
        for c in range(len(headers1) - 1):
            if r == 1 and not (c in (0, 1, 3, 7, 15)):
                data = num[index]
                index += 1
                rows1[r][c + 1].config(text=data)

            if r == (len(description1) - 1):
                data = result[c]
                rows1[r + 1][c + 1].config(text=data)

            elif (r - 1) in (0, 1, 2, 3, 4):
                # print (matrix[r-2])
                rows1[r + 1][c + 1].config(text=matrix[r - 1][c])


# matrix
# R =  0 a 4.
# C = 0 a 15.

# Deberia ir
# R = 0 a 6 debe ir de 0 a 6
# C = 0 15 pero es 1 a 16


# Window
root = Tk()
root.title("Hamming Code")
# root.geometry("1315x780+103+15")
root.overrideredirect(False)
# root.resizable(False, False)
root.configure(background='black')

# Header Canvas
headerCanvas = Canvas(root, bg=headerColor, highlightthickness=0)

# Body Canvas
bodyCanvas = Canvas(root, bg=bodyColor, highlightthickness=0)

# Label de instruccion.
headerLabel = Label(headerCanvas, text=label1, bg=headerColor, fg=white, font=(font, 16))

# Entry del numero.
numberEntry = Entry(headerCanvas, width=20, font=(font, 14), relief="flat")
numberEntry.insert(0, '101010101010')
numberEntry.bind("<Return>", onEnter)

# Button para llamar a Hamming
hammingImg = PhotoImage(file="resources/hamming.png")
hammingButton = Button(headerCanvas, image=hammingImg, command=fillTable1, bg=headerColor, activebackground=headerColor,
                       relief='flat', borderwidth=0)

# Toggle Button
switchbtn0 = PhotoImage(file="resources/toggle_on.png")
switchbtn1 = PhotoImage(file="resources/toggle_off.png")
switchLabel = Label(headerCanvas, image=switchbtn0, width=70, height=50, bg=headerColor)
switchLabel.bind("<Button-1>", switch)

# Toggle Label
dirTxt = StringVar()
dirTxt.set(parity)
toggleText = Label(headerCanvas, textvariable=dirTxt, justify=CENTER, anchor='center',
                   bg=headerColor, fg=white, font=(font, 10), width=8)

# Frame Base
groundFrame = Frame(bodyCanvas, bg=groundFrameColor, width=500, height=150)

# Conversion Widgets
cnvVar = StringVar("")
cnvLabel = Label(groundFrame, textvariable=cnvVar, justify=LEFT, anchor="nw",
                 bg=groundFrameColor, fg=white, font=(font, 13), height=5)

# Conversion Widgets
nrziVar = StringVar("")
nzriLabel = Label(groundFrame, textvariable=nrziVar, bg=groundFrameColor, fg=white,
                  font=(font, 22, 'bold'))

# tables
l1 = Label(bodyCanvas, text="Tabla 1. Cálculo de los bits de paridad en el código Hamming.", bg=bodyColor,
           font=(font, 13))
l2 = Label(bodyCanvas, text="Tabla 2. Comprobación de los bits de paridad.", bg=bodyColor, font=(font, 13))

c1 = Frame(bodyCanvas, bg=tablesColor, width=600, height=300)
c2 = Frame(bodyCanvas, bg=tablesColor, width=600, height=300)

# Create table
createTable(headers1, description1, c1)

# Shoving on screen.
headerCanvas.grid(row=0, column=0, sticky='NSEW', columnspan=5, rowspan=2)
bodyCanvas.grid(row=2, column=0, sticky='NSEW', columnspan=5, rowspan=5)
headerLabel.grid(row=0, column=0, columnspan=1, padx=5, sticky='EW')
numberEntry.grid(row=0, column=1, columnspan=1, padx=5, pady=25)
hammingButton.grid(row=0, column=3, sticky='NSEW', padx=40, pady=5)
switchLabel.grid(row=0, column=5, pady=(0, 5), sticky='S')
toggleText.grid(row=0, column=5, pady=(10, 0), sticky='N')
groundFrame.grid(row=2, column=0, rowspan=2, columnspan=6, padx=5, pady=5, sticky='NSEW')
cnvLabel.grid(row=0, column=0, columnspan=2, rowspan=2, padx=15, pady=15, sticky='NSEW')
nzriLabel.grid(row=0, column=2, columnspan=2, rowspan=2, padx=15, pady=15, sticky='NSEW')
l1.grid(row=4, column=0, columnspan=3, padx=10, pady=10, ipady=5)
l2.grid(row=4, column=3, columnspan=3)
c1.grid(row=5, column=0, rowspan=3, columnspan=3, padx=10, pady=5, sticky='N')
c2.grid(row=5, column=3, rowspan=3, columnspan=3, padx=10, pady=5, sticky='N')

root.mainloop()
