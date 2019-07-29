from tkinter import *
import tkinter as tk
from tkinter import ttk
import cAdminMenu
import cLPRDataBase
from PIL import Image, ImageTk


class LoginFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        mydb=cLPRDataBase.myDataBase()

        def verificaDate():
            if entryNume.get()=="":
                if entryPass.get()=="":
                    entryPass.config(highlightbackground="red", highlightthickness=1)
                entryNume.config(highlightbackground="red", highlightthickness=1)
                labelWarningUser.config(text="Trebuie sa intorduceti un nume!",fg="red",font="TimesNewRoman 10 bold")
                labelWarningPass.config(text="Trebuie sa introduceti o parola!", fg="red", font="TimesNewRoman 10 bold")
            else:
                entryNume.config( highlightthickness=0)
                labelWarningUser.config(text="")
                if entryPass.get()=="":
                    entryPass.config(highlightbackground="red", highlightthickness=1)
                    labelWarningPass.config(text="Trebuie sa introduceti o parola!",fg="red",font="TimesNewRoman 10 bold")
                else:
                        labelWarningUser.config(text="")
                        labelWarningPass.config(text="")
                        if mydb.loginUser(entryNume.get(),entryPass.get()):
                            controller.show_frame(cAdminMenu.AdminFrame)

                        entryPass.config(highlightbackground="red", highlightthickness=1)
                        entryNume.config(highlightbackground="red", highlightthickness=1)
                        labelWarning=tk.Label(self, text="Username sau parola gresite!",
                                              font="TimesNewRoman 10 bold",fg="red")
                        labelWarning.place(relx=0.5,rely=0.65,anchor=CENTER)


        backgorundImage=PhotoImage(file="GUIPhotos/056.png")
        label = ttk.Label(self,image=backgorundImage)
        label.place(x=0,y=0)
        label.image=backgorundImage

        # username
        userImage = PhotoImage(file="GUIPhotos/055.png")
        labelNume = Label(label, image=userImage)
        labelNume.place(relx=0.3, rely=0.4, anchor=CENTER, width=250, height=40)
        labelNume.image=userImage

        entryNume = Entry(label)
        entryNume.place(relx=0.75, rely=0.4, anchor=CENTER, relwidth="0.4", relheight='0.04')
        labelWarningUser = tk.Label(label, text="")
        labelWarningUser.place(relx=0.55,rely=0.425,  anchor=NW)

        # password
        passwordImage = PhotoImage(file="GUIPhotos/053.png")
        labelPass = Label(label, image=passwordImage)
        labelPass.place(relx=0.3, rely=0.52, anchor=CENTER, width=250, height=40)
        labelPass.image=passwordImage

        entryPass = Entry(label,show="*")
        entryPass.place(relx=0.75, rely=0.52, anchor=CENTER, relwidth="0.4", relheight='0.04')
        labelWarningPass = tk.Label(label, text="")
        labelWarningPass.place( relx=0.55,rely=0.545, anchor=NW)

        #buton
        buttonImage = PhotoImage(file="GUIPhotos/031.png")
        logButton = Button(label, image=buttonImage,relief=RIDGE,
                           command=lambda: verificaDate())
        logButton.place(rely=0.8, relx=0.5, anchor=CENTER, width="266", height='35')
        logButton.image=buttonImage

