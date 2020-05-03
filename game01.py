import random ,time 
from tkinter import messagebox
class Score:
    PointsArr = [None] * 2
    def __init__(self):
        self.PointsArr[0] = 0
        self.PointsArr[1] = 0
    
    def addPoints(self, player, points):
        self.PointsArr[player-1] += points
    
    def addPoint(self, player):
        self.PointsArr[player-1] += 1
    
    def getScore(self, player):
        return self.PointsArr[player-1]

def help():
    print("Hi my name is bot\nHere is an explanation of what all this software is \nif you want to continue writing 'yes' if you do not write 'no'\nif you wont to start play write 'start'")
    Continued = input("")
    if Continued == 'yes':
        print("ok let's \nstart the software is basically a competition between two contestants \nboth competing in 3 games which ultimately determines who won most of\n(the games work in random order)")
        print("game 1:\ngame 1 is the famous game 'hang man' \nI dont think that I need to explain how you playing the game")
        print("player 1 is chooses a word while player 2 close his eyes and Then he has to guess the word \nhe has 10 guesses if he managed to guess\nthe word he won if not the other one won  ")
        print("\n\ngame 2:\ngame 2 called 'test in math'\nin the game the software will give you 5 Account questions that their activity selected at random \n(there was more chance of a connection than any other action)")
        print("\n\ngame 3:\ngame 3 called 'X O' yes onther famous game in the game you need tם \nDesign on the board in a row / column / diagonal of X or O")
        say = input("if you wont to start play write 'start'")
        if say == 'start':
            print("so let's start\nFirst of all I wont to now your names")
        else :
            bot_start()
    elif Continued == 'start' :
        print("so let's start\nFirst of all I wont to now your names")
    else :
        bot_start()

def bot_start():
    print("Hi \nmy name is bot\nif you wont to start plase write 'start'\nif you wont an explanation plase wrait 'help'")
    Continued_1 = input("")
    if Continued_1 == 'start':
        print("so let's start\nFirst of all I wont to now your names")
    elif Continued_1 == 'help':
        help()
def game_1():

    print("now we going to play 'hang man'")
    print(f"player 1 {name_2} close your eyes until player 2 {name_1} write a word \nbut the word need to be with 3 - 7 letters and need to be a real word")
    word = input("enter your word...")
    show_word = '_' * len(word)
    print('\n' * 100)
    len_in_word = len(word) * 1
    print(show_word)
    print('you have ', len_in_word, 'letter to guesses' )

    guesses = 10
    guesses_letters = set()

    while True:
        guess = input(f'guess a letter or word: {show_word}\n you guessed the letters({", ".join(guesses_letters)})\n')
        if len(guess) == 1:
            guesses_letters.add(guess.lower())
            show_word = ''.join(c if c.lower() in guesses_letters else '_' for c in word )
            if '_' not in show_word:
                print(f'you guessed the word {word}')
                gameScore.addPoint(1)
                break
        if len(guess) > 1:
            if guess == word:
                print(f'you guess right, the word is {word}\n{name_2} you are the winer of this copotion')
                gameScore.addPoint(1)
                break
        else:
            print(f"sorry {guess} isn't the word")
        guesses-=1
        if not guesses:
            print(f' sorry the game has ended.the word is {word}\n{name_1} you are the winer of this copotion')
            gameScore.addPoint(2)
            break
        

def game_2():
    Score_player_2 = 0
    Score_player_1 = 0 
    input("we are going to play 'test in muth' plase press 'eneter' to start")
    shape = (2, 3, 4, 5, 6, 10, 12, 15, 30)
    print(f"turn: player 1 {name_2}")
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    input("Press Enter to start")
    start_time = time.time()
    r = 0
    num = 1
    for b in range(5):
        action = random.randint(1, 5)
        if action == 1:
            x = random.randint(50, 100)
            y = random.randint(1, 50)
            the_exercise = x - y
            print(f"How mach is {x} - {y}")
            Answer = int(input("enter your answer..."))

        elif action == 2:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            the_exercise  = x * y
            print(f"How mach is {x} x {y}")
            Answer = int(input("enter your answer..."))

        elif action == 3:
    
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            the_exercise  = x + y

            print(f"How mach is {x} + {y}")
            Answer = int(input("enter your answer..."))
        else:
            x = 60
            y = random.choice(shape)
            the_exercise  = x / y

            print(f"How mach is {x} / {y}")
            Answer = int(input("enter your answer..."))

        end_time = time.time()


        if Answer == the_exercise :
            Score_player_1 += 20
            print(f"Answer {num} is right")
            r += 1
        else:
            print(f"Answer {num} is wrong, the right answer is {the_exercise}")
        num += 1
        print(Score_player_1)
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    t = int(round(time_lapsed))
    Grade_1 = (Score_player_1 - t)
    print(f" your right in {r} Answers so\n you get {Score_player_1} points but you wasted (Rounded of course) {t} so you get {Grade_1} points")



    Score_player_2 = 0
    print(f"turn: player 2 {name_1}")
    def time_convert_2(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    input("Press Enter to start")
    start_time = time.time()
    r = 0
    num = 1
    for b in range(5):
        action = random.randint(1, 5)
        if action == 1:
            x = random.randint(50, 100)
            y = random.randint(1, 50)
            the_exercise = x - y
            print(f"How mach is {x} - {y}")
            Answer = int(input("enter your answer..."))

        elif action == 2:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            the_exercise  = x * y
            print(f"How mach is {x} x {y}")
            Answer = int(input("enter your answer..."))

        elif action == 3:
    
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            the_exercise  = x + y

            print(f"How mach is {x} + {y}")
            Answer = int(input("enter your answer..."))
        else:
            x = 60
            y = random.choice(shape)
            the_exercise  = x / y

            print(f"How mach is {x} / {y}")
            Answer = int(input("enter your answer..."))

        end_time = time.time()


        if Answer == the_exercise :
            Score_player_2 += 20
            print(f"Answer {num} is right")
            r += 1
        else:
            print(f"Answer {num} is wrong, the right answer is {the_exercise}")
        num += 1
        print(Score_player_2)
    time_lapsed_2 = end_time - start_time
    time_convert_2(time_lapsed_2)
    t2 = int(round(time_lapsed_2))
    Grade_2 = (Score_player_2 - t2)
    print(f" your right in {r} Answers so\n you get {Score_player_2} points but you wasted (Rounded of course) {t} Seconds so you get {Grade_2} points")
    if Grade_1 > Grade_2:
        print("player 2 win this stage")
        gameScore.addPoint(1)
    elif Grade_2 == Grade_1:
        print("you both get the same Grade")
    else :
        print("player 1 win this stage")
        gameScore.addPoint(2)
def game_3():
    input("Now we are going to play X O\nplase Press 'eneter' to start ")
    class game:
        def __init__(self, player_1, player_2):
            self.board = board()
            self.players = [player_1, player_2]
            self.turn = False

        def play(self):
            while True:
                corrent_player = self.players[int(self.turn)]

                print(self.board.to_string())
                inputMove = input(f"plesse {corrent_player.name} make move 0-8\n")
                print(f"Your move is: {inputMove}")
                move = int(inputMove)
                while True:
                    try:
                        is_winner = self.board.make_move(corrent_player, move)
                        break
                    except (ValueError, IndexError):
                        inputMove = input(f"the place is catch \nplesse {corrent_player.name} make move 0-8\n")
                        print(f"Your move is: {inputMove}")
                        move = int(inputMove)
                if is_winner or self.board.is_draw():
                    break
                self.turn = not self.turn
            print(self.board.to_string())
            if is_winner:
                print(f'Well done {corrent_player.name} you win !')
                if corrent_player.name == name_1:
                    gameScore.addPoint(2)
                else :
                    gameScore.addPoint(1)
            else:
                print("Sorry we have draw")

    class board:
        def __init__(self):
            self.board = [' '] * 9

        def to_string(self):
            return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}'.format(*self.board)

        def make_move(self, player, place):
            if self.board[place] != ' ':
                raise ValueError(f'sorry place{place} is alredy taken.')
            self.board[place] = player.maker
            return self.is_winner(player.maker)

        def is_winner(self, maker):
            winning_position = [
                [0,1,2],
                [3,4,5],
                [6,7,8],
                [0,3,6],
                [1,4,7],
                [2,5,8],
                [2,4,6],
                [0,4,8],
            ]
            return any([all ([self.board[x] == maker for x in pos]) for pos in winning_position])
        def is_draw(self):
            return ' ' not in self.board
    class player:
        def __init__(self, name, maker):
            self.name = name
            self.maker = maker


    game(player(name_2,'X'), player(name_1,'O')).play()
def bot_middle():
    print(f"ok \n {name_2} you are player 1\n{name_1} you are player 2")
    a = [1, 2, 3]
    for x in range(3):
        order = random.randint(0, len(a)-1)
        print("The array is: ", a, ", Random num is: ",order,", Value (game number) is: ",a[order])
        if a[order] == 1:
            game_1()
        if a[order] == 2:
            game_2()
        if a[order] == 3:
            game_3()
        a.pop(order)
    bot_final()
def bot_final():
    print("so the winner is...\n")
    if gameScore.getScore(1) > gameScore.getScore(2):
        messagebox.showinfo("Congratulations", "player 1 win!!!")
    elif gameScore.getScore(1) < gameScore.getScore(2):
        messagebox.showinfo("Congratulations", "player 2 win!!!")
    else:
        messagebox.showinfo("draw", "player 2 win and player 1 have the same scoring")

gameScore = Score()
print("test func: score is: ",gameScore.getScore(1))
bot_start()
name_1 = input("plase eneter the first name...")
name_2 = input("ok plase eneter the second name...")
bot_middle()
