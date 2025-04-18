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

