from tkinter import *
from juego import *

elementoObtenido = []

ventana = Tk()
ventana.title("Juego")
ventana.iconbitmap("atomo.ico")
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
  print(probabilidad)
  txtCompuesto.delete(0,END)
  lblCompuesto.config(text="?")
  lblMensaje.config(text="")
  lblElemento.config(text=elemento)
  btnConfirmar.config(text="Comprobar",command=compararElemento)
def compararElemento():
  elementoUsuario = txtCompuesto.get()
  global elementoObtenido
  print(elementoObtenido,elementoUsuario)
  respuesta = validarElementos(elementoObtenido,elementoUsuario)
  informacion = respuesta.split("-")
  print(informacion)
  probabilidad = informacion[4]
  pasaSiguiente = informacion[3]
  print(type(pasaSiguiente))
  lblCompuesto.config(text=informacion[1])
  if pasaSiguiente == "True":
    lblMensaje.config(text="Correcto",fg="green")
    btnConfirmar.config(text="Siguiente",command=mostrarCompuesto)
  else:
    lblMensaje.config(text="Incorrecto",fg="red")
    btnConfirmar.config(text="Siguiente",command=mostrarCompuesto)
  print(respuesta)
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
btnConfirmar = Button(text="Comprobar",command=compararElemento,pady=4,bg="#0af",fg="white")
btnConfirmar.pack()
lblPorcentaje = Label(text="",pady=12,bg="#222",fg="#0f0",font=("Arial", 24))
lblPorcentaje.pack()
mostrarCompuesto()
ventana.mainloop()