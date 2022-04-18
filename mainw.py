import os
from tkinter import *
from tkinter import ttk
import numpy as np
import random
import sys
skor = 0
root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Son Harften Kelime Türetme Oyunu\n").grid(column=0, row=0)


ttk.Label(frm, text="\nKelime Giriniz:").grid(column=4, row=5)


def cikis():
    print("Cıkış yapılıyor...")
    sys.exit()

ttk.Button(frm, text="Cıkış", command=cikis).grid(column=5, row=1)

dönütler = []
kelimeler = []

def oyun_bitti():
    print(f"""
OYUN BİTTİ    
SKOR:{skor}
    """)
kullanılan_kelimeler = []

for kelime in open('full.txt','r+',encoding='utf8').read().split('\n'):
    kelimeler.append(kelime.split(' ')[0])
while True:
    mümkün_kelimeler = []

    ilkkelime = input('Kelime giriniz:').lower()
    sonharf = ilkkelime[-1]
    if kelimeler.count(ilkkelime.lower()) == 0:
        print(ilkkelime, 'diye bir kelime bulunamadı')
        oyun_bitti()
        exit()
    if ilkkelime.endswith('ğ'):
        print('Sen kazandın!')
        oyun_bitti()
        exit()
    for kelime in kelimeler:
        if kelime.startswith(sonharf) and kullanılan_kelimeler.count(kelime) == 0:
            mümkün_kelimeler.append(kelime)

    dönüt = np.random.choice(mümkün_kelimeler)
    try:
        global stop
        if not ilkkelime.startswith(dönütler[-1][-1]):
            print(f'{dönütler[-1][-1]} harfi ile başlayan bir kelime bulmanız gerekiyordu')
            oyun_bitti()
            os.system('exit')
            os.system('taskkill /f /im python.exe')
    except:
        pass

    if kullanılan_kelimeler.count(ilkkelime) != 0:
        print('Bu kelime kullanıldı!')
        kullanılan_kelimeler.append(dönüt)
        kullanılan_kelimeler.append(ilkkelime)
        skor += 1
        print(dönütler[-1])

    else:
        print(dönüt)
        kullanılan_kelimeler.append(dönüt)
        kullanılan_kelimeler.append(ilkkelime)
        skor += 1

    dönütler.append(dönüt)
    root.mainloop()
