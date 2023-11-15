import itertools


def solve(S: list[int]):
    a, b = [1, 0, 0, 0, 0, 0], [S[0] - 1, 0, 0, 0, 0, 0]
    
    for s1i_idx in itertools.combinations(range(1, 31), 5):
        s1i_idx = set(s1i_idx)
        remaining = [S[i] for i in range(2, 36) if i not in s1i_idx]
        a[1:] = [S[i] - b[0] for i in s1i_idx]
        try:
            for i in range(1, 6):
                b[i] = remaining.pop(0) - a[0]
                for j in range(1, 6):
                    remaining.remove(b[i] + a[j])
            print(*a)
            print(*b)
            return
        except ValueError:
            pass
    
    print('IMPOSSIBLE')
    return


def pair_sums(d1, d2):
    return sorted(a + b for a in d1 for b in d2)


def random_dice():
    import random
    a = [random.randint(1, 5 * 10 ** 8) for _ in range(6)]
    b = [random.randint(1, 5 * 10 ** 8) for _ in range(6)]
    return a, b


def test(d1, d2):
    ps = pair_sums(d1, d2)
    a, b = solve(ps)
    return pair_sums(a, b) == ps


def test100():
    for _ in range(100):
        if not test(*random_dice()):
            print('you fucked up')


def test100b():
    for _ in range(100):
        solve([2] * 35 + [3])


def main():
    T = int(input())
    for _ in range(T):
        S = [int(x) for x in input().split()]
        solve(S)


if __name__ == '__main__':
    main()
