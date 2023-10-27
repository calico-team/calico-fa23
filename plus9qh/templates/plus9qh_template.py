def solve(N: int, X: list[str]) -> str:
    """
    Find an HQ9+ program that outputs exactly the given text or return
    IMPOSSIBLE if no solutions exist.

    N: the number of lines of text
    X: a list containing the lines of the text
    """
    # YOUR CODE HERE
    return ''


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = [input() for _ in range(N)]
        print(solve(N, X))


if __name__ == '__main__':
    main()
