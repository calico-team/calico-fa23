def solve(A: int, B: int) -> int:
    '''
    Implements addition like a preschooler, which exceeds the time limit.
    '''
    total = 0
    for i in range(A):
        total += 1
    for j in range(B):
        total += 1
    return total


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A, B = int(temp[0]), int(temp[1])
        print(solve(A, B))


if __name__ == '__main__':
    main()
