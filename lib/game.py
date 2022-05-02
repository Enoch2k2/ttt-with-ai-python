import os
import pdb

def inbetween(value, min, max):
  return value >= min and value <= max

class Game:
  WIN_COMBO = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
  ]

  def __init__(self, player_1, player_2, board):
    self.player_1 = player_1
    self.player_2 = player_2
    self.board = board
    self.play()

  def turn(self):
    
    user_input = int(self.current_user().move(self.board))

    if(self.valid_move(user_input)):
      # current user makes a move
      # display the move
      self.clear_terminal()
      self.board.update(self.current_user().token, user_input - 1)
      self.board.display()
    else:
      self.clear_terminal()
      self.invalid_message()
      self.board.display()
      self.turn()

  def current_user(self):
    return self.player_1 if self.turn_count() % 2 == 0 else self.player_2

  def turn_count(self):
    return self.board.cells.count("X") + self.board.cells.count("O")

  def valid_move(self, user_input):
    return inbetween(user_input, 1, 9) and not self.board.position_taken(user_input - 1)

  def cats_game(self):
    return self.board.full() and not self.won() # is full or no winner

  def won(self):
    return next((win_combo for win_combo in Game.WIN_COMBO if self.board.cells[win_combo[0]] == self.board.cells[win_combo[1]] and self.board.cells[win_combo[1]] == self.board.cells[win_combo[2]] and self.board.cells[win_combo[2]]!= " "), False)

  def winner(self):
    return self.board.cells[self.won()[0]]

  def game_over(self):
    return self.cats_game() or self.won()

  def invalid_message(self):
    print("You typed something incorrect, please try again!")
  
  def clear_terminal(self):
    os.system("clear")

  def play(self):
    self.board.display()
    while not self.game_over():
      self.turn()
    
    if(self.won()):
      print(f"Player {self.winner()} won!")
    else:
      print("Cat's game!")
      