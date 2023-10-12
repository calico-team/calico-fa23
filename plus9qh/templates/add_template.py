def solve(A: int, B: int) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
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
