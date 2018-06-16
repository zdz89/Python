import os
import glob

nazwaPliku = "lista.txt"
pulpit = os.path.join(os.environ["HOMEPATH"],"Desktop")
plik = os.path.join(pulpit,nazwaPliku)

lista_plikow = os.listdir(pulpit)

if nazwaPliku in lista_plikow:
    f = open(plik, "r")
    for linia in f.read().splitlines():
        print(linia)
    f.close()
else:
    f = open(plik, 'w+')
    f.close()

f = open(plik, "a")
kontynuowac = "t"
while (kontynuowac == "t"):
    nowaLinia = input("Dodaj nowego studenta: ")
    print(nowaLinia, file=f)
    kontynuowac = input("Kontynuować? (t/n): ")
f.close()
    

