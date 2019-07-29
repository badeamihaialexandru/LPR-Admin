from tkinter import *
import tkinter as tk
import cLPRDataBase
import cAdminMenu
from tkinter import ttk
import cSucces
from PIL import Image, ImageTk


class AddAdminFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        def addUser():
            mydb=cLPRDataBase.myDataBase()
            if entryNume.get()=="":
                entryNume.config(highlightbackground="red", highlightthickness=1)
                labelUserWarning.config(text="Introduceti un username!")
                if entryPass.get()=="":
                    entryPass.config(highlightbackground="red", highlightthickness=1)
                    labelPassWarning.config(text="Introduceti o parola!")
                    if reEntryPass.get()=="":
                        reEntryPass.config(highlightbackground="red", highlightthickness=1)
                        labelRePassWarning.config(text="Reintroduceti parola!")

            else:
                if mydb.checkUserExists(entryNume.get()):
                    entryNume.config(highlightbackground="red", highlightthickness=1)
                    labelUserWarning.config(text="Acest nume exista deja!", fg="red")
                else:
                    if entryPass.get()=="":
                        entryPass.config(highlightbackground="red", highlightthickness=1)
                        labelPassWarning.config(text="Introduceti o parola!")
                        if reEntryPass.get()=="":
                            reEntryPass.config(highlightbackground="red", highlightthickness=1)
                            labelRePassWarning.config(text="Reintroduceti parola!", fg="red")
                    else:
                        if reEntryPass.get()=="":
                            reEntryPass.config(highlightbackground="red", highlightthickness=1)
                            labelRePassWarning.config(text="Trebuie sa reintroduceti parola!", fg="red")
                        else:
                            if entryPass.get()!=reEntryPass.get():
                                entryPass.config(highlightbackground="red", highlightthickness=1)
                                reEntryPass.config(highlightbackground="red", highlightthickness=1)
                                labelRePassWarning.config(text="Parolele trebuie sa fie identice!", fg="red")
                            else:
                                mydb.addUser(entryNume.get(),entryPass.get())
                                entryPass.config(highlightthickness=0)
                                entryNume.config(highlightthickness=0)
                                reEntryPass.config(highlightthickness=0)
                                entryPass.delete(0, END)
                                entryNume.delete(0, END)
                                reEntryPass.delete(0, END)
                                labelUserWarning.config(text="")
                                labelPassWarning.config(text="")
                                labelRePassWarning.config(text="")
                                controller.show_frame(cSucces.SuccesFrame)

        def goBack():
            controller.show_frame(cAdminMenu.AdminFrame)
            entryPass.config(highlightthickness=0)
            entryNume.config(highlightthickness=0)
            reEntryPass.config(highlightthickness=0)
            entryPass.delete(0,END)
            entryNume.delete(0,END)
            reEntryPass.delete(0,END)
            labelUserWarning.config(text="")
            labelPassWarning.config(text="")
            labelRePassWarning.config(text="")

        backgroundImage=PhotoImage(file="GUIPhotos/059.png")
        labelBackground=Label(self,image=backgroundImage)
        labelBackground.place(x=0,y=0)
        labelBackground.image=backgroundImage


        # username
        userImage = PhotoImage(file="GUIPhotos/055.png")
        labelNume = Label(self, image=userImage)
        labelNume.place(x=30, y=220, width=250, height=40)
        labelNume.image = userImage

        entryNume = Entry(self)
        entryNume.place(x=290, y=230, width=180, height=24)

        labelUserWarning = Label(self, text="",font="TimesNewRoman 10 bold",fg="red")
        labelUserWarning.place(x=290, y=256)

        # password
        passwordImage = PhotoImage(file="GUIPhotos/053.png")
        labelPass = Label(self, image=passwordImage)
        labelPass.place(x=30, y=280, width=250,height=40)
        labelPass.image = passwordImage

        entryPass = Entry(self,show="*")
        entryPass.place(x=290, y=290,width=180, height=24)

        labelPassWarning=Label(self,text="",font="TimesNewRoman 10 bold",fg="red")
        labelPassWarning.place(x=290,y=316)

        # repeat password
        rePasswordImage = PhotoImage(file="GUIPhotos/054.png")
        reLabelPass = Label(self, image=rePasswordImage)
        reLabelPass.place(x=30, y=340, width=250, height=40)
        reLabelPass.image = rePasswordImage

        reEntryPass = Entry(self,show="*")
        reEntryPass.place(x=290, y=350, width=180, height=24)

        labelRePassWarning = Label(self, text="",font="TimesNewRoman 10 bold",fg="red")
        labelRePassWarning.place(x=290, y=376)


        # buton adauga admin
        addAdminImage = PhotoImage(file="GUIPhotos/037.png")
        addAdminButton = Button(self, image=addAdminImage, relief=RIDGE,command=lambda: addUser())
        addAdminButton.place(y=460, x=100, width="266", height='35')
        addAdminButton.image = addAdminImage

        #buton inapoi
        backImage = PhotoImage(file="GUIPhotos/036.png")
        backButton = Button(self, image=backImage, relief=RIDGE, command=lambda: goBack())
        backButton.place(y=520, x=100, width="266", height='35')
        backButton.image = backImage
