import homework1_mhanifsaleh as homework

if __name__ == "__main__":
    l1 = []
    l2 = []
    for n in range(1, 5):
       print(f"n = {n}, and num_sq = {n*n} num_placements_all = {homework.num_placements_all(n)}")
       l1.append(homework.num_placements_all(n))
       print(f"n = {n}, and num_sq = {n*n} num_placements_one_per_row = {homework.num_placements_one_per_row(n)}")
       l2.append(homework.num_placements_one_per_row(n))

    print("l1 = ", l1)
    print("l2 = ", l2)
    print("Testing is done!")
    
    board = [[0,0], [0, 1],
             [1, 0], [0,2],
             [1, 1], [0,3],
             [1, 2], [1,3],
             [0,3,1]]
    print("The tests on the board will be = ", board)
    for i in board:
        is_valid = homework.n_queens_valid(i)
        if is_valid:
            print("the Board looks like= ", i, "it is VALID")
        else:
            print("the Board looks like=", i, "it is NOT valid")

    print("The final function sol is = ", list(homework.n_queens_solutions(4)))
    print("The final function sol is = ", len(list(homework.n_queens_solutions(8))))

    b = [[True, False],[False, True]]
    print("p = LightsOutpuzzle(b) is called here")
    p = homework.LightsOutPuzzle(b)
    print("The board looks like = ", p.get_board())
    p = [[True, True],[True, True]]
    print("p = LightsOutpuzzle(p) is called here ", p)
    print("The board b still looks like ", b)

    print("create and perform move #1")
    p = homework.create_puzzle(3, 3)
    print("The board looks like(create_puzzle) = ", p.get_board())
    p.perform_move(1, 1)
    print("The board looks like(after changing it) = ", p.get_board())

    print("create and perform move #2")
    j = homework.create_puzzle(3, 3)
    print("The board looks like(create_puzzle) = ", j.get_board())
    j.perform_move(0, 0)
    print("The board looks like(after changing it) = ", j.get_board())

    print("50%' chance to turn on the light or off")
    z = homework.create_puzzle(3, 3)
    print("The board looks like(create_puzzle) = ", z.get_board())
    z.scramble()
    print("answer for scramble = ", z.get_board())

    print("test of the is_solved function #1")
    w = homework.LightsOutPuzzle([[True,False],[False,True]])
    print("The board looks like = ", w.get_board())
    answer = w.is_solved()
    print("The answer for is_solved = ", answer)

    print("test of the is_solved function #2")
    w = homework.LightsOutPuzzle([[False,False],[False,False]])
    print("The board looks like = ", w.get_board())
    answer = w.is_solved()
    print("The answer for is_solved = ", answer)


    print("test of the copy function #1")
    i = homework.create_puzzle(3, 3)
    i2 = i.copy()
    print("are i and i2 the same: ", i.get_board() == i2.get_board())

    print("test of the copy function #2")
    k = homework.create_puzzle(3, 3)
    k2 = i.copy()
    k.perform_move(1, 1)
    print("are k and k2 the same: ", k.get_board() == k2.get_board())

    print("successors function test#1")
    o = homework.create_puzzle(2, 2)
    for move, new_p in o.successors():
        print("move = ", move, "new_board = ", new_p.get_board())

    print("solver function test#1")
    p = homework.create_puzzle(2, 3)
    for row in range(2):
        for col in range(3):
            p.perform_move(row, col)
    print("The board looks like = ", p.get_board())
    print("The answer for solver = ", p.find_solution())

    print("solver function test#2")
    h = [[False,False,False],[False,False,False]]
    k = homework.LightsOutPuzzle(h)
    print("The board looks like = ", k.get_board())
    print("The answer for solver = ", k.find_solution() is None)

    print("solve_identical_disks function test#1")
    print("answer for the disk (4,2) is:", homework.solve_identical_disks(4,2))
    print("solve_identical_disks function test#2")
    print("answer for the disk (5,2) is:", homework.solve_identical_disks(5,2))
    print("solve_identical_disks function test#3")
    print("answer for the disk (4,3) is:", homework.solve_identical_disks(4,3))
    print("solve_identical_disks function test#4")
    print("answer for the disk (5,6) is:", homework.solve_identical_disks(5,3))


    print("solve_distinct_disks function test#1")
    print("answer for the disk (4,2) is:", homework.solve_distinct_disks(4,2))
    print("solve_distinct_disks function test#2")
    print("answer for the disk (5,2) is:", homework.solve_distinct_disks(5,2))
    print("solve_distinct_disks function test#3")
    print("answer for the disk (4,3) is:", homework.solve_distinct_disks(4,3))
    print("solve_distinct_disks function test#4")
    print("answer for the disk (5,6) is:", homework.solve_distinct_disks(5,3))