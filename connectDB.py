import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                       'Server=DESKTOP-I4TGSED\SQLEXPRESS;'
                       'Database=Trivia;'
                       'Trusted_Connection=yes;')
cursor = conn.cursor()
class SQL():
    def init(self):
     self.conect=[]
    def DB1(self):
     self.conect = []
    PersonID = int(input("ID"))
    FName=input('fname')
    Ctagory=input('category')
    Qustion=input('quastion')
    #Answer=input('answer')
    cursor.execute("INSERT INTO [Quation] (PersonID,FName,Ctagory,Qustion) VALUES(?,?,?,?)",(PersonID,FName, Ctagory,Qustion))
    conn.commit()
    cursor.close()
    conn.close()
b=SQL()
b.DB1()