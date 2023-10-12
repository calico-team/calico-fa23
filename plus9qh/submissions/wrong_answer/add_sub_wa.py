def solve(A: int, B: int) -> int:
    '''
    Implements subtraction instead of addition, which gives a wrong answer.
    '''
    return A - B


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A, B = int(temp[0]), int(temp[1])
        print(solve(A, B))


if __name__ == '__main__':
    main()
