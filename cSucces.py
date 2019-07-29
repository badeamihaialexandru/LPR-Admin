from tkinter import *
import tkinter as tk
from tkinter import ttk
import cAdminMenu
import cAdminMenu


class SuccesFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        print(parent)
        checkedImage=PhotoImage(file="GUIPhotos/039.png")
        labelChecked=tk.Label(self,image=checkedImage)
        labelChecked.place(relx=0.5,rely=0.3,anchor=CENTER)
        labelChecked.image=checkedImage

        #buton
        buttonImage = PhotoImage(file="GUIPhotos/038.png")
        logButton = Button(self, image=buttonImage,relief=RIDGE,
                           command=lambda:controller.show_frame(cAdminMenu.AdminFrame))
        logButton.place(rely=0.7, relx=0.5, anchor=CENTER, width="266", height='35')
        logButton.image=buttonImage

        labelWarning=tk.Label(self,text="")
        labelWarning.place(rely=0.9,relx=0.5,anchor=CENTER)