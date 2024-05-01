from random import *

elementos = [
    "H-Hidrogeno-1-False-50",
    "He-Helio-2-False-50",
    "Li-Litio-3-False-50",
    "Be-Berilio-4-False-50",
    "B-Boro-5-False-50",
    "C-Carbono-6-False-50",
    "N-Nitrogeno-7-False-50",
    "O-Oxigeno-8-False-50",
    "F-Fluor-9-False-50",
    "Ne-Neon-10-False-50",
    "Na-Sodio-11-False-50",
    "Mg-Magnesio-12-False-50",
    "Al-Aluminio-13-False-50",
    "Si-Silicio-14-False-50",
    "P-Fosforo-15-False-50",
    "S-Azufre-16-False-50",
    "Cl-Cloro-17-False-50",
    "Ar-Argon-18-False-50",
    "K-Potasio-19-False-50",
    "Ca-Calcio-20-False-50",
    "Sc-Scandio-21-False-50",
    "Ti-Titanio-22-False-50",
    "V-Vanadio-23-False-50",
    "Cr-Cromo-24-False-50",
    "Mn-Manganeso-25-False-50",
    "Fe-Hierro-26-False-50",
    "Co-Cobalto-27-False-50",
    "Ni-Niquel-28-False-50",
    "Cu-Cobre-29-False-50",
    "Zn-Zinc-30-False-50"
]

def todosElementos():
    return elementos
def escojerElemento ():
    i = 0
    while i<1:
        global elementos
        shuffle(elementos)
        elemento=elementos.pop()
        infElemento=elemento.split("-")
        prob=randint(1,100)
        if prob < int(infElemento[4]):
            i=1 
            return infElemento
        else:
            elementos.append(elemento)
            
def validarElementos(infElemento,respuesta):
    valorCorrecto = None
    print(infElemento)
    probalElemento=int(infElemento.pop())
    Elemento = str(infElemento[1])
    elementoLower = Elemento.lower()
    respuestaStr = str(respuesta)
    respuestaFinal = respuestaStr.lower()
    if elementoLower == respuestaFinal:
        if probalElemento >10:
            probalElemento = probalElemento-10
            infElemento.append(probalElemento)
            valorCorrecto = True
        else:
            infElemento.append(probalElemento)
            valorCorrecto = True
    else:
        if probalElemento < 100:
            probalElemento = probalElemento+10
            infElemento.append(probalElemento)
            valorCorrecto = False
        else:
            infElemento.append(probalElemento)
            valorCorrecto = False
    simbolo = infElemento[0] 
    nomElemento = infElemento[1] 
    numAtomico = infElemento[2] 
    probabilidad = str(infElemento[4]) 
    elemento = str(f"{simbolo}-{nomElemento}-{numAtomico}-{valorCorrecto}-{probabilidad}")
    print(elemento)
    elementos.append(elemento)
    return elemento

""" validarElementos("H-Hidrogeno-1-0","Hidrogeno") """
def calcularPosibilidad(posibilidad):
    cadena = ""
    posibilidad = int(posibilidad)
    if posibilidad == 50:
        cadena = f"----- {posibilidad}%"
    elif posibilidad == 40: 
        cadena = f"---- {posibilidad}%"
    elif posibilidad == 60: 
        cadena = f"------ {posibilidad}%"
    return cadena