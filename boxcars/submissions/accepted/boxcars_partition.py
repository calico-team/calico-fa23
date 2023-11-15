"""

TODO move this mini-editorial somewhere else

WLOG let our answer be a1 <= a2 <= ... <= a6 and b1 <= ... <= b6. A solution,
then, is an assignment of positive integers to all ai and bi and an assignment
of all values in S to sij such that sij = bi + aj, as shown below:

    a1  a2  a3  a4  a5  a6
b1  s11 s12 s13 s14 s15 s16
b2  s21 s22 s23 s24 s25 s26
b3  s31 s32 s33 s34 s35 s36
b4  s41 s42 s43 s44 s45 s46
b5  s51 s52 s53 s54 s55 s56
b6  s61 s62 s63 s64 s65 s66

Checking all 36! assignments of S to sij is too much, unfortunately. We need a
starting point to cut down on some options.

Thankfully, the existence of a solution implies we can add some integer k to all
ai and subtract from all bi of that solution. We can also swap a and b. This
means if a solution exists, a solution with a1 = 1 exists. Thus, WLOG we can
set a1 = 1.

A very important property of the table above is that i < k ==> sij <= skj and
j < l ==> sij <= sil. This means that s11 <= s12 and s11 <= s21, so S_1 must
be assigned s11. Along with a1 = 1, this implies b1 = S_1 - 1.

Now with a starting point, observe that if we assign all s1i (fill the first
row), then all the other values become well defined, and we will be able to
check if a solution with those s1i assignments exists. The smallest unassigned
S value must be in s21. This means b2 = s21 - a1. With b2 set, we can calculate
what the values of all s2i must be in order for a solution to exist:
s2i = b2 + ai. If any of these aren't able to be assigned by S, no solution with
these s1i exist. Otherwise, continue the process to try assigning to the rest
of the table.

Note that since s16 <= s26 <= ... s66 and s11 has already been assigned, there
are 30 choose 5 = 142506 different ways of assigning s1i. This cuts it a bit
close with the time limit, but implementations with a small enough constant
factor can still pass. If your constant is too big, there is another small
optimization you can make.

TODO is this even necessary?

Because of the property and the fact that S[0] was assigned to s11, S[1] must
either be in s12 or s21. We can try both. In doing either, we'll have a
situation where the first 2 values of the first row has been filled (If S[1] was
assigned to s21, we can transpose). Now we only have 29 choose 4 = 23751 ways of
assigning s1i, but we must try for both S[1] = s12 and S[1] = s21, so
23751 * 2 = 47502, which is a 3x speedup.
"""

import itertools


def solve(S: list[int]):
    # suppose we assign S[1] to s12
    a, b = [1, S[1] - S[0] + 1, 0, 0, 0, 0], [S[0] - 1, 0, 0, 0, 0, 0]
    if check(S, a, b):
        print(*a)
        print(*b)
        return
    
    # suppose we assign S[1] to s21
    a, b = [1, 0, 0, 0, 0, 0], [S[0] - 1, S[1] - 1, 0, 0, 0, 0]
    a, b = b, a # transpose so that s12 is assigned
    if check(S, a, b):
        print(*a)
        print(*b)
        return
    
    print('IMPOSSIBLE')
    return


def check(S, a, b):
    """
    Assuming that s11 and s12 have been assigned, and thus a1, a2, and b1 have
    also been assigned, try every possible s13..s16 to check if an assignment of
    S to the rest of the table exists.
    
    Returns True with the assignment stored in a and b if found.
    """
    for i13_i14_i15_i16 in itertools.combinations(range(2, 31), 4):
        i13_i14_i15_i16 = set(i13_i14_i15_i16)
        remaining = [S[i] for i in range(2, 36) if i not in i13_i14_i15_i16]
        a[2:] = [S[i] - b[0] for i in i13_i14_i15_i16]
        try:
            for i in range(1, 6):
                b[i] = remaining.pop(0) - a[0]
                for j in range(1, 6):
                    remaining.remove(b[i] + a[j])
            return True
        except ValueError:
            pass
    return False


"""
TODO move these to an actual testing file lmao
"""

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
        ans = solve(S)


if __name__ == '__main__':
    main()
