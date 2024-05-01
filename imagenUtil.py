from PIL import Image, ImageTk
import os
#Cambiar PATH
directory = os.path.dirname(__file__)
PATH=f"{directory}\\img\\"


def obtenerImagen(nombre,ancho=300):
    imagen = Image.open(PATH+nombre)
    porcentaje = (ancho / float(imagen.size[0]))
    alto = int((float(imagen.size[1]) * float(porcentaje)))
    imagenModificada=imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    photoImg=ImageTk.PhotoImage(imagenModificada)
    return photoImg