import tkinter as tk
from interfaz_generada import App
import suma


class Ventana(App):
    def __init__(self, parent):
        super(Ventana, self).__init__(parent)
        entrys = [
            self.en_00, self.en_01, self.en_02,
            self.en_10, self.en_11, self.en_12,
            self.en_20, self.en_21, self.en_22
        ]
        for entry in entrys:
            entry.bind("<Return>", self.sumaCuadros)
        entrys[0].focus_set()
        
    def sumaCuadros(self, e):
        valores = self.valoresLista()
        # suma filas
        self.lb_fila0.config(text=str(suma.fila(0, valores))) 
        self.lb_fila1.config(text=str(suma.fila(1, valores)))
        self.lb_fila2.config(text=str(suma.fila(2, valores)))
        # suma columna
        self.lb_col0.config(text=str(suma.columna(0, valores)))
        self.lb_col1.config(text=str(suma.columna(1, valores)))
        self.lb_col2.config(text=str(suma.columna(2, valores)))
        # suma diagonales
        self.lb_sone.config(text=str(suma.diagonalSoNe(valores)))
        self.lb_nose.config(text=str(suma.diagonalNoSe(valores)))


if __name__=="__main__":
    raiz = tk.Tk()
    app = Ventana(raiz)
    raiz.mainloop()