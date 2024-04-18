from tkinter import *
from juego import *
ventana = Tk()
ventana.title("Juego")
ventana.iconbitmap("atomo.ico")
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.config(bg="#222")
# Funciones
def mostrarCompuesto():
  infoElemento = escojerElemento()
  elemento = infoElemento[0]
  print(elemento)
  lblElemento.config(text=elemento)
# FRAMES
frameJuego = Frame(ventana, bg="#323232")
lbltitulo = Label(text="Memorize",bg="#222",fg="#fff",foreground="white",font=("Arial",32),pady=10,).pack()
lblElemento = Label(text="",bg="#222",fg="#fff",font=("Arial",24),pady=24,padx=24,borderwidth=(4),relief="solid",highlightcolor="white",highlightthickness=1)
lblElemento.pack()
lblCompuesto = Label(text="Hidrogeno",bg="#222",fg="#fff",font=("Arial",24),pady=32,).pack()
txtCompuesto = Entry(bg="#333",fg="White",font="Arial",highlightthickness=1,highlightcolor="White").pack()
btnConfirmar = Button(text="Comprobar",command=mostrarCompuesto).pack()
ventana.mainloop()