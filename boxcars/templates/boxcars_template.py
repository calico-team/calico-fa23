def solve(S: list[int]):
    """
    Output two lines containing the sides of the dice separated by dashes -,\
    such that the two dice yield the given sum distribution S.
    
    S: a list containing the possible 36 sums achieved rolling the two unknown die.
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
