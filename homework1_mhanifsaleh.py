############################################################
# ECS170: Uninformed Search
############################################################

student_name = "Mohammad Ayub Hanif Saleh"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random
import collections


############################################################
# Section 1: N-Queens
############################################################

# I think this is a n^2 board with n queens on it so if we think that there is no difference between the queens
# And order does not matter then we can call this problem a combination problem.
# The equation for Combination then we know is comb(n,k) = n!/(k!(n-k)!)
# And we know that k is the number of queens and n is the number of squares in the board.
def num_placements_all(n):
    # we can set the number of squares to be n*n.
    # num_sq! / (n! (num_sq‑n)!)
    num_sq = n*n
    answer = math.factorial(num_sq) / (math.factorial(n) * math.factorial(num_sq - n))
    #using the math lib we can use the math.comb which I found using the W3Schools when searching for the combination formula in python.
    #but when I was doing the lights out problem I was getting 0.5 less then I looked at the discussion and I found that they want me to use factorial.
    #so I just made equation using that and used it.
    return int(answer)

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
        eq_probab = random.random() < 0.5

        #I think we have to go through each row and column and flip the lights.
        for row in range(self.rows):
            for col in range(self.cols):
                if eq_probab: #using the 50% chance to turn on the light or off.
                    self.perform_move(row, col) #change the light.


    def is_solved(self):
        #if the every light is off then we just return true.
        #otherwise we return false
        #The easiest way I think is that checking the light is off or not.
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col]: #is it on?
                    return False
        return True #didn't find any light.

    def copy(self):
        board_temp = self.get_board() #I will copy it and then return it as a new object.
        return LightsOutPuzzle(board_temp)

    # we move it by row and col and then we make a new object and return it.
    #I think a good way and easy would be to just make a copy for every row and col that we move.
    #And then we can just return the new object.
    def successors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                new_board = self.copy()
                new_board.perform_move(row, col)
                yield ((row, col), new_board) # so if we have move (1,1) then we will return the new board with the move.
        

    def find_solution(self):

        if(self.is_solved()):
            return []
        else:
            queue = collections.deque()
            queue.append((self.copy(), []))
            begin = tuple(tuple(row) for row in self.get_board()) #I think we need to keep track of the visited.
            visited = {begin}

            while queue:
                current, moves = queue.popleft() #pop the left side of the queue.

                for move, new_puzzle in current.successors(): #get the successors of the current board.
                    new_visited = tuple(tuple(row) for row in new_puzzle.get_board()) #track of the visited.
                    if new_visited in visited: #we check if we have already visited this board.
                        continue
                    visited.add(new_visited)
                    new_moves = moves + [move] #we make a new move and add it to the list.

                    if new_puzzle.is_solved():
                        return new_moves #we found the solution.
                    
                    queue.append((new_puzzle, new_moves))

            return None


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

# First I think we need to sorted indices of the disks.
def solve_identical_disks(length, n):

    first = tuple(range(n))
    finished = tuple(range(length-n, length))

    #then I want to make sure we have the BFS 
    queue = collections.deque()
    queue.append((first, []))
    visited = {first}

    while queue:
        current, moves = queue.popleft()
        if current == finished:
            return moves
        #I made this to check for membership.
        taken = set(current)

        #name the jumps to make it easier for coding logic
        jump_one_left = -1
        jump_one_right = 1
        jump_two_left = -2
        jump_two_right = 2 

        #lets check for each disk and see if moving it can work.
        for index in range(len(current)):
            pos = current[index]
            #checking for moving it to the left or right.
            for i in (jump_two_right, jump_two_left, jump_one_right, jump_one_left):
                cell = pos + i
                #checking for conditions of the cell.
                if cell in taken:
                    continue
                if not (0 <= cell < length):
                    continue
                if abs(i) == jump_two_right:
                    middle = (pos + cell) // 2
                    if middle not in taken:
                        continue
                
                #it is a valid move so we can add it to the queue.
                new_current = list(current)
                new_current[index] = cell
                #sort the new current for right order.
                new_current.sort()
                new_current = tuple(new_current)
                #checking for visited cells.
                if new_current in visited:
                    continue
                visited.add(new_current)
                #add the new current to the queue.
                queue.append((new_current, moves + [(pos, cell)]))
    #return none since we can't find a solution.
    return None


#for this function I just copied the same code as the last one but with some changes.
#I noticed we don't need to sort the disk.
#it is reversed finished tuple.
def solve_distinct_disks(length, n):
    first = tuple(range(n))
    temp_finished = []
    for i in range(n):
        cell = length - 1 - i
        temp_finished.append(cell)
    finished = tuple(temp_finished)

    #then I want to make sure we have the BFS 
    queue = collections.deque()
    queue.append((first, []))
    visited = {first}

    while queue:
        current, moves = queue.popleft()
        if current == finished:
            return moves
        #I made this to check for membership.
        taken = set(current)

        #name the jumps to make it easier for coding logic
        jump_one_left = -1
        jump_one_right = 1
        jump_two_left = -2
        jump_two_right = 2 

        #lets check for each disk and see if moving it can work.
        for index in range(len(current)):
            pos = current[index]
            #checking for moving it to the left or right.
            for i in (jump_two_right, jump_two_left, jump_one_right, jump_one_left):
                cell = pos + i
                #checking for conditions of the cell.
                if cell in taken:
                    continue
                if not (0 <= cell < length):
                    continue
                if abs(i) == jump_two_right:
                    middle = (pos + cell) // 2
                    if middle not in taken:
                        continue
                
                #it is a valid move so we can add it to the queue.
                new_current = list(current)
                new_current[index] = cell
                #sort the new current for right order.
                new_current = tuple(new_current)
                #checking for visited cells.
                if new_current not in visited:
                    visited.add(new_current)
                    #add the new current to the queue.
                    queue.append((new_current, moves + [(pos, cell)]))
    #return none since we can't find a solution.
    return None