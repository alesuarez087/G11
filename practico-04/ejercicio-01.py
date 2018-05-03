"""1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 ."""


from tkinter import *
import time

def Sumar():
	try:
		_valorV1 = int(V1entrada.get())
		_valorV2= int(V2entrada.get())
		valor= _valorV1 + _valorV2
		etiquetaRes.config(text=valor)
	except ValueError:
		etiquetaRes.config(text="Introduce un numero!")

def Restar():
	try:
		_valorV1 = int(V1entrada.get())
		_valorV2= int(V2entrada.get())
		valor= _valorV1 - _valorV2
		etiquetaRes.config(text=valor)
	except ValueError:
		etiquetaRes.config(text="Introduce un numero!")

def Multiplicar():
	try:
		_valorV1 = int(V1entrada.get())
		_valorV2= int(V2entrada.get())
		valor= _valorV1 * _valorV2
		etiquetaRes.config(text=valor)
	except ValueError:
		etiquetaRes.config(text="Introduce un numero!")

def Dividir():
	try:
		_valorV1 = int(V1entrada.get())
		_valorV2= int(V2entrada.get())
		valor= _valorV1 / _valorV2
		etiquetaRes.config(text=valor)
	except ValueError:
		etiquetaRes.config(text="Introduce un numero!")
	except ZeroDivisionError:
		etiquetaRes.config(text="El divisor no puede ser cero")

ventana=Tk()

ventana.title("MINI - Calculadora")

ventana.resizable(True,False)

ventana.iconbitmap("calcu.ico")

ventana.geometry("450x100")

ventana.config(bg="blue")
#ventana.config(background="black", fg="#03f943", justify="right")
vp = Frame(ventana)
vp.config(bg="yellow")
vp.grid(column=0, row=0, padx=(70,70), pady=(10,10))
vp.columnconfigure(1, weight=1)
vp.rowconfigure(1, weight=1)

botonSum = Button(vp, text="+", command=Sumar)
botonSum.grid(row=9, column=16)

botonRes= Button(vp, text="-", command=Restar)
botonRes.grid(row=9, column=17)

botonMult= Button(vp, text="x", command=Multiplicar)
botonMult.grid(row=9, column=18)

botonDiv= Button(vp, text="/", command=Dividir)
botonDiv.grid(row=9, column=19)

V1=""
V1entrada = Entry(vp,width=10, textvariable = "V1" )
V1entrada.grid( row=9, column=4,padx=(30,30))

V2=""
V2entrada = Entry(vp,width=10, textvariable = "V2" )
V2entrada.grid( row=9, column=6,padx=(20,20))
#vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))

etiquetaV1 = Label(vp, width=10, text="1° Operando")
etiquetaV1.config(bg="yellow")
etiquetaV1.grid(column=4, row=8)

etiquetaV2 = Label(vp, width=10, text="2° Operando")
etiquetaV2.config(bg="yellow")
etiquetaV2.grid(column=6, row=8)

etiquetaRes = Label(ventana, text="Resultado")
etiquetaRes.config(bg="yellow")
etiquetaRes.grid(column=0, row=20, pady=(10,10))

ventana.mainloop()
