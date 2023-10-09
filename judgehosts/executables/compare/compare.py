import sys
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

cnt_fixed = lambda perm: sum(j + 1 == p for j, p in enumerate(perm))


# CHECK THIS, IT WAS MADE WITH CHATGPT THANK YOU JAMES FOR THE IDEA <33333

def dfs(u, g, visited):
    visited[u] = True
    if not g[u]:
        return True  # is a sink
    for v in g[u]:
        if not visited[v]:
            dfs(v, g, visited)

def flow(N, M, S, U, V, eaten):
    sources = [True] * (N + 1)
    visited = [False] * (N + 1)
    g = [[] for _ in range(N + 1)]
    for i in range(M):
        g[U[i]].append(V[i])
        sources[V[i]] = False
    for i in eaten:
        visited[i] = True
    for i in range(1, N + 1):
        if sources[i] and not visited[i]:
            if dfs(i, g, visited):
                return True
    return False

def calc_sources(U, V, N):
    sources = set([i for i in range(1, N + 1)])
    for i in V :
        sources.discard(i)
    return sources


def calc_sinks(U, V, N):
    sinks = set([i for i in range(1, N + 1)])
    for i in U :
        sinks.discard(i)
    return sinks

def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):

        # READ INPUT FROM INPUT FILE
        N, M, S = tuple([int(x) for x in read_file(test_in).split(' ')])
        U, V = [], []
        for i in range(M) :
            ui, vi = tuple([int(x) for x in read_file(test_in).split(' ')])
            U.append(ui)
            V.append(vi)

        contestants = calc_sources(U, V,N)
        judgehosts = calc_sinks(U, V, N)
        
        # READ REFERENCE SOLUTION

        ref_str = read_file(test_out).split(' ')

        # Check that the first line does not have more than 1 element
        if len(ref_str) > 1 :
            print(f'Test #{case}: [Reference] The first line of output contains the wrong number of elements (more than one).'
                    'The reference output is wrong.',
                    f'Item: {ref_str}')
            exit(1)
        
        # Check that the element makes sense
        if not (ref_str[0].isdigit() or ref_str[0] == "IMPOSSIBLE") :
            print(f'Test #{case}: [Reference] The first line of output contains a wrong element (NaN nor IMPOSSIBLE).'
                    'The reference output is wrong.',
                    f'Item: {ref_str}')
            exit(1)

        ref_impossible = not ref_str[0].isdigit()

        if not ref_impossible :
            # Read computers eaten by Bessie
            computers_eaten_ref = int(ref_str[0])

            # Check if Bessie ate more computers than stomachs
            if computers_eaten_ref > S :
                print(f'Test #{case}: [Reference] Bessie eats more than S computers.'
                        'The reference output is wrong.',
                        f'Item: {computers_eaten_ref}')
                exit(1)

            ref_computers_str = ''.join(read_file(test_out).split(' '))

            # Check that the length of the computer list given is the same as the computers given before
            if len(ref_computers_str) != computers_eaten_ref :
                print(f'Test #{case}: [Reference] The length of the list of computers eaten does not match the number given.'
                    'The reference output is wrong.',
                    f'Item: {ref_computers_str}')
                exit(1)

            # Check that they are numbers lol
            for x in ref_computers_str :
                if not x.isdigit() :
                    print(f'Test #{case}: [Reference] One of the elements of the computers list is not valid (NaN).'
                        'The reference output is wrong.',
                        f'Item: {x}')
                    exit(1)
            
            ref_computers = [int(x) for x in ref_computers_str]

            # Check that the numbers given are in range
            for x in ref_computers :
                if x <= 0 or x > N :
                    print(f'Test #{case}: [Reference] One of the elements of the computers list is not valid (The index is out of bounds).'
                        'The reference output is wrong.',
                        f'Item: {x}')
                    exit(1)
                elif x in contestants:
                    print(f'Test #{case}: [Reference] One of the elements of the computers list is not valid (It is a contestant).'
                        'The reference output is wrong.',
                        f'Item: {x}')
                    exit(1)
                elif x in judgehosts:
                    print(f'Test #{case}: [Reference] One of the elements of the computers list is not valid (It is a judgehost).'
                        'The reference output is wrong.',
                        f'Item: {x}')
                    exit(1)

            
            # Check that the solution given is correct
            if flow(N, M, S, U, V, ref_computers) :
                print(f'Test #{case}: [Reference] One of the submissions still gets judged by one of the judgehosts.'
                    'The reference output is wrong.',
                    f'Item: {flow(N, M, S, U, V, ref_computers)}')
                exit(1)

            
        # Read submitted solution

        sub_str = read().split(' ')
        # Check that the first line does not have more than 1 element
        if len(sub_str) > 1 :
            print(f'Test #{case}: [Submission] The first line of output contains the wrong number of elements (more than one).')
            continue
        
        # Check that the element makes sense
        if not (sub_str[0].isdigit() or sub_str[0] == "IMPOSSIBLE") :
            print(f'Test #{case}: [Submission] The first line of output contains a wrong element (NaN nor IMPOSSIBLE).')
            continue

        sub_impossible = not sub_str[0].isdigit()

        if not sub_impossible :
            # Read computers eaten by Bessie
            computers_eaten_sub = int(sub_str[0])

            # Check if Bessie ate more computers than stomachs
            if computers_eaten_sub > S :
                print(f'Test #{case}: [Submission] Bessie eats more than S computers.')
                continue

            sub_computers_str = ''.join(read().split(' '))

            # Check that the length of the computer list given is the same as the computers given before
            if len(sub_computers_str) != S :
                print(f'Test #{case}: [Submission] The length of the list of computers eaten does not match the number given.')
                continue

            # Check that they are numbers lol
            okay = True
            for x in sub_computers_str :
                if not x.isdigit() :
                    print(f'Test #{case}: [Submission] One of the elements of the computers list is not valid (NaN).')
                    okay = False

            if not okay :
                continue
            
            sub_computers = [int(x) for x in sub_computers_str]

            # Check that the numbers given are in range
            for x in sub_computers :
                if x <= 0 or x > N :
                    print(f'Test #{case}: [Submission] One of the elements of the computers list is not valid (The index is out of bounds).')
                    okay = False
                elif x in contestants:
                    print(f'Test #{case}: [Submission] One of the elements of the computers list is not valid (It is a contestant).')
                    okay = False
                elif x in judgehosts:
                    print(f'Test #{case}: [Submission] One of the elements of the computers list is not valid (It is a judgehost).')
                    okay = False


            if not okay :
                continue
            
            # Check that the solution given is correct
            if flow(N, M, S, U, V, sub_computers) :
                print(f'Test #{case}: [Submission] One of the submissions still gets judged by one of the judgehosts.')
                continue


        if sub_impossible and not ref_impossible :
            print(f'Test #{case}: [Submission] The solution given states that it is IMPOSSIBLE, but it is actually possible.')
            continue

        if ref_impossible and not sub_impossible :
            print(f'Test #{case}: [Reference] The solution given states that it is IMPOSSIBLE, but it is actually possible.'
                'The reference output is wrong. THIS IS A MAJOR ERROR. CANCEL CALICO AFTER THIS.',
                f'Item: {x}')
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