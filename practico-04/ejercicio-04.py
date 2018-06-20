from tkinter import *
from tkinter import ttk, font




class ABMCiudades():
	def __init__(self):
		self.root = Tk()
		self.root.title("ABM Ciudades")
		self.root.protocol("WM_DELETE_WINDOW", self.cerrar)
		# Fuente
		self.fuente = font.Font(family='tahoma',weight='bold', size=12)
		self.fuente1 = font.Font(family='tahoma', slant='italic', size=15)

		self.principal()
		self.item_id = ""
		self.ciudad = StringVar()
		self.postal = StringVar()
		self.root.mainloop()
		self.nom_pant=""


	def principal(self):
		frame = Frame(self.root, pady=20, borderwidth=0, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)

		self.tree = ttk.Treeview(frame, columns=("one"))
		self.tree.heading("#0", text="Ciudad")
		self.tree.heading("one", text="Cod. postal")
                #cambia el nombre de la pantalla
		self.nom_pant="Nueva Ciudad"
		#botones
		btn_add = Button(frame, text="Agregar", height=2, command=self.nuevo_o_editar)
		btn_edit = Button(frame, text="Editar", height=2, command=self.editar)
		btn_delete = Button(frame, text="Eliminar", height=2, command=self.eliminar)

		self.tree.pack(side = TOP, fill=BOTH, expand=True)
		btn_add.pack(side = LEFT, fill=BOTH, expand=True)
		btn_edit.pack(side = LEFT, fill=BOTH, expand=True)
		btn_delete.pack(side = LEFT, fill=BOTH, expand=True)


	def agregar(self):

		if(self.item_id != ""):
			self.tree.item(self.item_id, text=self.ciudad.get(), values=(self.postal.get()))
		else:
			self.tree.insert("", 0, text=self.ciudad.get(), values=(self.postal.get()))
		self.cancelar()




	def editar(self):
		self.item_id = self.tree.focus()
		if(self.item_id != ""):
			item = self.tree.item(self.item_id)
			self.ciudad.set(item['text'])
			self.postal.set(item['values'][0])
                        #cambia el nombre de la pantalla
			self.nom_pant="Editar Ciudad"
			self.nuevo_o_editar()
		else:
			print("Debe seleccionar una ciudad para Editar")






	def eliminar(self):
		try:
			seleccionado = self.tree.selection()[0]
			self.tree.delete(seleccionado)
		except Exception as e:
			print("Debe seleccionar una ciudad para Borrar")


	def nuevo_o_editar(self):
		self.modal = Toplevel(self.root)
		self.modal.title(self.nom_pant)
		self.modal.geometry('300x250')
		self.modal.resizable(0,0)

		frame = Frame(self.modal, pady=10)
		frame.pack(side = TOP, fill=BOTH, expand=True)


		#Etiquetas
		label1 = Label(frame, text="Ciudad :", font=self.fuente1, width=15)
		label2 = Label(frame, text="Cod. postal :", font=self.fuente1, width=15)


		entrada1 = Entry(frame, textvariable=self.ciudad, width=10, font=self.fuente)
		entrada2 = Entry(frame, textvariable=self.postal, width=10, font=self.fuente)

		#Separador
		separ = ttk.Separator(frame, orient=HORIZONTAL)

		#Botones
		btn_aceptar = Button(frame, text="Guardar", height=2, width=10, command=self.agregar)
		btn_cancelar = Button(frame, text="Cancelar", height=2, width=10, command=self.cancelar)


		label1.pack(side=TOP, fill=BOTH, expand=True,padx=1,pady=1)
		entrada1.pack(side=TOP, fill=X, expand=True, padx=5,pady=5)
		label2.pack(side=TOP, fill=BOTH, expand=True,padx=5,pady=5)
		entrada2.pack(side=TOP, fill=X, expand=True,padx=5,pady=5)
		separ.pack(side=TOP, fill=BOTH, expand=True,padx=5,pady=5)
		btn_aceptar.pack(side=LEFT, fill=BOTH, expand=True,padx=5,pady=5)
		btn_cancelar.pack(side=RIGHT, fill=BOTH, expand=True,padx=5,pady=5)

		self.nom_pant="Nueva Ciudad"



	def cancelar(self):
		self.item_id = ""
		self.ciudad.set("")
		self.postal.set("")
		self.modal.destroy()

	def cerrar(self):
		self.root.destroy()
		self.root.quit()

if __name__ == '__main__':
	ABMCiudades()
