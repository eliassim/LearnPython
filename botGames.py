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
