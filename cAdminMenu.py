from tkinter import *
import tkinter as tk
from tkinter import ttk
import cAddPersoana
import cAddAdmin
import cRmAdmin
import cRmMasina

class AdminFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        backgroundImage=PhotoImage(file="GUIPhotos/058.png")
        backgroundLabel = ttk.Label(self,image=backgroundImage)
        backgroundLabel.place(x=0,y=0)
        backgroundLabel.image=backgroundImage

        #buton adaugare admin
        photoAddAdmin=PhotoImage(file="GUIPhotos/051.png")
        butonAddAdmin=tk.Button(backgroundLabel,image=photoAddAdmin,
                                command=lambda: controller.show_frame(cAddAdmin.AddAdminFrame))
        butonAddAdmin.place(x=100,y=145,width=300,height=40)
        butonAddAdmin.image = photoAddAdmin

        # buton sterge admin
        photoRemoveAdmin = PhotoImage(file="GUIPhotos/050.png")
        butonRemoveAdmin = tk.Button(backgroundLabel, image=photoRemoveAdmin,
                                     command=lambda: controller.show_frame(cRmAdmin.RemoveAdminFrame))
        butonRemoveAdmin.place(x = 100, y = 215, width = 300, height = 40)
        butonRemoveAdmin.image = photoRemoveAdmin

        #buton adaugare masina
        photoAddMasina=PhotoImage(file="GUIPhotos/049.png")
        butonAddMasina=tk.Button(backgroundLabel,image=photoAddMasina,
                                   command=lambda: controller.show_frame(cAddPersoana.AddPersoanaFrame))
        butonAddMasina.place(x=100, y=345, width=300, height=40)
        butonAddMasina.image=photoAddMasina



        # buton sterge masina
        photoRemoveMasina=PhotoImage(file="GUIPhotos/048.png")
        butonRmMasina = tk.Button(backgroundLabel,image=photoRemoveMasina,
                                   command=lambda: controller.show_frame(cRmMasina.RemoveMasinaFrame))
        butonRmMasina.place(x=100, y=415, width=300, height=40)
        butonRmMasina.image=photoRemoveMasina

