class Board:
  
  def __init__(self, cells=[" ", " ", " ", " ", " ", " ", " ", " ", " "]):
    self.cells = cells

  def display(self):
    print(f" { self.cells[0] } | { self.cells[1]} | { self.cells[2] }")
    print("-----------")
    print(f" { self.cells[3] } | { self.cells[4]} | { self.cells[5] }")
    print("-----------")
    print(f" { self.cells[6] } | { self.cells[7]} | { self.cells[8] }")

  def position_taken(self, index):
    return self.cells[index] != " "

  def update(self, token, index):
    self.cells[index] = token

  def full(self):
    return self.cells.count(" ") == 0
