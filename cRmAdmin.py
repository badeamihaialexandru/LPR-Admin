from tkinter import *
import tkinter as tk
from tkinter import ttk
import cAdminMenu
import cSucces
import cLPRDataBase
import cButtonTreeView
from PIL import Image, ImageTk


class RemoveAdminFrame(tk.Frame):
    def menubar(self, root):
        menubar = tk.Menu(root)
        return menubar

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)

        def dropAdmin():
            toRemove=vedereCopac.tag_has('checked')
            if len(toRemove)==0:
                labelWarningSelect.config(text="Selectati un username!")
            else:
                for admin_ID in toRemove:
                    mydb.removeUser(admin_ID)
                vedereCopac.delete(*vedereCopac.get_children())
                adminiDinBaza = mydb.listareTotiAdmini()
                for admin in adminiDinBaza:
                    vedereCopac.insert("", "end", admin[0], values=(admin[1]))
                controller.show_frame(cSucces.SuccesFrame)

        def filterAdmin(usernameEntry):
            if usernameEntry=="":
                entryNume.config(highlightbackground="red", highlightthickness=1)
                labelWarningNume.config(text="Introduceti un username!")
            else:
                mydb = cLPRDataBase.myDataBase()
                answer=mydb.listareAdminiLevenshtein(usernameEntry)
                vedereCopac.delete(*vedereCopac.get_children())
                for row in answer:
                    vedereCopac.insert("", "end", row[0], values=(row[1]))

        def refreshTable():
            vedereCopac.delete(*vedereCopac.get_children())
            mydb = cLPRDataBase.myDataBase()
            adminiDinBaza = mydb.listareTotiAdmini()
            for admin in adminiDinBaza:
                vedereCopac.insert("", "end", admin[0], values=(admin[1]))

        def goBack():

            entryNume.config(highlightthickness=0)
            labelWarningNume.config(text="")
            labelWarningSelect.config(text="")
            entryNume.delete(0,END)
            controller.show_frame(cAdminMenu.AdminFrame)


        backgroundImage=PhotoImage(file="GUIPhotos/062.png")
        label = ttk.Label(self,image=backgroundImage)
        label.place(x=0,y=0,relwidth=1,relheigh=1)
        label.image=backgroundImage


        # username
        userImage = PhotoImage(file="GUIPhotos/052.png")
        labelNume = Label(label, image=userImage)
        labelNume.place(x=80, y=70,width='250', height='40')
        labelNume.image=userImage

        entryNume = Entry(label)
        entryNume.place(x=40, y=120, width=250,height=24)

        labelWarningNume=Label(self,text="",font="TimesNewRoman 10 bold",fg="red")
        labelWarningNume.place(x=40,y=144)

        #buton cautare dupa nume
        butonCautareImage=PhotoImage(file="GUIPhotos/066.png")
        butonCautare=Button(self,image=butonCautareImage,relief=RIDGE,
                            command=lambda: filterAdmin(entryNume.get()))
        butonCautare.place(x=340,y=120,width='120',height='24')
        butonCautare.image=butonCautareImage

        #buton refresh table
        butonRefreshImage=PhotoImage(file="GUIPhotos/067.png")
        butonRefresh=Button(self,image=butonRefreshImage,relief=RIDGE,
                            command=lambda: refreshTable())
        butonRefresh.place(x=20,y=210,height=30,width=460)
        butonRefresh.image=butonRefreshImage

        #TreeView

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y, pady=(250, 150))
        scrollbar.place(x=480,y=250,height=200)

        vedereCopac=cButtonTreeView.CheckboxTreeview(self, columns=("username",),yscrollcommand = scrollbar.set)
        scrollbar.config(command=vedereCopac.yview)

        vedereCopac.place(x=20,y=250,height=200,width=460)

        mydb = cLPRDataBase.myDataBase()
        adminiDinBaza=mydb.listareTotiAdmini()
        for admin in adminiDinBaza:
            vedereCopac.insert("","end",admin[0],values=(admin[1]))

        #label warning
        labelWarningSelect=Label(self,text="",fg="red",font="TimesNewRoman 10 bold")
        labelWarningSelect.place(x=20,y=450)

        #buton sterge
        buttonImage = PhotoImage(file="GUIPhotos/047.png")
        logButton = Button(label, image=buttonImage,relief=RIDGE,
                           command=lambda: dropAdmin())
        logButton.place(y=480, x=117, width="266", height='35')
        logButton.image=buttonImage

        # buton inapoi
        buttonImage = PhotoImage(file="GUIPhotos/036.png")
        logButton = Button(label, image=buttonImage, relief=RIDGE,
                           command=lambda: goBack())
        logButton.place(y=530, x=117,width="266", height='35')
        logButton.image = buttonImage
