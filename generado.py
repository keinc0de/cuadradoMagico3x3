import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=286
        height=219
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.num00 = tk.StringVar()
        self.en_00=tk.Entry(root, textvariable=self.num00)
        self.en_00["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_00["font"] = ft
        self.en_00["fg"] = "#333333"
        self.en_00["justify"] = "center"
        self.en_00["text"] = ""
        self.en_00.place(x=10,y=60,width=60,height=45)

        self.num01 = tk.StringVar()
        self.en_01=tk.Entry(root, textvariable=self.num01)
        self.en_01["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_01["font"] = ft
        self.en_01["fg"] = "#333333"
        self.en_01["justify"] = "center"
        self.en_01["text"] = ""
        self.en_01.place(x=80,y=60,width=60,height=45)

        self.num02 = tk.StringVar()
        self.en_02=tk.Entry(root, textvariable=self.num02)
        self.en_02["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_02["font"] = ft
        self.en_02["fg"] = "#333333"
        self.en_02["justify"] = "center"
        self.en_02["text"] = ""
        self.en_02.place(x=150,y=60,width=60,height=45)

        self.num10 = tk.StringVar()
        self.en_10=tk.Entry(root, textvariable=self.num10)
        self.en_10["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_10["font"] = ft
        self.en_10["fg"] = "#333333"
        self.en_10["justify"] = "center"
        self.en_10["text"] = ""
        self.en_10.place(x=10,y=110,width=60,height=45)

        self.num11 = tk.StringVar()
        self.en_11=tk.Entry(root, textvariable=self.num11)
        self.en_11["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_11["font"] = ft
        self.en_11["fg"] = "#333333"
        self.en_11["justify"] = "center"
        self.en_11["text"] = ""
        self.en_11.place(x=80,y=110,width=60,height=45)

        self.num12 = tk.StringVar()
        self.en_12=tk.Entry(root, textvariable=self.num12)
        self.en_12["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_12["font"] = ft
        self.en_12["fg"] = "#333333"
        self.en_12["justify"] = "center"
        self.en_12["text"] = ""
        self.en_12.place(x=150,y=110,width=60,height=45)

        self.num20 = tk.StringVar()
        self.en_20=tk.Entry(root, textvariable=self.num20)
        self.en_20["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_20["font"] = ft
        self.en_20["fg"] = "#333333"
        self.en_20["justify"] = "center"
        self.en_20["text"] = ""
        self.en_20.place(x=10,y=160,width=60,height=45)

        self.num21 = tk.StringVar()
        self.en_21=tk.Entry(root, textvariable=self.num21)
        self.en_21["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_21["font"] = ft
        self.en_21["fg"] = "#333333"
        self.en_21["justify"] = "center"
        self.en_21["text"] = ""
        self.en_21.place(x=80,y=160,width=60,height=45)

        self.num22 = tk.StringVar()
        self.en_22=tk.Entry(root, textvariable=self.num22)
        self.en_22["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        self.en_22["font"] = ft
        self.en_22["fg"] = "#333333"
        self.en_22["justify"] = "center"
        self.en_22["text"] = ""
        self.en_22.place(x=150,y=160,width=60,height=45)

        self.lb_col0=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lb_col0["font"] = ft
        self.lb_col0["fg"] = "#333333"
        self.lb_col0["justify"] = "center"
        self.lb_col0["text"] = ""
        self.lb_col0.place(x=10,y=10,width=60,height=45)

        self.lb_col1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lb_col1["font"] = ft
        self.lb_col1["fg"] = "#333333"
        self.lb_col1["justify"] = "center"
        self.lb_col1["text"] = ""
        self.lb_col1.place(x=80,y=10,width=60,height=45)

        self.lb_col2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        self.lb_col2["font"] = ft
        self.lb_col2["fg"] = "#333333"
        self.lb_col2["justify"] = "center"
        self.lb_col2["text"] = ""
        self.lb_col2.place(x=150,y=10,width=60,height=45)

        self.lb_sone=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        self.lb_sone["font"] = ft
        self.lb_sone["fg"] = "#333333"
        self.lb_sone["justify"] = "center"
        self.lb_sone["text"] = ""
        self.lb_sone.place(x=220,y=10,width=60,height=45)

        self.lb_fila0=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        self.lb_fila0["font"] = ft
        self.lb_fila0["fg"] = "#333333"
        self.lb_fila0["justify"] = "center"
        self.lb_fila0["text"] = ""
        self.lb_fila0.place(x=220,y=60,width=60,height=45)

        self.lb_fila1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        self.lb_fila1["font"] = ft
        self.lb_fila1["fg"] = "#333333"
        self.lb_fila1["justify"] = "center"
        self.lb_fila1["text"] = ""
        self.lb_fila1.place(x=220,y=110,width=60,height=45)

        self.lb_fila2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        self.lb_fila2["font"] = ft
        self.lb_fila2["fg"] = "#333333"
        self.lb_fila2["justify"] = "center"
        self.lb_fila2["text"] = ""
        self.lb_fila2.place(x=220,y=160,width=60,height=45)

    def _valores(self):
        d = {
            "v00":self.valorEntry(self.en_00),
            "v01":self.valorEntry(self.en_01),
            "v02":self.valorEntry(self.en_02),
            "v10":self.valorEntry(self.en_10),
            "v11":self.valorEntry(self.en_11),
            "v12":self.valorEntry(self.en_12),
            "v20":self.valorEntry(self.en_20),
            "v21":self.valorEntry(self.en_21),
            "v22":self.valorEntry(self.en_22)
        }
        return d

    def valorEntry(self, entry):
        v = entry.get()
        valor = 0
        if v!="" and v.isdigit():
            valor = int(v)
        return valor

    def valoresLista(self):
        d = self._valores()
        lista = []
        valores = list(d.values())
        for x in range(0, len(valores), 3):
            lista.append([valores[x], valores[x+1], valores[x+2]])
        return lista

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
