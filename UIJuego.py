from tkinter import *

ventana = Tk()
ventana.title("Juego")
ventana.iconbitmap("atomo.ico")
ventana.geometry("500x500")
ventana.resizable(0,0)
ventana.config(bg="#222")
# FRAMES
frameJuego = Frame(ventana, bg="#323232")
lbltitulo = Label(text="Juego",bg="#222",fg="#fff",font=("Arial",32),pady=10,)
lbltitulo.pack()
ventana.mainloop()