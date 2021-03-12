from logica import *
from tkinter import *


class Application:

    parity = "par"

    def __init__(self):

        self.root = Tk()
        self.root.geometry("1024x568")

        self.label_ingrese_binario = Label(self.root, text="Ingrese un numero binario:                ")
        self.label_ingrese_binario.grid(row=0, column=0)

        self.my_entry = Entry(self.root, width=30)
        self.my_entry.grid(row=0, column=1)

        self.var_label_conversiones = StringVar()
        self.var_label_conversiones.set("")
        self.label_conversiones = Label(self.root, textvariable=self.var_label_conversiones)
        self.label_conversiones.grid(row=2, column=0)

        self.var_label_nrzi = StringVar()
        self.var_label_nrzi.set("")
        self.label_nrzi = Label(self.root, textvariable=self.var_label_nrzi, font=("Verdana", 24))
        self.label_nrzi.grid(row=3, column=0)

        self.button1 = Button(self.root, text="Aceptar", command=self.button_funcion)
        self.button1.grid(row=0, column=2)

        self.opcion = IntVar()  # Como StrinVar pero en entero

        Radiobutton(self.root, text="Paridad par", variable=self.opcion,
                    value=1, command=self.selec).grid(row=0, column=3)
        Radiobutton(self.root, text="Paridad impar", variable=self.opcion,
                    value=2, command=self.selec).grid(row=1, column=3)

        self.root.title("Hamming code")

        self.root.mainloop()

    def selec(self):
        if self.opcion.get() == 1:
            self.parity = "par"
        if self.opcion.get() == 2:
            self.parity = "impar"

        print("paridad " + self.parity)

    def button_funcion(self):
        self.mostrar_conversiones()
        self.mostrar_codigo_nrzi()

    def mostrar_codigo_nrzi(self):

        num = self.my_entry.get()

        if is_binary(num) == 0:
            self.var_label_nrzi.set("")
            return

        codigo = obtener_codigo_nrzi(num, "bajo")
        resultado = ""
        print(resultado)

        for x in codigo:
            if x == "alto":
                resultado += "|¯"
            else:
                resultado += "|_"
        self.var_label_nrzi.set(resultado)

    def mostrar_conversiones(self):
        self.var_label_conversiones.set(convertir_binario_h_o_d(self.my_entry.get()))


    #def prueba(self):
    #    self.varLabel.set("value")
