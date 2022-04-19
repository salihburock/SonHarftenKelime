from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Son Harften Kelime Türetme")

def kelime_gonder():
    kelime = kelime_bul(giris.get())
    donut.set(kelime_bul(kelime))
def kelime_bul(kelime):
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
    return dönüt


mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

giris = StringVar()
giris_entry = ttk.Entry(mainframe, width=7, textvariable=giris)
giris_entry.grid(column=2, row=1, sticky=(W, E))



donut = StringVar()
ttk.Label(mainframe, textvariable=donut).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Cıkış", command=exit).grid(column=1, row=3, sticky=W)

ttk.Button(mainframe, text="Gönder", command=kelime_gonder).grid(column=3, row=3)

ttk.Label(mainframe, text="Kelime giriniz:").grid(column=1, row=1, sticky=W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

giris_entry.focus()
root.bind("<Return>", exit)

root.mainloop()
