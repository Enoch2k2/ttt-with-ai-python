import os
import pdb
from board import Board
from game import Game
from players.computer import Computer
from players.human import Human

class Cli:
  def __init__(self):
    self.welcome()
    self.options()

  def welcome(self):
    self.clear()
    print("Welcome to Tic Tac Toe!")

  def options(self):
    self.print_options()
    user_input = input("User Input: ")
    self.clear()
    if(self.valid_option(user_input)):
      if(user_input == "4"):
        self.goodbye()
        return False
      self.game_mode(user_input)
    else:
      self.invalid_message()
      self.options()
    
  def print_options(self):
    print("")
    print("Which mode would you like?")
    print("1. 2 Player")
    print("2. 1 Player")
    print("3. 0 Player")
    print("4. to exit program")

  def valid_option(self, user_input):
    if(user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4"):
      return True
    else:
      return False

  def game_mode(self, user_input):
    if(user_input == "1"):
      self.two_player_game()
    elif(user_input == "2"):
      self.one_player_game()
    elif(user_input == "3"):
      self.zero_player_game()
  
  def two_player_game(self):
    player_1 = Human("X")
    player_2 = Human("O")
    board = Board()
    Game(player_1, player_2, board)
  
  def one_player_game(self):
    player_1 = Human("X")
    player_2 = Computer("O")
    board = Board()
    Game(player_1, player_2, board)

  def zero_player_game(self):
    player_1 = Computer("X")
    player_2 = Computer("O")
    board = Board()
    Game(player_1, player_2, board)

  def invalid_message(self):
    print("You typed something incorrect, please try again.")
  
  def goodbye(self):
    print("Terminating Game and shutting down...")

  def clear(self):
    os.system("clear")