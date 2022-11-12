import tkinter as tk
from generado import App
import suma

class Ventana(App):
    def __init__(self, parent):
        super(Ventana, self).__init__(parent)

        self.en_00.bind("<Return>", self.sumaFila0)
        self.en_01.bind("<Return>", self.sumaFila0)
        self.en_02.bind("<Return>", self.sumaFila0)
        self.en_10.bind("<Return>", self.sumaFila1)
        self.en_11.bind("<Return>", self.sumaFila1)
        self.en_12.bind("<Return>", self.sumaFila1)
        self.en_20.bind("<Return>", self.sumaFila2)
        self.en_21.bind("<Return>", self.sumaFila2)
        self.en_22.bind("<Return>", self.sumaFila2)

    def sumaFila0(self, e):
        res = suma.fila(0, self.valoresLista())
        self.lb_fila0.config(text=str(res))

    def sumaFila1(self, e):
        res = suma.fila(1, self.valoresLista())
        self.lb_fila1.config(text=str(res))

    def sumaFila2(self, e):
        res = suma.fila(2, self.valoresLista())
        self.lb_fila2.config(text=str(res))


if __name__=="__main__":
    raiz = tk.Tk()
    app = Ventana(raiz)
    app.valoresLista()

    raiz.mainloop()