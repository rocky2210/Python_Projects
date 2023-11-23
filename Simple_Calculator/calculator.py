from color import colors,fg,bg

global choice
class Calculator:
    def __init__(self):
        self.result = 0 

    def add(self, a, b):
        self.result = a + b
        return self.result

    def sub(self, a, b):
        self.result = a - b
        return self.result

    def mul(self, a, b):
        self.result = a * b
        return self.result

    def div(self, a, b):
        # if b == 0:
        #     print("Error: Division by zero.")
        # else:
        self.result = a / b
        return self.result

    # Menu
    def menu(self):
        print(fg.green+"\n\n----------------------------------------------------"+colors.reset)
        print(fg.red,colors.underline+"\tUser commands"+colors.reset)
        print(fg.blue+"\n\t1. Addition"+colors.reset)
        print(fg.blue+"\t2. Subtraction"+colors.reset)
        print(fg.blue+"\t3. Multiplication"+colors.reset)
        print(fg.blue+"\t4. Division"+colors.reset)
        print(fg.blue+"\t5. Previous result"+colors.reset)
        print(fg.blue+"\t6. Exit\n"+colors.reset)
        print(fg.red+"🔴 Note: Only accepts two values at a time"+colors.reset)
        print(fg.green+"----------------------------------------------------"+colors.reset)
        print("\n\n")

    # Menuchoice
    def menuchoice(self):
        while True:
            try:
                choice = int(input(fg.yellow+"Enter your choice: "+colors.reset))
                if 1<= choice <= 6:
                    return choice
                else:
                    print(fg.red+"\n\t❌ Please enter the valid choice (1 to 6)\n"+colors.reset)
            except ValueError:
                print(fg.red+"\n\t❌ Value error please enter valid choice (1 to 6)\n"+colors.reset)

    # Header
    def header(self):
        print("  ____  _                 _         ____      _            _       _              ")
        print(" / ___|(_)_ __ ___  _ __ | | ___   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __  ")
        print(" \\___ \\| | '_ ` _ \\| '_ \\| |/ _ \\ | |   / _` | |/ __| | | | |/ _` | __/ _ \\| '__| ")
        print("  ___) | | | | | | | |_) | |  __/ | |__| (_| | | (__| |_| | | (_| | || (_) | |    ")
        print(" |____/|_|_| |_| |_| .__/|_|\\___|  \\____\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|    ")
        print("                   |_|                                                            ")
        print("\t\t\t\t Made by ❤️ lila")

    # Result
    @staticmethod
    def boxoutput(message,result):
        result_str = str(result)
        box = len(message) + len(result_str) * 4 #both side 2+2
        boxresult = f'| {message} {result} |'
        print(fg.red+'\n+' + '-' * box +'+'+colors.reset)
        print(fg.cyan+boxresult+colors.reset)
        print(fg.red+'+' + "-" * box +'+'+colors.reset)

    # Exit
    def exit(self):
        print(fg.green+"Thank you.💯"+colors.reset)
        print(fg.green+"Thank you.....✌️"+colors.reset)
        print(fg.green+"Thank you.......!😁"+colors.reset)
