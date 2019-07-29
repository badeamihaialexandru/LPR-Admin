import tkinter as tk
import cLogIn
import cAdminMenu
import cAddAdmin
import cSucces
import cAddPersoana
import cRmAdmin
import cRmMasina
class interfata(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x600")
        self.resizable(False,False)
        self.title("NrDeInamtRecunoscatatorul")
        container=tk.Frame(self)
        container.pack(fill="both",expand=True)


        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.usernameAdmin=['mihaibda']
        self.passwordAdmin=['mihaibda']
        self.x=None
        self.y=None
        self.assign_ops=None
        self.Label=""  #pentru labelul de sub poza cu masina

        self.frames={}

        for F in (cLogIn.LoginFrame, cAdminMenu.AdminFrame, cAddAdmin.AddAdminFrame,cSucces.SuccesFrame,
                  cAddPersoana.AddPersoanaFrame,cRmAdmin.RemoveAdminFrame,cRmMasina.RemoveMasinaFrame):
            frame = F(container,self)

            self.frames[F]= frame

            frame.grid(row=0, column=0,sticky="nsew")

        self.show_frame( cLogIn.LoginFrame )

    def show_frame(self,cont):
 #       if cont==cPanouControl.PanouControl:
        self.geometry("500x600")
        frame=self.frames[cont]
        frame.tkraise()

        menubar = frame.menubar(self )
        self.configure(menu=menubar)

app=interfata()
app.mainloop()