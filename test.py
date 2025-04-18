import homework1_mhanifsaleh as homework

if __name__ == "__main__":
    for n in range(1, 5):
        print(f"n = {n}, and num_sq = {n*n} num_placements_all = {homework.num_placements_all(n)}")
    
    print("Testing is done!")