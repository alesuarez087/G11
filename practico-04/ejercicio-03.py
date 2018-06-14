from tkinter import *
from tkinter import ttk, font


class Application():
    def __init__(self):

        self.root = Tk()
        self.root.title("CIUDADES Y SU CODIGO POSTAL")
        self.root.geometry("350x400")

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.mostrar()

        self.root.mainloop()


    def mostrar(self):

         tree = ttk.Treeview(self.root, columns=("one"))
         tree.column("one",width=100, anchor="center")

         tree.heading("#0", text="Ciudad")
         tree.heading("one", text="Cod. postal")

         tree.insert("" , 0, text="Funes", values=("2132"))
         tree.insert("" , 0, text="Roldan", values=("2134"))
         tree.insert("" , 0, text="San Jorge", values=("2452"))
         tree.insert("" , 0, text="Rosario", values=("2000"))
         tree.insert("" , 0, text="Concordia", values=("3200"))


         tree.pack(side = TOP, fill=BOTH, expand=True)

    def cerrar(self):
        self.root.destroy()
        self.root.quit()




if __name__ == '__main__':
    Application()
