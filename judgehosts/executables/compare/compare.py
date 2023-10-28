import sys
from collections import deque
from itertools import groupby


def main():
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
        exit(1)
    _, test_in_path, test_out_path = sys.argv

    try:
        with open(test_in_path, 'r') as test_in:
            with open(test_out_path, 'r') as test_out:
                compare(test_in, test_out)
    except IOError:
        print('Failed to open test input')
        exit(1)


def check_case(is_reference, is_contestant, is_judgehost, g, N, S, test_out, case):

    # Read first line of input
    first_line = read_file(test_out).split() if is_reference else read().split()

    # Check that it only has one element
    if len(first_line) != 1:
        print(f'Test #{case}: [Reference? {is_reference}] : The first line contains more than one element',
              f'{first_line}',
              f'{len(first_line)}')
        if is_reference:
            exit(1)
        else:
            return False

    # Check that the element is correct
    if not (first_line[0].isdigit() or first_line[0] == 'IMPOSSIBLE'):
        print(f'Test #{case}: [Reference? {is_reference}] : The first line contains a wrong element',
              f'{first_line[0]}')
        if is_reference:
            exit(1)
        else:
            return False

    possible = first_line[0].isdigit()

    # Finish reading input
    if not possible:
        return False

    # Read next line containing computers
    eaten = read_file(test_out).split() if is_reference else read().split()

    _S = int(first_line[0])

    if _S > S:
        print(f'Test #{case}: [Reference? {is_reference}] : Try to eat more than S computers',
              f'{first_line}')
        if is_reference:
            exit(1)
        else:
            return False

    if len(eaten) != _S:
        print(f'Test #{case}: [Reference? {is_reference}] : More computers eaten than stated',
              f'S = {_S}',
              f'eaten = {eaten}')
        if is_reference:
            exit(1)
        else:
            return False

    for u in eaten:
        if not u.isdigit():
            print(f'Test #{case}: [Reference? {is_reference}] : One of the computers eaten is not a positive integer',
                  f'{u}')
            if is_reference:
                exit(1)
            else:
                return False

    eaten = [int(u) for u in eaten]
    is_eaten = [False] * (N + 1)

    for u in eaten:
        if u <= 0 or u > N:
            print(f'Test #{case}: [Reference? {is_reference}] : Computer eaten out of bounds',
                  f'N = {N}',
                  f'u = {u}')
            if is_reference:
                exit(1)
            else:
                return False
        elif is_contestant[u]:
            print(f'Test #{case}: [Reference? {is_reference}] : Tried to eat a contestant',
                  f'u = {u}',
                  f'eaten = {eaten}')
            if is_reference:
                exit(1)
            else:
                return False
        elif is_judgehost[u]:
            print(f'Test #{case}: [Reference? {is_reference}] : Tried to eat a judgehost',
                  f'u = {u}',
                  f'eaten = {eaten}')
            if is_reference:
                exit(1)
            else:
                return False
        else:
            is_eaten[u] = True

    q = deque()
    for i in range(1, N + 1):
        if is_contestant[i]:
            q.append(i)

    while q:
        u = q.popleft()
        for v in g[u]:
            if not is_contestant[v] and not is_eaten[u]:
                q.append(v)
                is_contestant[v] = True

    for i in range(1, N + 1):
        if is_contestant[i] and is_judgehost[i]:
            print(f'Test #{case}: [Reference? {is_reference}] : A submission reaches a judgehost',
                  f'u = {i}')
            if is_reference:
                exit(1)
            else:
                return False

    return True


def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):

        # Read input from input file
        N, M, S = tuple([int(x) for x in read_file(test_in).split()])
        U, V = [], []
        for i in range(M):
            ui, vi = tuple([int(x) for x in read_file(test_in).split()])
            U.append(ui)
            V.append(vi)

        # Test case logic (build the graph)
        is_contestant = [True] * (N + 1)
        is_judgehost = [True] * (N + 1)
        g = [[] for _ in range(N + 1)]
        for u, v in zip(U, V):
            g[u].append(v)
            is_judgehost[u] = False
            is_contestant[v] = False

        reference_possible = check_case(True, is_contestant[:], is_judgehost[:], g, N, S, test_out, case)
        contestant_possible = check_case(False, is_contestant[:], is_judgehost[:], g, N, S, test_out, case)

        if reference_possible and not contestant_possible:
            print(f'Test #{case}: [Reference? False] : Contestant says its impossible but its possible')
        elif not reference_possible and contestant_possible:
            print(f'Test #{case}: [Reference? True] : Reference says its impossible but its possible',
                  'If this happens do not call Nacho he wont write a single python line anymore')
            exit(1)

    try:
        temp = ''
        while not temp:
            temp = input().strip()
        print('Trailing output when judge expected no more output')
    except:
        pass


def read_file(file):
    try:
        return file.readline().strip()
    except EOFError:
        print('End of test input while judge expected more input')
        exit(1)


def read():
    try:
        return input().strip()
    except EOFError:
        print('End of output while judge expected more output')
        exit()


if __name__ == '__main__':
    main()
