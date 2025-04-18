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


