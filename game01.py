import random ,time 
def help():
    print("Hi my name is bot\nHere is an explanation of what all this software is \nif you want to continue writing 'yes' if you do not write 'no'")
    Continued = input("")
    if Continued == 'yes':
        print("ok Let's \nstart the software is basically a competition between two contestants \nboth competing in 3 games which ultimately determines who won most of\n(the games work in random order)")
        print("game 1:\ngame 1 is the famous game 'hang man' \nI dont think that I need to explain how you playing the game")
        print("player 1 is chooses a word while player 2 close his eyes and Then he has to guess the word \nhe has 10 guesses if he managed to guess\nthe word he won if not the other one won  ")
        print("\n\ngame 2:\ngame 2 called 'test in math'\nin the game the software will give you 5 Account questions that their activity selected at random \n(there was more chance of a connection than any other action)")
        print("\n\ngame 3:\ngame 3 called 'X O' yes onther famous game in the game you need tם \nDesign on the board in a row / column / diagonal of X or O")
    else :
        print("okk")

def game_1():
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
                break
        if len(guess) > 1:
            if guess == word:
                print(f'you guess right the word is {word}')
                break
        else:
            print(f"sorry {guess} isn't the word")
        guesses-=1
        if not guesses:
            print(f'sorry the game has ended.the word is {word}')
            break
def game_4():
    x = 0
    t = 0
    n = 1
    Player_1_score = 0
    Player_2_score = 0
    while x == 50 :
        num = int(input('enter num...'))
        if n == num or str(num) == 'boom':
            t += 1
        else:
            print("Sorry you rong")
            if num % 2 == 1:
                Player_2_score += 1
            else :
                Player_1_score += 1
        x += 1
        n += 1


def game_3():
    shape = (2, 3, 4, 5, 6, 10, 12, 15, 30)
    Score_player_1 = 0
    Score_player_2 = 0
    print("turn: player 1")
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
    print("turn: player 2")
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
    print(f" your right in {r} Answers so\n you get {Score_player_2} points but you wasted (Rounded of course) {t} Seconds so you get {Grade_1} points")
    if Grade_1 > Grade_2:
        print("player 2 win this stage")
    else :
        print("player 1 win this stage")
def game_2():
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


    game(player('bob','x'), player('moshe','o')).play()
