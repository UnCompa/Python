from random import *

elementos= ["H-Hidrogeno-1-1-1-50",
             "He-Helio-2-18-1-50",
             "Ne-Neòn-10-18-2-50",
             "Ar-Argòn-18-18-3-50",
             "Kr-Kriptòn-36-18-4-50",
             "Xe-Xenòn-54-18-5-50",
             "Rn-Radòn-86-18-6-50"]
def escojerElemento ():
    i = 0
    while i<1:
        global elementos
        shuffle(elementos)
        elemento=elementos.pop()
        infElemento=elemento.split("-")
        prob=randint(1,100)
        if prob < int(infElemento[5]):
            i=1 
            return infElemento
        else:
            elementos.append(elemento)
            
infElemento=escojerElemento()
print(infElemento [0])
respuesta =input("cual es el nombre del elemento:")
probalElemento=int(infElemento.pop())
if infElemento[1] == respuesta:
    if probalElemento >10:
        probalElemento = probalElemento-10
        infElemento.append(probalElemento)
    else:
        infElemento.append(probalElemento)
else:
    if probalElemento < 100:
        probalElemento = probalElemento+10
        infElemento.append(probalElemento)
    else:
        infElemento.append(probalElemento)
elemento= infElemento[0]+"-"+infElemento[1]+"-"+infElemento[2]+"-"+infElemento[3]+"-"+infElemento[4]+"-"+str(infElemento[5])
elementos.append(elemento)