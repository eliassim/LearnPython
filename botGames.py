import random
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
def game_2():
    x = 0
    y = 0 
    rongs_pleyer1 = 0
    rongs_pleyer2 = 0
    while y == 100:
        i = int(input("enter number or boom..."))
        if y % 7 == 0 or '7' in str (i):
            if str (i) == "boom":
                y =+ 1 
            else :
                if x == 0:
                    rongs_pleyer1 =+ 1
                    x == 1
                else :
                    rongs_pleyer2 =+ 1
                    x == 0
        else :
            if y == i:
                y =+ 1
            else :
                if x == 0:
                    rongs_pleyer1 =+ 1
                    x == 1
                else :
                    rongs_pleyer2 =+ 1
                    x == 0
def game3 ():
    class board: 
        def __init__(self):
            self.board = [' '] * 9

        def to_string(self):
            return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*self.board)


        def make_move(self, player, place):
            if self.board[place] != ' ':
                raise ValueError(f'Sorry the plase {place} already taken')
            self.board[place] = player.marker
            return self.winner_is (player.marker)

        def winner_is (self, marker):
            winning_positions = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],
            ]
            return any([all([self.board[x] == marker for x in pos])for pos in winning_positions])

    
    class player:
        def __init__(self, name, marker):
            self.name = name
            self.marker = marker
    class Game:
        def __init__(self, player1, player2):
            self.board = board()
            self.players = [player1, player2]
            self.turn = False
        def play(self):
            while True:
                current_player = self.players[int(self.turn)]

                print(self.board.to_string)
                move = int(input(f'This is the current board\n{current_player} plesse make your move '))
                print("Your move is: ", move)
                while True:
                    try:
                        is_winner = self.board.make_move(current_player, move)
                        break
                    except ValueError:
                        move = int(input(f'Sorry {current_player} the plasse is trap \nplesse make your move '))
                if is_winner:
                    break
                self.turn = not self.turn

    print(board().to_string()) 
    Game(player ('bob', 'x'), player ('moshe', 'o')).play()
def game_4():
    z = random.randint(1, 100)
    gass_player1 = 0
    gass_player2 = 0
    while gass_player1 == z or gass_player2 == z :
        gass_player1 = int(input("enter your gass player1... "))
        if gass_player1 == z:
            print(f"you gassed right \nthe number is {z}")
        else :
            print("sorry this is not the right number")
        gass_player2 = int(input("enter your gass player2... "))
        if gass_player2 == z:
            print(f"you gassed right \nthe number is {z}")
        else :
            print("sorry this is not the right number")
            
            
game_4()