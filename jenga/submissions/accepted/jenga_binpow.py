def solve(A: int, B: int) -> int:
    '''
    Implements addition with Python's arbitary precision arithmetic.
    '''
    return A + B


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()
