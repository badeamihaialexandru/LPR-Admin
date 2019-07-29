import mysql.connector
from argon2 import PasswordHasher
from passlib.hash import argon2
import datetime

class myDataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='bd1967bd',
                                      host='127.0.0.1',
                                      database='mydb')
        self.myCursor = self.mydb.cursor(buffered=True)

    def checkUserExists(self,username):
        query="SELECT * FROM admini WHERE username=\'"+username+"\'"
        self.myCursor.execute(query)
        if self.myCursor.fetchone() is None:
            return False
        else:
            return True

    def addUser(self,username,password):
        passHash=argon2.hash(password)
        query="insert into admini VALUES (NULL,\'"+username+"\',\'"+passHash+"\')"
        self.myCursor.execute(query)
        self.mydb.commit()

    def removeCar(self, car_id):
        # verifica daca exista mai intai, cu metoda de mai sus!!!
        query = "UPDATE numereinmat SET Acces =0 WHERE numere_ID =\'" + car_id + "\'"
        self.myCursor.execute(query)
        self.mydb.commit()

    def removeUser(self,admin_id):
        #verifica daca exista mai intai, cu metoda de mai sus!!!
        query="DELETE FROM admini WHERE admin_ID=\'"+admin_id+"\'"
        self.myCursor.execute(query)
        self.mydb.commit()

    def loginUser(self,username,password):
        try:
            query="SELECT parola FROM admini WHERE username=\'"+username+"\'"
            self.myCursor.execute(query)
            answer= self.myCursor.fetchone()


            if argon2.verify(password,answer[0]):
       #     if password==answer[0]:
                return True
        except:
            return False



    def addPersoana(self,nume,prenume,functie,):
        query="SELECT persoane_ID FROM persoane where Nume=\'"+nume+"\'AND Prenume=\'"+prenume+"\'AND Functie=\'"+functie+"\'"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchone()
        if answer is None:
            newQuery="INSERT INTO persoane VALUES (NULL,\'"+nume+"\',\'"+prenume+"\',\'"+functie+"\')"
            self.myCursor.execute(newQuery)
            self.mydb.commit()
            lastQuery=" SELECT LAST_INSERT_ID() "
            self.myCursor.execute(lastQuery)
            return self.myCursor.fetchone()
        else:
            return answer

    def addCuloare(self,culoare):
        # adaugare culoare
        query = "SELECT culori_ID FROM culori WHERE culoare=\'" + culoare + "\'"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchone()
        if answer is None:
            secondQuery="INSERT INTO culori VALUES (NULL,\'"+culoare+"\') "
            self.myCursor.execute(secondQuery)
            self.mydb.commit()
            lastQuery = " SELECT LAST_INSERT_ID() "
            self.myCursor.execute(lastQuery)
            return self.myCursor.fetchone()
        else:
            return answer


    def addNumar(self,numar,culoare,model,marca,nume,prenume,functie):
        persoana_id=self.addPersoana(nume,prenume,functie)
        culoare_id=self.addCuloare(culoare)
        query="SELECT numere_ID,acces FROM numereinmat WHERE NumarInmatriculare=\'"+numar+"\'"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchone()
        if answer is not None:
            if answer[1] is "1":
                return -1
            else:
                newQuery = "UPDATE numereinmat SET acces=1 where numere_ID=\'"+answer[0].astype(str)+"\'"
                self.myCursor.execute(newQuery)
                self.mydb.commit()
                return 1
        else:
            newQuery="INSERT INTO numereinmat VALUES (NULL,\'"+str(persoana_id[0])+"\',\'"+str(culoare_id[0])+"\',\'"+\
                     numar+"\',\'"+marca+"\',\'"+model+"\',\'1\')"
            self.myCursor.execute(newQuery)
            self.mydb.commit()
            return 1

    def removeNumar(self,numar):
        query="SELECT numere_ID FROM numereinmat WHERE NumarInmatriculare=\'"+numar+"\'"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchone()
        if answer is None:
            return -1
        else:
            newQuery="DELETE FROM tranzitii WHERE numereInmat_numere_ID=\'"+str(answer[0])+"\'"
            newScndQuery="DELETE FROM numereinmat WHERE numere_ID=\'"+str(answer[0])+"\'"
            self.myCursor.execute(newQuery)
            self.mydb.commit()
            self.myCursor.execute(newScndQuery)
            self.mydb.commit()
            return 1
    def listareMasiniLevenshtein(self,userIntrodus):
        query ="SELECT numere_id,nume,prenume,functie,NumarInmatriculare FROM numereinmat INNER JOIN persoane ON "\
               "persoane_persoane_ID=persoane_ID WHERE levenshtein_ratio(\'"+userIntrodus+"\',nume)>30 AND acces=1"
        self.myCursor.execute(query)
        answer = self.myCursor.fetchall()
        return answer

    def listareAdminiLevenshtein(self,adminIntrodus):
        query="SELECT admin_ID, username FROM admini WHERE levenshtein_ratio(\'"+adminIntrodus+"\',username)>30 "
        self.myCursor.execute(query)
        answer=self.myCursor.fetchall()
        return answer

    def listareTotiAdmini(self):
        query="SELECT admin_ID,username FROM admini"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchall()
        return answer

    def listareToateMasini(self):
        query="SELECT numere_id,nume,prenume,functie,NumarInmatriculare FROM numereinmat INNER JOIN persoane ON "\
              "persoane_persoane_ID=persoane_ID AND acces=1"
        self.myCursor.execute(query)
        answer=self.myCursor.fetchall()
        return answer

    def __del__(self):
        self.mydb.close()


