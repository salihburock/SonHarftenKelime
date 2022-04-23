from tkinter import *
import sys
from tkinter import ttk
import tkinter as tk
import random
from time import sleep
import os
import subprocess as sp
pd = ""
try:
    pd = sys.argv[1]
except:
    pass
od=0

if pd != "yo":
    giris_ekranı = tk.Tk()
    giris_ekranı.title("Son Harften Kelime Türetme")
    giris_ekranı.geometry("300x200")
    giris_ekranı.configure(bg="#ab6700")
    linklabel= tk.Label(text="")
    girislabeli = tk.Label(text="Son Harften Kelime Türetme Oyunu",bg="#ab6700",fg="#130675",font=("Comic Sans MS",12,"bold"))
    girislabeli.pack()
    kapatbutonu = tk.Button(text="    Çıkış    ",fg="red",command=exit,bg="black",pady=20)
    ileributonu = tk.Button(text="Oyuna Başla",fg="lime",command=giris_ekranı.destroy,bg="black",pady=20)
    kapatbutonu.pack(side="left")
    ileributonu.pack(side="right")
    giris_ekranı.resizable(0,0)
    giris_ekranı.iconbitmap("icon.ico")
    giris_ekranı.protocol("WM_DELETE_WINDOW",exit)
    giris_ekranı.mainloop()

kelimeler = []
for kelime in open("liste1.txt","r+",encoding="utf-8").read().split("\n"):
    kelimeler.append(kelime.split(' ')[0])
def yeniden_oyna():
    sp.run("baslat.bat")
    root.quit()    
bilgisayar_kelimesi = random.choice(kelimeler)
def oyun_bitti(skor,durum=bool):
    global od
    od=1
    if durum:
        oyunbittimesajılabeli.config(text=f"""
        OYUN BİTTİ
        SEN KAZANDIN
        skor:{skor}
        """)
        

    if not durum:
        skor -= 1
        oyunbittimesajılabeli.config(text=f"""
        OYUN BİTTİ
        SEN KAYBETTİN
        skor:{skor}
        """)
    donat.config(text="")
    gönder_buton.config(state="disabled")
    yenidenoynalabeli.place(x=318,y=70)
    yenidenoynabutonu.place(x=390,y=90)
    yenidenoynayıiptalbutonu.place(x=309,y=90)

kullanılan_kelimeler = []
mümkün_kelimeler = []
skor = 0
root = Tk()
root.title("Son Harften Kelime Türetme")
root.geometry("721x400")
root.resizable(0, 0)
root.iconbitmap("icon.ico")


def bilgisayarın_kelime_bulması(kelime):
    global skor, mümkün_kelimeler, bilgisayar_kelimesi, od
    kullanılan_kelimeler.append(kelime)
    for mkelime in kelimeler:
        if mkelime.startswith(kelime[-1]) and kullanılan_kelimeler.count(mkelime) == 0:
            mümkün_kelimeler.append(mkelime)
    bilgisayar_kelimesi = random.choice(mümkün_kelimeler)
    donat.config(text=bilgisayar_kelimesi)
    
    noidea.config(font=("Arial",15),pady=3,padx=4,text=f"{bilgisayar_kelimesi[-1]} ile başlayan bir kelime giriniz: ")
    kullanılan_kelimeler.append(bilgisayar_kelimesi)

def bizim_kelime_göndermemiz():

    global bilgisayar_kelimesi,skor,mümkün_kelimeler, od
    kullanıcıKelimesi = giris_entry.get()
    skor += 1
    donat.config(text=bilgisayar_kelimesi)
    kullanılan_kelimeler.append(bilgisayar_kelimesi)
    
    if kelimeler.count(kullanıcıKelimesi) == 0:
        hatamesajılabeli.config(text=f'{hatamesajılabeli.cget("text")}\n{kullanıcıKelimesi}, diye bir kelime bulunamadı!')
        oyun_bitti(skor,0)
        od=1
    if not kullanıcıKelimesi.startswith(bilgisayar_kelimesi[-1]):
        hatamesajılabeli.config(text=f'{hatamesajılabeli.cget("text")}\n{bilgisayar_kelimesi[-1]} ile başlayan bir kelime bulmanız gerekiyordu!')
        oyun_bitti(skor,0)
        od=1
    if bilgisayar_kelimesi.endswith("ğ"):
        hatamesajılabeli.config(text="Bilgisayar ğ ile biten kelime buldu!")
        oyun_bitti(skor,0)
        od=1
    if kullanılan_kelimeler.count(kullanıcıKelimesi) > 0:
        hatamesajılabeli.config(text=f'{hatamesajılabeli.gcet("text")}\n{kullanıcıKelimesi}, "kelimesi kullanıldı!"\n')
        oyun_bitti(skor,0)
        od=1
    if kullanıcıKelimesi.endswith("ğ") and not od:
        oyun_bitti(skor,1)
        od=1
    mümkün_kelimeler = []
    donat.config(text="")
    skorlabel.config(text=f"Skor: {skor-1}")

    bilgisayarın_kelime_bulması(kelime=kullanıcıKelimesi)
    if od:
        donat.config(text="")
    giris_entry.delete(0,END)
    
kullanıcı_giriş_paneli = ttk.Entry()
noidea = tk.Label(font=("Arial",15),pady=3,padx=4,text=f"{bilgisayar_kelimesi[-1]} ile başlayan bir kelime giriniz: ")
noidea.pack(side="top")
skorlabel = tk.Label(text="Skor:",fg="lightblue")
skorlabel.place(x=339,y=50)
giris_entry = tk.Entry(fg="#fff",bg="black")
giris_entry.pack(side="top")
çıkış_butonu = tk.Button(text="       Çıkış       ",command=exit,bg="gray",fg="red")
çıkış_butonu.pack(side="left",ipadx=20,ipady=10)
gönder_buton = tk.Button(text="Kelimeyi gönder", fg="lime",bg="gray",command=bizim_kelime_göndermemiz)
gönder_buton.pack(side="right",ipadx=20,ipady=10)
donat = tk.Label(text=bilgisayar_kelimesi,fg="darkblue",font=("Arial",20,"bold"))
donat.pack(side="top",pady=30)
oyunbittimesajılabeli = tk.Label(text = "",fg="#9c5106")
oyunbittimesajılabeli.pack(side="bottom")
yenidenoynalabeli = tk.Label(text="Yeniden oyna ?",fg="darkgreen")
yenidenoynabutonu = tk.Button(text="✔",bg="green",command=yeniden_oyna)
yenidenoynayıiptalbutonu = tk.Button(text="✖",bg="red",command=exit)
hatamesajılabeli = tk.Label(fg="red",text="")
hatamesajılabeli.pack(side="bottom")
giris_entry.focus()
root.attributes("-topmost", True)

root.mainloop()
