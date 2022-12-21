import pyodbc
from colorama import Fore

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-I4TGSED\SQLEXPRESS;'
                      'Database=Trivia;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT *FROM dbo.Quation')


class bdo:
    def __init__(self):
        self.lst = []

    def main(self):
        self.lst = []

    for row in cursor:
        use_input = input(Fore.CYAN + "are you ready? yes or no: " + Fore.RESET)
        if use_input == 'yes':
            cat = input(Fore.GREEN + "please enter category:c/l/g " + Fore.RESET)
            if cat == 'c':
                cursor.execute('select Qustion from Quation where PersonID = 1')
                row = cursor.fetchall()
                emp = []
                for question in row:
                    print(question)
                    answer = input(Fore.YELLOW + "please enter your answer " + Fore.RESET)
                    print("answer is", answer)
                    emp.append(answer)
                    print(emp)
                    cursor = conn.cursor()
                    cursor.execute('SELECT  answer from Answer where ID =1')
                for answer in cursor:
                    print("The correct answer is", answer)
            if cat == 'g':
                cursor.execute('select Qustion from Quation where PersonID = 2')
                row = cursor.fetchall()
                emp = []
                for question in row:
                    print(question)
                    answer = input("please enter your answer: ")

                    print("answer is", answer)
                    emp.append(answer)
                    print(emp)
                    cursor = conn.cursor()
                    cursor.execute('SELECT answer from Answer where ID =2')
                for answer in cursor:
                    print("The correct answer is", answer)
            if cat == 'l':
                cursor.execute('select Qustion from Quation  where PersonID = 3')
                row = cursor.fetchall()
                emp = []
                for question in row:
                    print(question)
                    answer = input("please enter your answer: ")
                    print("answer is", answer)
                    emp.append(answer)
                    print(emp)
                    cursor = conn.cursor()
                    cursor.execute('SELECT  answer from Answer where ID =3')
                for answer in cursor:
                    print("The correct answer is", answer)
