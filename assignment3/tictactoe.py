class TictactoeException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__()


class Board:
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
    
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    
    def __str__(self):
        str_board = ""
        for i in range(len(self.board_array)):
            k = 0
            for k in range(len(self.board_array[k])):
                str_board = str_board + "—-"
            str_board = str_board + "\n"
            for j in range(len(self.board_array[i])):
                str_board = str_board + "|" + self.board_array[i][j]
            str_board = str_board + "|\n"
        for _ in range(len(self.board_array)):
            str_board = str_board + "—-"
        return str_board
    
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 # row
        column = move_index % 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")            
board = Board()

try:
    result = board.whats_next()
    while not result[0]:
        move = input(f"{board.turn}'s turn:")
        board.move(move)
        result = board.whats_next()
        print(board)
    print(f"Game over: {result[1]}")
except TictactoeException as e:
    print(f"Error: {e.message}")

# "upper left", "upper center", "upper right", 
# "middle left", "center", "middle right", 
# "lower left", "lower center", "lower right"
