import chess
import chess.engine
import chess.svg
import random
import time
import sys
from IPython.display import display, SVG, clear_output
from mover import game

def square_to_coordinates(coordinates):
    print(coordinates)
    if coordinates[0] == "a":
        return [int(coordinates[1])-1, 7]
    elif coordinates[0] == "b":
        return [int(coordinates[1])-1, 6]
    elif coordinates[0] == "c":
        return [int(coordinates[1])-1, 5]
    elif coordinates[0] == "d":
        return [int(coordinates[1])-1, 4]
    elif coordinates[0] == "e":
        return [int(coordinates[1])-1, 3]
    elif coordinates[0] == "f":
        return [int(coordinates[1])-1, 2]
    elif coordinates[0] == "g":
        return [int(coordinates[1])-1, 1]
    elif coordinates[0] == "h":
        return [int(coordinates[1])-1, 0]
    else:
        raise ValueError("This square is not known.")

def uci_to_coordinates(uci_move):
    # The piece type is the first character, which we can ignore
    # The next two characters are the starting square
    start_square = uci_move[-4:-2]
    # The last two characters are the target square
    end_square = uci_move[-2:]
    return [square_to_coordinates(start_square), square_to_coordinates(end_square)]

class Game:

    def __init__(self, player_colour="random", engine_difficulty = 10) -> None:
        self.player_colour = player_colour
        self.board = chess.Board()
        engine_path = "/opt/homebrew/bin/stockfish"

        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)

        self.engine.configure({"Skill Level": engine_difficulty})
        
        if self.player_colour == "random":
            coin_flip = random.choice([0, 1])

            if coin_flip == 0:
                self.player_colour = "white"
            else:
                self.player_colour = "black"

        self.display_board()
        self.game()

    def display_board(self):
        clear_output(wait=True)
        display(SVG(chess.svg.board(board=self.board)))

    def game(self) -> None:
        while True:
            self.white_move()
            self.black_move()

    def white_move(self):
        if self.player_colour == "white":
            self.player_move()
        else:
            self.engine_move()

    def black_move(self):
        if self.player_colour == "white":
            self.engine_move()
        else:
            self.player_move()

    def move(self, move):
        self.board.push(chess.Move.from_uci(move))
        coordinates = uci_to_coordinates(move)
        self.api_move_arm(coordinates)
        self.display_board()

    def is_legal_move(self, move) -> bool:
        try:
            if chess.Move.from_uci(move) in self.board.legal_moves:
                return True
        except ValueError: #need to specify this
            return False
        return False

    def api_move_arm(self, coordinates) -> None:
        game([coordinates])

    def player_move(self) -> None:
        while True:
            player_move = input("Please enter your next move (press t to terminate)\n")
            print(self.is_legal_move(player_move))
            if self.is_legal_move(player_move):
                self.move(player_move)
                break
            elif (player_move == 't' or player_move == 'T'):
                sys.exit("Ended game.")
            else:
                legal_moves = list(self.board.legal_moves)
                legal_moves_str = ", ".join(move.uci() for move in legal_moves)
                print("Your move is not valid, valid moves: ", legal_moves_str)

    def engine_move(self) -> None:
        time.sleep(1)
        engine_move = str(self.engine.play(self.board, chess.engine.Limit(time=1.0)).move)
        print(engine_move)
        self.move(engine_move)
