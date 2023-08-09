class QuizApp:
    def __init__(self):
        self.username = ""

    def greeting(self):
        print()
        print("----------------------------------------")
        print("--------Welcome to Python Quiz!!--------")
        print("----------------------------------------")
        print()
    def menuHeader(self):
        print()
        print("---------------------------")
        print("Please input your choice from the options below:")
        print("(M): Repeat this menu")
        print("(L): List available quizzes")
        print("(T): Take a quiz")
        print("(E): Exit the program")
        print()
    def menuSelectionError(self):
        print("I'm sorry, but that's not a valid input, please try again.")
    def goodbye(self):
        print()
        print("----------------------------------------")
        print(f"--Thanks {self.username} for playing!--")
        print("----------------------------------------")
        print()
    def menu(self):
        self.menuHeader()
        
        while(True):
            print()
            print("----------------------------------------")
            selection = input("Selection: ")
            if len(selection) == 0:
                self.menuSelectionError()
                continue
            selection = selection.capitalize()
            if selection[0] == "E":
                self.goodbye()
                break
            elif selection[0] == "M":
                self.menuHeader()
                continue
            elif selection[0] == "L":
                print()
                print("----------------------------------------")
                print("Available Quizzess to be added")
                print()
                # TODO: list all available quizzess
                continue
            elif selection[0] == "T":
                try:
                    quizID = int(input("Enter desired quiz ID number: "))
                    print(f"You've selected quiz {quizID}")
                    # TODO start selected quiz
                except:
                    self.menuSelectionError()
                continue
            else:
                self.menuSelectionError()

    def startup(self):
        # Prints the greeting at startup
        self.greeting()
        self.username = input("Please type your username: ")
        print()
        print(f"Welcome to our quiz app {self.username}")

    def run(self):
        # Execute the startup routine, asking for username
        # printing greeting and so on...
        self.startup()
        # Starts the main program menu and run until user
        # inputs exit option
        self.menu()

if __name__ == "__main__":
    app = QuizApp()
    app.run()