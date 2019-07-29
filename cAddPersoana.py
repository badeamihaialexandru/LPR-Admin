from tkinter import *
import tkinter as tk
import cLPRDataBase
import cAdminMenu
from tkinter import ttk
import cSucces
from PIL import Image, ImageTk


class AddPersoanaFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        def addMasina():
            goOn=True
            if numeEntry.get() is "":
                numeEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningNume.config(text="Introduceti nume!")
                goOn=False
            else:
                labelWarningNume.config(text="")
                numeEntry.config(highlightthickness=0)
            if prenumeEntry.get() is "":
                prenumeEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningPrenume.config(text="Introduceti prenume!")
                goOn = False
            else:
                labelWarningPrenume.config(text="")
                prenumeEntry.config(highlightthickness=0)
            if functieEntry.get() is "":
                functieEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningFunctie.config(text="Introduceti functie!")
                goOn = False
            else:
                labelWarningFunctie.config(text="")
                functieEntry.config(highlightthickness=0)
            if modelEntry.get() is "":
                modelEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningModel.config(text="Introduceti model!")
                goOn = False
            else:
                labelWarningModel.config(text="")
                modelEntry.config(highlightthickness=0)
            if marcaEntry.get() is "":
                marcaEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningMarca.config(text="Introduceti producator!")
                goOn = False
            else:
                labelWarningMarca.config(text="")
                marcaEntry.config(highlightthickness=0)
            if culoareEntry.get() is "":
                culoareEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningCuloare.config(text="Introduceti culoare!")
                goOn = False
            else:
                labelWarningCuloare.config(text="")
                culoareEntry.config(highlightthickness=0)
            if numarEntry.get() is "":
                numarEntry.config(highlightbackground="red", highlightthickness=1)
                labelWarningNumar.config(text="Introduceti numar!")
                goOn = False
            else:
                labelWarningNumar.config(text="")
                numarEntry.config(highlightthickness=0)

            if goOn is True:
                mydb=cLPRDataBase.myDataBase()
                ans=mydb.addNumar(numarEntry.get(),culoareEntry.get(),modelEntry.get(),marcaEntry.get(),
                              numeEntry.get(),prenumeEntry.get(),functieEntry.get())
                if ans==1:
                    numeEntry.config(highlightthickness=0)
                    prenumeEntry.config(highlightthickness=0)
                    functieEntry.config(highlightthickness=0)
                    modelEntry.config(highlightthickness=0)
                    marcaEntry.config(highlightthickness=0)
                    culoareEntry.config(highlightthickness=0)
                    numarEntry.config(highlightthickness=0)
                    numeEntry.delete(0,END)
                    prenumeEntry.delete(0,END)
                    functieEntry.delete(0,END)
                    modelEntry.delete(0,END)
                    marcaEntry.delete(0,END)
                    culoareEntry.delete(0,END)
                    numarEntry.delete(0,END)


                    controller.show_frame(cSucces.SuccesFrame)
                else:
                    numarEntry.config(highlightbackground="red", highlightthickness=1)
                    labelWarningNumar.config(text="Numarul exista deja!",fg="red")



        def goBack():
            numeEntry.config(highlightthickness=0, text="")
            prenumeEntry.config(highlightthickness=0, text="")
            functieEntry.config(highlightthickness=0, text="")
            modelEntry.config(highlightthickness=0, text="")
            marcaEntry.config(highlightthickness=0, text="")
            culoareEntry.config(highlightthickness=0, text="")
            numarEntry.config(highlightthickness=0, text="")

            numeEntry.delete(0, END)
            prenumeEntry.delete(0, END)
            functieEntry.delete(0, END)
            modelEntry.delete(0, END)
            marcaEntry.delete(0, END)
            culoareEntry.delete(0, END)
            numarEntry.delete(0, END)

            labelWarningNume.config(text="")
            labelWarningPrenume.config(text="")
            labelWarningFunctie.config(text="")
            labelWarningMarca.config(text="")
            labelWarningModel.config(text="")
            labelWarningCuloare.config(text="")
            labelWarningNumar.config(text="")

            controller.show_frame(cAdminMenu.AdminFrame)

        backgroundImage=PhotoImage(file="GUIPhotos/061.png")
        labelBackground=Label(self,image=backgroundImage)
        labelBackground.place(x=0,y=0)
        labelBackground.image=backgroundImage
        #nume
        userImage = PhotoImage(file="GUIPhotos/040.png")
        labelNume = Label(self, image=userImage)
        labelNume.place(x=40, y=90,width=250, height=40)
        labelNume.image = userImage

        numeEntry = Entry(self)
        numeEntry.place(x=300, y=100,  width=150, height=24)

        labelWarningNume=Label(self,text="",fg="red",font="TimesNewRoman 10 bold")
        labelWarningNume.place(x=300,y=129)
        # prenume
        prenumeImage = PhotoImage(file="GUIPhotos/041.png")
        prenumeLabel = Label(self, image=prenumeImage)
        prenumeLabel.place(x=40, y=140, width=250, height=40)
        prenumeLabel.image = prenumeImage

        prenumeEntry = Entry(self)
        prenumeEntry.place(x=300, y=150, width=150,height=24)

        labelWarningPrenume = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningPrenume.place(x=300, y=179)

        # functie
        functieImage = PhotoImage(file="GUIPhotos/045.png")
        functieLabel = Label(self, image=functieImage)
        functieLabel.place(x=40, y=190, width=250, height=40)
        functieLabel.image = functieImage

        functieEntry = Entry(self)
        functieEntry.place(x=300, y=200,width=150, height=24)

        labelWarningFunctie = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningFunctie.place(x=300, y=229)

        #AL DOILEA PATRAT

        #marca
        marcaImage = PhotoImage(file="GUIPhotos/042.png")
        marcaLabel = Label(self, image=marcaImage)
        marcaLabel.place( x=40,y=270, width=250, height=40)
        marcaLabel.image = marcaImage

        marcaEntry = Entry(self)
        marcaEntry.place(x=300, y=280, width=150, height=24)

        labelWarningMarca = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningMarca.place(x=300, y=309)

        #model
        modelImage = PhotoImage(file="GUIPhotos/043.png")
        modelLabel = Label(self, image=modelImage)
        modelLabel.place(x=40, y=320, width=250, height=40)
        modelLabel.image = modelImage

        modelEntry= Entry(self)
        modelEntry.place(x=300, y=330,  width=150, height=24)

        labelWarningModel = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningModel.place(x=300, y=359)

        # culoare
        culoareImage = PhotoImage(file="GUIPhotos/044.png")
        culoareLabel = Label(self, image=culoareImage)
        culoareLabel.place(x=40, y=370, width=250, height=40)
        culoareLabel.image = culoareImage

        culoareEntry = Entry(self)
        culoareEntry.place(x=300, y=380, width=150,height=24)

        labelWarningCuloare = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningCuloare.place(x=300, y=409)

        #numar
        numarImage=PhotoImage(file="GUIPhotos/046.png")
        numarLabel = Label(self, image=numarImage)
        numarLabel.place(x=40,y=420, width=250, height=40)
        numarLabel.image = numarImage

        numarEntry = Entry(self)
        numarEntry.place(x=300, y=430,  width=150, height=24)

        labelWarningNumar = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningNumar.place(x=300, y=457)

        #warning


        # buton adauga masina
        buttonImage = PhotoImage(file="GUIPhotos/037.png")
        logButton = Button(self, image=buttonImage, relief=RIDGE,command=lambda:addMasina())
        logButton.place(y=500, x=118, width=266, height=35)
        logButton.image = buttonImage

        #buton go back
        buttonImage = PhotoImage(file="GUIPhotos/036.png")
        logButton = Button(self, image=buttonImage, relief=RIDGE, command=lambda: goBack())
        logButton.place(y=550, x=118,  width=266, height=35)
        logButton.image = buttonImage