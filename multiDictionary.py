import copy
from time import time

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        pass


    @staticmethod
    def searchwordlinear(lista, frase):
        parolenotfound=""
        parole=frase.split(" ")
        for parola in parole:
            trovata=False
            for i in lista:
                if parola==i:
                    trovata=True

                else:
                    pass
            if trovata==True:
                pass
            else:
                parolenotfound=parolenotfound+parola+"\n"
        return parolenotfound
    @staticmethod
    def searchworddicotomic(lista,frase):
        parole = frase.split(" ")
        notfound=""
        for parola in parole:
            copialista = copy.deepcopy(lista)
            found=False
            while found==False:
                confronto = []
                confronto.append(parola)
                if len(copialista) == 0:
                    notfound += parola + "\n"
                    break
                counte =( len(copialista)/2)
                counter=int(counte)
                lunghezzalista=len(copialista)
                confronto.append(copialista[counter])
                confronto.sort()
                if parola == copialista[counter]:
                    found=True
                    break
                if lunghezzalista==1:
                    notfound=notfound+parola+"\n"
                    found=True
                    break
                if confronto[0] == parola:
                    copialista = copialista[:counter]


                if confronto[1] == parola:
                    copialista = copialista[counter+1:]

        return notfound




















