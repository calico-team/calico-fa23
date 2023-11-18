def solve(N: int) -> int:
    numDays = 0
    for i in range(1, N + 1):
        numDays += i * i
    return numDays - N

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
