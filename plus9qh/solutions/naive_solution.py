def solve(N: int, X: list[int]):
    """
    Output a program that outputs the given text.

    T: the number of Test Cases
    X: the list of lines of the program
    """
    program = ""
    h = "Hello, world!"
    for line in X:
        if 'Q' in line:
            result = line.split("Hello, world!")
            return result[0]
    for count, line in enumerate(X):
        if 'beer' in line:
            program += "9"
            X.remove(count)
            X.remove(count + 1)
            X.remove(count + 2)
        else:
            while line:
                if line[0:len(h)] == h:
                    program += "H"
                    line = line[len(h):]
    return program

def main():
    T = int(input())
    for _ in range(T):
        info = input().strip().split(' ')
        N = int(info[0])
        X  = []
        for i in range(N):
            info = input().strip().split(' ')
            X.append(int(info[0]))
        solve(N, X)

if __name__ == '__main__':
    main()
