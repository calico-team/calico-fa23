def solve(N: int) -> int:
    """
    Return the number of unique Jenga towers that can be built using N or fewer
    bricks. Give your answer modulo 3359232.
    
    N: the maximum number of bricks to use
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()