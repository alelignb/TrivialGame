from utility import game
from colorama import Fore
game()
class collig (game):
    def man(self):
        user = input(Fore.GREEN + "Are you ready to start ?" + Fore.RESET)
        if user == "yes":
            print(Fore.BLUE + "will come to our question game!you can play 2 games  " + Fore.RESET)
        else:
            exit()
            print("Sorry you are not get permission")
        choice = input("Place inter your choirs depending on the"
                       " question\n-computer= c\n-general knowledge = g\n-logic=l\n enter chose ")
        if choice == "c":
            self.answer()

        elif choice == "g":
            self.general()
        elif choice == "l":

            self.QA()
        else:
            print(Fore.RED + "place select at list one category" + Fore.RESET)
a = collig()
a.man()
