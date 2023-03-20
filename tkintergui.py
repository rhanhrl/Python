#GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk as tk2
from tkinter.messagebox import showinfo

appgui = tk.Tk()
appgui.configure(bg="white")
appgui.geometry("300x200")
appgui.resizable(False, False)
appgui.title("Raihan Herlambang")

NAMA = tk.StringVar()

#frame input
inputframe = tk2.Frame(appgui)
#penempatan grid, pack, place
inputframe.pack(padx=10, pady=10, fill="x", expand=True)

#komponen

#label untuk nama
labelframe = tk2.Label(inputframe, text="Nama")
labelframe.pack(padx=10, pady=10, fill="x",expand= True)

#entry
entryframe = tk2.Entry(inputframe, textvariable=NAMA)
entryframe.pack(padx=10, fill="x", expand=True)

#tombol
def buttonfungsi():
    print(entryframe.get())
    showinfo(title="Warning", message="OKE")

buttonframe = tk2.Button(inputframe, text="EXIT", command=buttonfungsi)
buttonframe.pack(fill="x", expand=True, padx=10, pady=10)




appgui.mainloop()

