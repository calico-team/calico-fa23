def solve(N: int) -> int:
    '''
    TODO: Change description
    '''
    return (pow(2, 1 + N // 3, 3359232) - 2) % 3359232


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()
