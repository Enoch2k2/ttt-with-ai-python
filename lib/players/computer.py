import pdb
import random
from game import Game
from player import Player

class Computer(Player):
    def __init__(self, token):
      super().__init__(token)
      self.opp_token = "X" if token == "O" else "O"

    def move(self, board):
      if self.win_move(board):
        return self.win_move(board)
      elif self.defence_move(board):
        return self.defence_move(board)
      else:
        return self.random_move(board)

    def win_move(self, board):
      for idx, win_combo in enumerate(Game.WIN_COMBO):
        combo_1 = board.cells[win_combo[0]]
        combo_2 = board.cells[win_combo[1]]
        combo_3 = board.cells[win_combo[2]]

        if(self.check_for_move(combo_1, combo_2, combo_3, self.token)):
          return str(win_combo[2] + 1)
        elif(self.check_for_move(combo_2, combo_3, combo_1, self.token)):
          return str(win_combo[0] + 1)
        elif(self.check_for_move(combo_3, combo_1, combo_2, self.token)):
          return str(win_combo[1] + 1)
    
    def defence_move(self, board):
      for idx, win_combo in enumerate(Game.WIN_COMBO):
        combo_1 = board.cells[win_combo[0]]
        combo_2 = board.cells[win_combo[1]]
        combo_3 = board.cells[win_combo[2]]

        if(self.check_for_move(combo_1, combo_2, combo_3, self.opp_token)):
          return str(win_combo[2] + 1)
        elif(self.check_for_move(combo_2, combo_3, combo_1, self.opp_token)):
          return str(win_combo[0] + 1)
        elif(self.check_for_move(combo_3, combo_1, combo_2, self.opp_token)):
          return str(win_combo[1] + 1)

    def check_for_move(self, cell_1, cell_2, cell_3, token):
      return cell_1 == token and cell_2 == token and cell_3 == " "

    def random_move(self, board):
      l = []
      for idx, x in enumerate(board.cells):
        if x == " ":
          l.append(idx)

      return str(random.choice(l) + 1)