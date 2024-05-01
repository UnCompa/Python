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
    "Zn-Zinc-30-False-50",
    "Ga-Galio-31-False-50",
    "Ge-Germanio-32-False-50",
    "As-Arsenico-33-False-50",
    "Se-Selenio-34-False-50",
    "Br-Bromo-35-False-50",
    "Kr-Kripton-36-False-50",
    "Rb-Rubidio-37-False-50",
    "Sr-Estroncio-38-False-50",
    "Y-Ytrio-39-False-50",
    "Zr-Zirconio-40-False-50",
    "Nb-Niobio-41-False-50",
    "Mo-Molibdeno-42-False-50",
    "Tc-Tecnecio-43-False-50",
    "Ru-Rutenio-44-False-50",
    "Rh-Rodio-45-False-50",
    "Pd-Paladio-46-False-50",
    "Ag-Plata-47-False-50",
    "Cd-Cadmio-48-False-50",
    "In-Indio-49-False-50",
    "Sn-Estano-50-False-50",
    "Sb-Antimonio-51-False-50",
    "Te-Telurio-52-False-50",
    "I-Yodo-53-False-50",
    "Xe-Xenon-54-False-50",
    "Cs-Cesio-55-False-50",
    "Ba-Bario-56-False-50",
    "La-Lantano-57-False-50",
    "Ce-Cerio-58-False-50",
    "Pr-Praseodimio-59-False-50",
    "Nd-Neodimio-60-False-50",
    "Pm-Prometio-61-False-50",
    "Sm-Esamio-62-False-50",
    "Eu-Europio-63-False-50",
    "Gd-Gadolinio-64-False-50",
    "Tb-Terbio-65-False-50",
    "Dy-Disprosio-66-False-50",
    "Ho-Holmio-67-False-50",
    "Er-Erbio-68-False-50",
    "Tm-Tulio-69-False-50",
    "Yb-Yterbio-70-False-50",
    "Lu-Lutecio-71-False-50",
    "Hf-Hafnio-72-False-50",
    "Ta-Tantalio-73-False-50",
    "W-Wolframio-74-False-50",
    "Re-Renio-75-False-50",
    "Os-Osmio-76-False-50",
    "Ir-Iridio-77-False-50",
    "Pt-Platino-78-False-50",
    "Au-Oro-79-False-50",
    "Hg-Mercurio-80-False-50",
    "Tl-Talio-81-False-50",
    "Pb-Plomo-82-False-50",
    "Bi-Bismuto-83-False-50",
    "Po-Polonio-84-False-50",
    "At-Astato-85-False-50",
    "Rn-Radon-86-False-50",
    "Fr-Francio-87-False-50",
    "Ra-Radio-88-False-50",
    "Ac-Actinio-89-False-50",
    "Th-Torio-90-False-50",
    "Pa-Protactinio-91-False-50",
    "U-Uranio-92-False-50",
    "Np-Neptunio-93-False-50",
    "Pu-Plutonio-94-False-50",
    "Am-Americio-95-False-50",
    "Cm-Curio-96-False-50",
    "Bk-Berkelio-97-False-50",
    "Cf-Californio-98-False-50",
    "Es-Einstenio-99-False-50",
    "Fm-Fermio-100-False-50",
    "Md-Mendelevio-101-False-50",
    "No-Nobelio-102-False-50",
    "Lr-Lawrencio-103-False-50",
    "Rf-Rutherfordio-104-False-50",
    "Db-Dubnio-105-False-50",
    "Sg-Seaborgio-106-False-50",
    "Bh-Bohrio-107-False-50",
    "Hs-Hassio-108-False-50",
    "Mt-Meitnerio-109-False-50",
    "Ds-Darmstadtio-110-False-50",
    "Rg-Roentgenio-111-False-50",
    "Cn-Copernicio-112-False-50",
    "Nh-Nihonio-113-False-50",
    "Fl-Flerovio-114-False-50",
    "Mc-Moscovio-115-False-50",
    "Lv-Livermorio-116-False-50",
    "Ts-Tenesino-117-False-50",
    "Og-Oganeson-118-False-50"
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
    (infElemento)
    probalElemento=int(infElemento.pop())
    Elemento = str(infElemento[1])
    elementoLower = Elemento.lower()
    respuestaStr = str(respuesta)
    respuestaFinal = respuestaStr.lower()
    if elementoLower == respuestaFinal:
        if probalElemento > 0:
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
    (elemento)
    elementos.append(elemento)
    return elemento

""" validarElementos("H-Hidrogeno-1-0","Hidrogeno") """
def calcularPosibilidad(posibilidad):
    cadena = ""
    posibilidad = int(posibilidad)
    if posibilidad == 0:
        cadena = f"{posibilidad}%"
    elif posibilidad == 10: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 20: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 30: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 40: 
        cadena = f"{posibilidad}%"
    if posibilidad == 50:
        cadena = f"{posibilidad}%"
    elif posibilidad == 60: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 70: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 80: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 90: 
        cadena = f"{posibilidad}%"
    elif posibilidad == 100: 
        cadena = f"{posibilidad}%"
    return cadena