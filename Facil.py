from tkinter import messagebox
from tkinter import *
from juegoFacil import *
import os
elementoObtenido = []
estadoBoton = "Comprobar"
ventana = Tk()
ventana.title("Memoria Atómica")
directory = os.path.dirname(__file__)
ventana.iconbitmap(f"{directory}/img/atomo.ico")
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
  global estadoBoton
  estadoBoton = "Comprobar"
  btnConfirmar.config(text="Comprobar",command=compararElemento)
def compararElemento():
  global estadoBoton
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
    estadoBoton = "Pasa"
    btnConfirmar.config(text="Siguiente",command=mostrarCompuesto)
  else:
    if probabilidad == "100":
      messagebox.showinfo("Lo sentimos","Has perdido el juego")
      exit()
    porcentaje = calcularPosibilidad(probabilidad)
    lblPorcentaje.config(text=porcentaje)
    lblMensaje.config(text="Incorrecto",fg="red")
    estadoBoton = "Pasa"
    btnConfirmar.config(text="Siguiente",command=mostrarCompuesto)
# FRAMES
lbltitulo = Label(text="Memoria Atómica",bg="#222",fg="#10b981",foreground="#10b981",font=("Helvetica",24),pady=16).pack()
lblElemento = Label(text="",bg="#222",fg="#fff",font=("Helvetica",24),pady=24,padx=24,borderwidth=(4),relief="flat",highlightthickness=3,highlightcolor="#0af",highlightbackground="#0af")
lblElemento.pack()
lblCompuesto = Label(text="?",bg="#222",fg="#fff",font=("Helvetica",24),pady=32,)
lblCompuesto.pack()
txtCompuesto = Entry(bg="#333",fg="White",font="Helvetica",highlightthickness=1,highlightcolor="#0af",insertbackground="white",highlightbackground="blue",relief="flat",disabledbackground="#121212")
txtCompuesto.pack()
lblMensaje = Label(text="",pady=24,bg="#222",font=("Helvetica",12))
lblMensaje.pack()
btnConfirmar = Button(text="Comprobar",command=compararElemento,pady=4,bg="#0af",fg="black",font=16)
btnConfirmar.pack()
lblPorcentaje = Label(text="",pady=12,bg="#222",fg="#aaa",font=("Helvetica", 16))
lblPorcentaje.pack()
def comprobar_enter(eent):
    global estadoBoton
    if estadoBoton == "Comprobar":
      compararElemento()
    elif estadoBoton == "Pasa": 
      mostrarCompuesto()
ventana.bind("<Return>", comprobar_enter)
mostrarCompuesto()
ventana.mainloop()