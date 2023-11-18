import sys


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


def check_case(is_reference, values, test_out, case):
    # Read first line of output
    first_line = read_file(test_out).split() if is_reference else read().split()

    # If the first line is impossible then we don't read anything else
    if len(first_line) == 1 and first_line[0] == 'IMPOSSIBLE':
        return False

    # Read the second line
    second_line = read_file(test_out).split() if is_reference else read().split()

    # Check that the first line is correct
    if len(first_line) != 6:
        print(f'Test #{case}: [Reference? {is_reference}] : The first line contains more than 6 elements',
              f'{first_line}',
              f'{len(first_line)}')
        if is_reference:
            exit(1)
        else:
            return False

    for x in first_line:
        if not x.isdigit():
            print(f'Test #{case}: [Reference? {is_reference}] : An element on the first line is not a number',
                  f'{first_line}',
                  f'{x}')
            if is_reference:
                exit(1)
            else:
                return False

    d1 = [int(x) for x in first_line]

    # Check that the second line is correct
    if len(second_line) != 6:
        print(f'Test #{case}: [Reference? {is_reference}] : The second line contains more than 6 elements',
              f'{second_line}',
              f'{len(second_line)}')
        if is_reference:
            exit(1)
        else:
            return False

    for x in second_line:
        if not x.isdigit():
            print(f'Test #{case}: [Reference? {is_reference}] : An element on the second line is not a number',
                  f'{second_line}',
                  f'{x}')
            if is_reference:
                exit(1)
            else:
                return False

    d2 = [int(x) for x in second_line]

    # Build the distribution
    distribution = sorted(a + b for a in d1 for b in d2)

    # Check that the distributions match
    if values != distribution:
        print(f'Test #{case}: [Reference? {is_reference}] : The distributions do not match',
              f'{values}',
              f'{distribution}',
              f'{d1}',
              f'{d2}')
        if is_reference:
            exit(1)
        else:
            return False

    return True


def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):

        # Read input from input file
        values = [int(x) for x in read_file(test_in).split()]
        reference_possible = check_case(True, values[:], test_out, case)
        contestant_possible = check_case(False, values[:], test_out, case)

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
