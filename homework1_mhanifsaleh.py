############################################################
# ECS170: Uninformed Search
############################################################

student_name = "Mohammad Ayub Hanif Saleh"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math



############################################################
# Section 1: N-Queens
############################################################

# I think this is a n^2 board with n queens on it so if we think that there is no difference between the queens
# And order does not matter then we can call this problem a combination problem.
# The equation for Combination then we know is comb(n,k) = n!/(k!(n-k)!)
# And we know that k is the number of queens and n is the number of squares in the board.
def num_placements_all(n):
    # we can set the number of squares to be n*n.
    num_sq = n*n
    #using the math lib we can use the math.comb which I found using the W3Schools when searching for the combination formula in python.
    return math.comb(num_sq, n)

# Now using the same thing but with the condition that each row contains only one queen.
# Then we can say that for each row have a queen so if we have n different squares.
# Then we can also say that the number of placements is n^n or in python pow(n,n) using Greeksforgeeks.
def num_placements_one_per_row(n):
    return pow(n, n)

#lets say that we have a board with 2 numbers given thus then we need to make sure that the queens are not in the same column.
#but I also see that we need to return true or false depending on the board and queen.
#I am assuiming that the board values means as such = "row, col" so if I have [0,2] then thats row 0 and column 0, row 1 and column 2 which will be true.
#so we can't have same column or diagonal or opposite diagonal.
def n_queens_valid(board):

    for i in range(len(board)):
        for z in range(i+1, len(board)):
            #we can check the [0,2] if its same column by doing 0 == 2?? we go on otherwise if its [1,1] 1==1 then it is false.
            if board[i] == board[z]:
                return False
            
            #for [0,2] else if same diagonal then we get the abs(0-1) == abs(0-2) we go on because it is valid.
            #abs(i-z) will do the vertical test by keeping the size only and we don't care about the sign.
            #and abs(board[i]- board[z]) will do the horizontal test and the same thing for abs. 
            if abs(i-z) == abs(board[i]- board[z]):
                return False
    #otherwise I think we are good and nothing is in same column or diagonal.
    return True

def n_queens_helper(board, n):

    #we need the solution from the function and also it should stop exploring after.
    #bascially this is our base case bc otherwise it kept going on.
    if len(board) == n:
        yield board
        return

    #I think we need to try and check until we find the correct placement and to do that we need to try each row.
    for try_col in range(n):
        if try_col not in board: #I check the column if there is no queen in the column we can place the queen.
            new_board = board + [try_col] #then I add the queen to the new board.
            if n_queens_valid(new_board): #I check if the board is still valid or not.
                yield from n_queens_helper(new_board, n) #then I will yield the new board and call the function again until I hit the base case.

#I think the easiest way is the hint way of need get all the possible valid placements of the queens by yielding the board.
def n_queens_solutions(n):
    yield from n_queens_helper([], n)

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    # For the constructor I think we just need to copy the board 
    # and keep it so outside functions can't change it and it will initialize the board.
    def __init__(self, board):
        #making sure we don't change the original board once we are making changes on the other functions.
        temp_board = []
        for row in board:
            temp_row = [] #making new row everytime.
            for col in row: #we take the T or F and copy it to the new row.
                temp_row.append(col)
            temp_board.append(temp_row) #once we finished row we just add it. 
        self.board = temp_board #now we will give it back to the object and store it.

        if len(board) != 0:
            self.rows = len(board)
            self.cols = len(board[0]) #we take the num of cols
        else:
            self.rows = 0
            self.cols = 0

    def get_board(self):
        #we want to get the board when ask for it so lets make a copy of it.
        #and return it so if in any way I by mistakenly change something I won't lose stuff.
        #I will just make a copy of it and return the board.
        board_temp = []
        for row in self.board:
            temp_row = []
            for col in row:
                temp_row.append(col)
            board_temp.append(temp_row)
        return board_temp

    def perform_move(self, row, col):
        # WE can toggle light on or off by using the not operator.

        #the cell we want to change.
        if (0 <= col < self.cols) and (0 <= row < self.rows):
            self.board[row][col] = not self.board[row][col]
        
        #exact nighbour above us.
        if (0<=(row-1) < self.rows):
            self.board[row-1][col] = not self.board[row-1][col]
        
        #exact nighbour below us.
        if (0<=(row+1) < self.rows):
            self.board[row+1][col] = not self.board[row+1][col]
        
        #exact nighbour to the left of us.
        if (0<=(col-1) < self.cols):
            self.board[row][col-1] = not self.board[row][col-1]
        
        #exact nighbour to the right of us.
        if (0<=(col+1) < self.cols):
            self.board[row][col+1] = not self.board[row][col+1]

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    #Making sure all the lights are off.
    board = []
    for row in range(rows):
        temp_row = []
        for col in range(cols):
            temp_row.append(False) #I put the light False so it is off.
        board.append(temp_row) #Added the finished row back.

    return LightsOutPuzzle(board)

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

