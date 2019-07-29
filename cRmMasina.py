from tkinter import *
import tkinter as tk
from tkinter import ttk
import cAdminMenu
import cSucces
import cLPRDataBase
import cMasinaTreeView
from PIL import Image, ImageTk


class RemoveMasinaFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        def dropCar():

            toRemove = vedereCopac.tag_has('checked')
            if len(toRemove) == 0:
                labelWarningSelect.config(text="Selectati un username!")
            else:
                for masina_ID in toRemove:
                    mydb.removeCar(masina_ID)
                vedereCopac.delete(*vedereCopac.get_children())
                masiniDinBaza = mydb.listareToateMasini()
                for masina in masiniDinBaza:
                    vedereCopac.insert("", "end", masina[0], values=(masina[1], masina[2], masina[3], masina[4]))
                controller.show_frame(cSucces.SuccesFrame)


            obj=cLPRDataBase.myDataBase()
            answer=obj.removeCar(entryNume.get())
            if answer is -1:
                entryNume.config(highlightbackground="red", highlightthickness=1)
                labelWarningNume.config(text="Masina nu exista in baza de date", fg="red")
            else:
                entryNume.config(highlightthickness=0)
                entryNume.delete(0, END)
                labelWarningNume.config(text="")
                controller.show_frame(cSucces.SuccesFrame)
        def goBack():
            entryNume.config(highlightthickness=0)
            entryNume.delete(0,END)
            labelWarningNume.config(text="")
            controller.show_frame(cAdminMenu.AdminFrame)

        def refreshTable():
            vedereCopac.delete(*vedereCopac.get_children())
            mydb = cLPRDataBase.myDataBase()
            masiniDinBaza = mydb.listareToateMasini()
            for masina in masiniDinBaza:
                vedereCopac.insert("", "end", masina[0], values=(masina[1],masina[2],masina[3],masina[4]))

        def filterCar(usernameEntry):
            if usernameEntry=="":
                entryNume.config(highlightbackground="red", highlightthickness=1)
                labelWarningNume.config(text="Introduceti un username!")
            else:
                mydb = cLPRDataBase.myDataBase()
                answer=mydb.listareMasiniLevenshtein(entryNume.get())
                vedereCopac.delete(*vedereCopac.get_children())
                for row in answer:
                    vedereCopac.insert("", "end", row[0], values=(row[1], row[2], row[3], row[4]))


        backgroundImage = PhotoImage(file="GUIPhotos/065.png")
        label = ttk.Label(self,image=backgroundImage)
        label.pack(fill=BOTH, expand=YES)
        label.image=backgroundImage


        # username
        userImage = PhotoImage(file="GUIPhotos/068.png")
        labelNume = Label(label, image=userImage)
        labelNume.place(x=45, y=73,width='250', height='40')
        labelNume.image=userImage

        entryNume = Entry(label)
        entryNume.place(x=40, y=120, width=250,height=24)

        labelWarningNume = Label(self, text="", font="TimesNewRoman 10 bold", fg="red")
        labelWarningNume.place(x=40, y=144)

        # buton cautare dupa nume
        butonCautareImage = PhotoImage(file="GUIPhotos/066.png")
        butonCautare = Button(self, image=butonCautareImage, relief=RIDGE,
                            command=lambda: filterCar(entryNume.get()))
        butonCautare.place(x=340, y=120, width='120', height='24')
        butonCautare.image = butonCautareImage


        #buton refresh
        butonRefreshImage = PhotoImage(file="GUIPhotos/067.png")
        butonRefresh = Button(self, image=butonRefreshImage, relief=RIDGE,
                              command=lambda: refreshTable())
        butonRefresh.place(x=20, y=210, height=30, width=460)
        butonRefresh.image = butonRefreshImage

        #Vedere copac

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y, pady=(250, 150))
        scrollbar.place(x=480, y=250, height=200)

        vedereCopac = cMasinaTreeView.CheckboxTreeview(self, columns=("nume","prenume","functie","numar"), yscrollcommand=scrollbar.set)
        scrollbar.config(command=vedereCopac.yview)
        vedereCopac.place(x=20, y=250, height=200, width=460)

        mydb=cLPRDataBase.myDataBase()
        masiniDinBaza=mydb.listareToateMasini()
        for masina in masiniDinBaza:
            vedereCopac.insert("","end",masina[0],values=(masina[1],masina[2],masina[3],masina[4]))

        # label warning select
        labelWarningSelect = Label(self, text="", fg="red", font="TimesNewRoman 10 bold")
        labelWarningSelect.place(x=20, y=450)

        #buton sterge
        buttonImage = PhotoImage(file="GUIPhotos/047.png")
        logButton = Button(label, image=buttonImage,relief=RIDGE,
                           command=lambda: dropCar())
        logButton.place(y=480, x=117, width="266", height='35')
        logButton.image=buttonImage

        # buton back
        buttonImage = PhotoImage(file="GUIPhotos/036.png")
        logButton = Button(label, image=buttonImage, relief=RIDGE,
                           command=lambda: goBack())
        logButton.place(y=530, x=117,width="266", height='35')
        logButton.image = buttonImage
