from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Son Harften Kelime Türetme")

def kelime_gonder():
    pass
    donut.set("Po")
def kelime_bul(kelime):
    pass

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
