from player import Player

class Human(Player):
  def __init__(self, token):
    super().__init__(token)

  def move(self, index, board):
    board.update(self.token, index)