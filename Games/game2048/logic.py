import random

class Game:
    def __init__(self, size =4):
        self.size = size
        self.score = 0
        self.board =  [[0 for i in range(self.size)] for i in range(self.size)] 
        self.spawn_tile()
        self.spawn_tile()

    def empty_cells(self):
        return [(r, c) for c in range(self.size) for r in range(self.size) if self.board[r][c] == 0]
    
    def spawn_tile(self):
        empty = self.empty_cells()
        if not empty:
            return 
        
        r, c = random.choice(empty)
        self.board[r][c] = 2 if random.random() < 0.6 else 4
        #print(self.board)
        
    
    def print_board(self):
        for r in self.board:
            print(r)
        print(f'Score: {self.score}')


    #### MOVEING TILES ####

    def compress(self, row):
        return [ i for i in row if i != 0 ]
    def merge(self,row):
        new_row = []
        skip = False

        for i in range(len(row)):
            if skip:
                skip = False
                continue 
            
            if i + 1 < len(row) and row[i] == row[i + 1]:
                new_value = row[i] * 2
                self.score += new_value
                new_row.append(new_value)
                skip = True
            else:
                new_row.append(row[i])

        return new_row
    
    def pad(self, row):
        return row + [0] * (self.size - len(row))
    
    def move_left(self):
        moved = False
        new_board = []

        for row in self.board:
            compressed_row = self.compress(row)
            merged_row = self.merge(compressed_row)
            padded_row = self.pad(merged_row)

            if padded_row != row:
                moved = True
            new_board.append(padded_row)
        
        self.board = new_board

        if moved: 
            self.spawn_tile()

    def can_move(self):
        if self.empty_cells():
            return True
        
        for r in range(self.size):
            for c in range(self.size):
                if c + 1 < self.size and self.board[r][c] == self.board[r][c + 1]:
                    return True
                if r + 1 < self.size and self.board[r][c] == self.board[r + 1][c]:
                    return True
                
        return False
    

    ### I AM THE SMARTEST GUY IN THE WORLD ###

    def reverse(self, board):
        return [row[::-1] for row in board]
    def transpose(self, board):
        return [list(row) for row in zip(*board)]
    
    def move_right(self):
        self.board = self.reverse(self.board)
        self.move_left()
        self.board = self.reverse(self.board)
    
    def move_up(self):
        self.board = self.transpose(self.board)
        self.move_left()
        self.board = self.transpose(self.board)

    def move_down(self):
        self.board = self.transpose(self.board)
        self.move_right()
        self.board = self.transpose(self.board)




    def is_game_over(self):
        return not self.can_move()
    def reset(self):
        self.score = 0
        self.board =  [[0] * self.size for _ in range(self.size)]
        self.spawn_tile()
        self.spawn_tile()
        



# debug 
#game = Game()
#game.spawn_tile()
#game.spawn_tile()
#game.print_board()
