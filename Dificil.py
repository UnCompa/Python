from tkinter import *
from tkinter import messagebox
from juegoDificil import *

elementoObtenido = []

ventana = Tk()
ventana.title("Juego")
ventana.iconbitmap("./img/atomo.ico")
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.config(bg="#222")
# Funciones
def mostrarCompuesto():
  global elementoObtenido
  infoElemento = escojerElemento()
  elementoObtenido = infoElemento
  elemento = infoElemento[0]
  probabilidad = infoElemento[4]
  porcentaje = calcularPosibilidad(probabilidad)
  lblPorcentaje.config(text=porcentaje)
  lblCompuesto.config(text="?")
  lblMensaje.config(text="")
  lblElemento.config(text=elemento)
  txtCompuesto.config(state="normal")
  txtCompuesto.delete(0,END)
  btnConfirmar.config(text="Comprobar",command=compararElemento)
def compararElemento():
  elementoUsuario = txtCompuesto.get()
  txtCompuesto.config(state="disabled")
  global elementoObtenido
  respuesta = validarElementos(elementoObtenido,elementoUsuario)
  informacion = respuesta.split("-")
  probabilidad = informacion[4]
  pasaSiguiente = informacion[3]
  lblCompuesto.config(text=informacion[1])
  if pasaSiguiente == "True":
    if probabilidad == "0":
      messagebox.showinfo("Felicidades","Ganaste el juego")
      exit()
    porcentaje = calcularPosibilidad(probabilidad)
    lblPorcentaje.config(text=porcentaje)
    lblMensaje.config(text="Correcto",fg="green")
    btnConfirmar.config(text="Siguiente",command=mostrarCompuesto)
  else:
    if probabilidad == "100":
      messagebox.showinfo("Lo sentimos","Has perdido el juego")
      exit()
    porcentaje = calcularPosibilidad(probabilidad)
    lblPorcentaje.config(text=porcentaje)
    lblMensaje.config(text="Incorrecto",fg="red")
    btnConfirmar.config(text="Siguiente",command=mostrarCompuesto)
# FRAMES
lbltitulo = Label(text="Memorize",bg="#222",fg="#fff",foreground="white",font=("Arial",32,),pady=10,).pack()
lblElemento = Label(text="",bg="#222",fg="#fff",font=("Arial",24),pady=24,padx=24,borderwidth=(4),relief="solid",highlightcolor="white",highlightthickness=1)
lblElemento.pack()
lblCompuesto = Label(text="?",bg="#222",fg="#fff",font=("Arial",24),pady=32,)
lblCompuesto.pack()
txtCompuesto = Entry(bg="#333",fg="White",font="Arial",highlightthickness=1,highlightcolor="White")
txtCompuesto.pack()
lblMensaje = Label(text="",pady=24,bg="#222")
lblMensaje.pack()
btnConfirmar = Button(text="Comprobar",command=compararElemento,pady=4,bg="#0af",fg="white",font=16)
btnConfirmar.pack()
lblPorcentaje = Label(text="",pady=12,bg="#222",fg="#0f0",font=("Arial", 24))
lblPorcentaje.pack()
mostrarCompuesto()
ventana.mainloop()