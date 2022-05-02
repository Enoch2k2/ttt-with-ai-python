from player import Player

class Human(Player):
  def __init__(self, token):
    super().__init__(token)

  def move(self, board):
    return input("Type 1-9 to make a move: ")