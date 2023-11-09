def solve(S: list[int]):
    """
    Output two lines containing the faces of the dice separated by spaces,
    such that the sorted list of their pairwise sums is equal to S.
    
    S: the list containing the desired nondecreasing list of 36 pairwise sums
    """
    # YOUR CODE HERE
    return


def main():
    T = int(input())
    for _ in range(T):
        S = [int(x) for x in input().split()]
        solve(S)

if __name__ == '__main__':
    main()
