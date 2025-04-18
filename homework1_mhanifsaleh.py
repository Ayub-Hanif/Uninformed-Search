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

def n_queens_solutions(n):
    pass

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

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
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

