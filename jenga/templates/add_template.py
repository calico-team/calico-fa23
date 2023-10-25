def solve(N: int) -> int:
    """
    Return the number of different Jenga tower that can be built using N bricks

    N: number of bricks that can be used
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A, B = int(temp[0]), int(temp[1])
        print(solve(A, B))

if __name__ == '__main__':
    main()
