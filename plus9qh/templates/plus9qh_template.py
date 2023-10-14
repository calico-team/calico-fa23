def solve(N: int, X: list[str]):
    """
    Find an HQ9+ program that exactly outputs the given text.

    N: the number of lines in the text
    X: a list containing the lines of the text
    """
    # YOUR CODE HERE
    return


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = [input() for _ in range(N)]
        solve(N, X)


if __name__ == '__main__':
    main()
