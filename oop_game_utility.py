import random
import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-I4TGSED\SQLEXPRESS;'
                      'Database=Trivia;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
class game:
    def _init_(self):
        self.computer = []
    def get_computer(self):
            self.computer = []
            self.computer.append(["CPU is the parts of computer that used to disply out put?", "false"])
            self.computer.append(["BIOS is used to control the the process of sequnces ?", "true"])
            self.computer.append(["GITHUB IS a version control application spcialy software testing ?", "true"])
            self.computer.append(["verual machin is used to use one time in differnet tasks", "true"])
            self.computer.append(["among programing language is python is one of those ","true"])
            self.computer.append(["SQL IS languge ", "true"])
       # print('https://github.com/alelignb/poworbal.git')
            return self.computer
    def answer(self):
        answer = self.get_computer()
        score=0
        for i in answer:
            print("Choices true or false:\n" + i[0])
            guess = input("Enter your choices")
            if guess == i[1]:

             print("correct")
             score = score + 1
            else:
                print("your input answer incorrect\n","-the correct answer is ",i[1],)
            print("your  score is :" + str(score))


        return self.answer
    def get_general(self):
        self.generals = []
        self.generals.append(["when was iseral gets permissin from untid nation to consider us country"," 1948"])
        self.generals.append(["the firest priminister for isreal?","yizhak roben"])
        self.generals.append(["womens priminister in isreal?", "Golda mir"])
        self.generals.append(["the orgin of human bing in the world?", " ehtiopia"])
        self.generals.append(["what country is not coloniazed during colonolizem of africa?", " ethiopia"])
        self.generals.append(["the origin of blue nile rever?", "ethiopa"])
        return self.generals
    def general(self):
        gene = self.get_general()
        random.shuffle(self.get_general())
        score = 0
        for j in gene:
            print(":" + j[0])
            guess = input("Enter the possible ansewer")
            if guess == j[1]:
                print("correct")
                score = score + 1
            else:
                print("your input answer is incorrect\n :" , "the correct answer is ",j[1])
        print("your score is :" + str(score))


    def get_QA(self):
        self.QA = []
        self.QA.append(["which application used to test API testing?", "posman"])
        self.QA.append(["which funcatinal teting used to test a specfic point that "
                     "after fix some bugs or not?", "retest,unit test"])
        self.QA.append(["list non funcatinal test?", "load test,valume test,recovery test,GUI test,backupp test..."])
        self.QA.append(["what the small file sent to your browsers from the website you vist ?", "cookis"])
        self.QA.append(["lis types of memory?", "cach memory ,cookis,RAM,ROM,real time"])
        self.QA.append(["list test enviroment?", "stage and producation"])
        self.QA.append(["methdology of testing?", "agile,v-shape,watwefull"])
        return self.QA

    def QA(self):
        problem = self.get_QA()

        random.shuffle(self.get_QA())
        score = 0
        for n in problem:
            print("QA QUESTIONS:" + n[0])
            guess = input(" Enter the posible answer\n")
            if guess == n[1]:
                print("correct")
                score = score + 1
            else:
                print("your input answer is incorrect\n","-the correct answer is ",n[1])
        print("your score is :" + str(score))
class sql():
    def __init__(self):
        self.conect=[]
    def DB1(self):
        self.conect = []
        pID = int(input("ID"))
        fname = input("NAME")
        Score = int(input("score"))
        cursor.execute("INSERT INTO [Score] (ID,FNAME,Score) VALUES(?,?,?)",(pID,fname,Score))
        conn.commit()
        cursor.close()
        conn.close()
