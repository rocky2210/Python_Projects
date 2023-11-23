import random
import time
from color import colors,fg,bg

class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0

    def increment_score(self):
        self.score += 1

#== User choice class ==#
class Person(Player):
    def choose(self):
        return int(input(fg.cyan+"\n\t\t\n\t\t 1. Rock 🪨 \n\t\t 2. Scissors ✂️ \n\t\t 3. Paper 📄"+colors.reset+fg.red+"\nEnter you choose: "+colors.reset))

#== Computer choice class ==#
class Computer(Player):
    def choose(self):
        return random.randint(1,3)

#== Main game class ==#
class RockPaperScissors:
    def __init__(self):
        self.print_header()
        self.player = Person(input(fg.green+"Enter your name : "+colors.reset))
        self.computer = Computer("Computer")
        self.draws = 0

    #== Header method ==#
    def print_header(self):
        print("""
        ______           _     ______                       _____      _                
        | ___ \\         | |    | ___ \\                     /  ___|    (_)                
        | |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __  \\ `--.  ___ _ ___ ___  ___  _ __ ___
        |    // _ \\ / __| |/ / |  __/ _` | '_ \\ / _ \\ '__|  `--. \\/ __| / __/ __|/ _ \\| '__/ __|    
        | |\\ \\ (_) | (__|   <  | | | (_| | |_) |  __/ |    /\\__/ / (__| \\__ \\__ \\ (_) | |  \\__ \\    
        \\_| \\_\\___/ \\___|_|\\_\\ \\_|  \\__,_| .__/ \\___|_|    \\____/ \\___|_|___/___/\\___/|_|  |___/    
                                        | |                                                    
                                        |_|                                                    
        \t\t\t\t\tMade by ❤️ lila (Rocky)
        """)
    
    #== ScoreBoard method  ==# 
    def print_scoreboard(self):
        print("\n\t\t\t================================")
        print(fg.red+colors.underline+f"\t\t\t\tScoreBoard"+colors.reset)
        print(fg.green+f"\t\t\t 😋 {self.player.name}: {self.player.score}"+colors.reset)
        print(fg.red+f"\t\t\t 🤖 Computerscore: {self.computer.score}"+colors.reset)
        print(fg.cyan+f"\t\t\t 🕊️  Draws: {self.draws}"+colors.reset)
        print("\t\t\t================================\n")

    #== Gamelogic method ==# 
    def play_round(self,player_choice):
        computer_choice = self.computer.choose()
        print(fg.blue+f"\nOpponent choice : {'Rock 🪨' if computer_choice == 1 else 'Scissors ✂️' if computer_choice == 2 else 'Paper 📄'}"+colors.reset)
        
        if(player_choice < 1 or player_choice > 3):
            print(bg.red+"\n\t\tInvalid option. Please choose again."+colors.reset)
        else:
            if player_choice == computer_choice:
                print("\n\t\t\t==========================")
                print(fg.purple+"\t\t\t   Draw...🤜🤛"+colors.reset)
                print("\t\t\t==========================\n")
                self.draws +=1
            elif (player_choice == 1 and computer_choice == 2) or \
                (player_choice == 2 and computer_choice == 3) or \
                (player_choice == 3 and computer_choice == 1):
                print("\n\t\t\t==========================")
                print(fg.green+"\t\t\t   You win...👍"+colors.reset)
                print("\t\t\t==========================\n")
                self.player.increment_score()  
            else:
                print("\n\t\t\t==========================")
                print(fg.red+"\t\t\t    Opponent win...👎"+colors.reset)
                print("\t\t\t==========================\n")
                self.computer.increment_score()   

    #== Main game method ==# 
    def play_game(self):
        while True:
            player_choice = int(input(fg.orange+"\n\t\t\t 1. Play a round 🕹️\n\t\t\t 2. View scoreboard 💯\n\t\t\t 3. Exit ❌ \n"+colors.reset+fg.green+" Choose an option : "+colors.reset))
            
            if player_choice == 1:
                self.play_round(self.player.choose())
            elif player_choice == 2:
                self.print_scoreboard()
            elif player_choice == 3:
                print(fg.green+"\nExiting...", end="")
                for _ in range(5):
                    time.sleep(0.1)
                    print("....", end="", flush=True)
                print("👋\n"+colors.reset)
                break
            elif(player_choice < 1 or player_choice > 3):
                print(bg.red+"\n\t\tInvalid option. Please choose again."+colors.reset)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()