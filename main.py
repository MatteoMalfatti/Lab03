from time import time

import multiDictionary
import spellchecker

sc = spellchecker.SpellChecker()


while(True):
    sc.printMenu()

    numeromenu=input("Scegli la lingua:")


    if int(numeromenu)== 1:
        listaita =[]
        with open("Italian.txt", "r", encoding="utf-8") as file:
            contenuto = file.read()
            parole = contenuto.split("\n")
            for i in parole:
                listaita.append(i)
        parolescorrette=""

        print("Inserisci la tua frase in Italiano\n")
        fraseit = input()
        fraseita=fraseit.lower()
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            fraseita = fraseita.replace(c, "")
        paroledaverificare=fraseita.split(" ")
        print(f"metodo con contains")
        for parola in paroledaverificare:
            if listaita.__contains__(parola):
                pass
            else:
                parolescorrette=parolescorrette+parola+"\n"
        print(parolescorrette)
        print(time())
        print(f"="*60)
        print(f"metodo con ricerca lineare")
        risultatolineare = multiDictionary.MultiDictionary.searchwordlinear(listaita, fraseita)
        print(risultatolineare)
        print(time())
        print(f"=" * 60)
        print(f"metodo con ricerca dicotomica")
        risultatodicotomico=multiDictionary.MultiDictionary.searchworddicotomic(listaita,fraseita)
        print(risultatodicotomico)
        print(time())
        break

    if int(numeromenu) == 2:
        listaingl= []
        with open("English.txt", "r", encoding="utf-8") as file:
            contenuto = file.read()
            parole = contenuto.split("\n")
            for i in parole:
                listaingl.append(i)
        parolescorrette = ""

        print("Inserisci la tua frase in Inglese\n")
        fraseingle = input()
        fraseinglese=fraseingle.lower()
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            fraseinglese = fraseinglese.replace(c, "")
        paroledaverificare = fraseinglese.split(" ")
        print(f"metodo con contains")
        for parola in paroledaverificare:
            if listaingl.__contains__(parola):
                pass
            else:
                parolescorrette = parolescorrette + parola + "\n"
        print(parolescorrette)
        print(time())
        print(f"=" * 60)
        print(f"metodo con ricerca lineare")
        risultatolineare= multiDictionary.MultiDictionary.searchwordlinear(listaingl, fraseinglese)
        print(risultatolineare)
        print(time())
        print(f"=" * 60)
        print(f"metodo con ricerca dicotomica")
        risultatodicotomico = multiDictionary.MultiDictionary.searchworddicotomic(listaingl, fraseinglese)
        print(risultatodicotomico)
        print(time())
        break
    if int(numeromenu) == 3:
        listaspagnolo = []
        with open("Spanish.txt", "r", encoding="utf-8") as file:
            contenuto = file.read()
            parole = contenuto.split("\n")
            for i in parole:
                listaspagnolo.append(i)
        parolescorrette = ""

        print("Inserisci la tua frase in Spagnolo\n")
        frasespa = input()
        frasespagnolo=frasespa.lower()
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            frasespagnolo = frasespagnolo.replace(c, "")
        paroledaverificare = frasespagnolo.split(" ")
        print(f"metodo con contains")
        for parola in paroledaverificare:
            if listaspagnolo.__contains__(parola):
                pass
            else:
                parolescorrette = parolescorrette + parola + "\n"
        print(parolescorrette)
        print(time())
        print(f"=" * 60)
        print(f"metodo con ricerca lineare")
        risultatolineare = multiDictionary.MultiDictionary.searchwordlinear(listaspagnolo, frasespagnolo)
        print(risultatolineare)
        print(time())
        print(f"=" * 60)
        print(f"metodo con ricerca dicotomica")
        risultatodicotomico = multiDictionary.MultiDictionary.searchworddicotomic(listaspagnolo, frasespagnolo)
        print(risultatodicotomico)
        print(time())
        break

    if int(numeromenu) == 4:
        break


