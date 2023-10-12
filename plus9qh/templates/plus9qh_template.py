def solve(N: int, M: int, X: list[int], Y: list[int], Z: list[int]):
    """
    Output a program that outputs the given text.

    T: the number of Test Cases
    N: the number of lines in the program
    X: the list of lines of the program
    """
    # YOUR CODE HERE
    return


def main():
    T = int(input())
    for _ in range(T):
        info = input().strip().split(' ')
        N = int(info[0])
        X  = []
        for i in range(N):
            info = input().strip().split(' ')
            X.append(int(info[0]))
        solve(N, X)


if __name__ == '__main__':
    main()
