"""Generates border state transition matrices configurations of the problem

Usage:
python3 make_matrix.py <k> [visible] [symmetry]
- k:        the length and width of the kxkxN tower. must be within 1 <= k <= 9
- visible:  True if we want to enforce all pieces visible else False
- symmetry: True if we optimize for rotationally symmetric states else False
"""

from itertools import chain, combinations
from math import isqrt
import sys

MAX_FEASIBLE_SIZE = 60


def main():
    k = int(sys.argv[1])
    assert 1 <= k <= 9
    visible = 'visible' in sys.argv
    symmetry = 'symmetry' in sys.argv
    noprint = 'noprint' in sys.argv
    
    transitions = make_transition_dict(k, visible, symmetry)
    if transitions:
        matrix, states = make_transition_matrix(transitions)
        pretty_print_matrix(matrix, states, k, visible, symmetry, noprint)
        path = 'matrix_' + str(k) + \
               ('_v' if visible else '') + \
               ('_s' if symmetry else '') + \
               '.in'
        serialize_matrix(matrix, path)
        print()


def make_transition_matrix(transition_dict):
    states = len(transition_dict)
    id_to_state = list(sorted(transition_dict.keys()))
    state_to_id = {s: i for i, s in enumerate(id_to_state)}
    
    matrix = [[0 for j in range(states)] for i in range(states)]
    for from_state, to_dict in transition_dict.items():
        for to_state, ways in to_dict.items():
            matrix[state_to_id[from_state]][state_to_id[to_state]] = ways
    
    return matrix, id_to_state


def make_transition_dict(k, visible, symmetry):
    allowed_placements = find_allowed_placements(k, visible)
    flat_state = '0' * (k*k)
    known_states = {flat_state}
    
    transition_dict = {}
    state_stack = [flat_state]
    while state_stack:
        state = state_stack.pop()
        if state not in transition_dict:
            adjacent = adjacent_states(state, allowed_placements, symmetry)
            transition_dict[state] = adjacent
            for new_state in transition_dict[state]:
                state_stack.append(new_state)
                known_states.add(new_state)
        
        if len(known_states) > MAX_FEASIBLE_SIZE:
            print(f'matrix for k={k}, visible={visible}, symmetry={symmetry}:')
            print(f'matrix is infeasible (n > {MAX_FEASIBLE_SIZE})')
            print()
            return None
    
    return transition_dict


def find_allowed_placements(k, visible):
    laterals = []
    for i in range(k):
        # 111000000, 000111000, 000000111
        laterals.append('0'*(k*i) + '1'*k + '0'*(k*(k-i-1)))
        # 100100100, 010010010, 001001001
        laterals.append('0'*i + ('1' + '0'*(k-1))*(k-1) + '1' + '0'*(k-i-1))

    visible_verticals, hidden_verticals = [], []
    for i in range(k * k):
        p = '0'*i + str(k) + '0'*(k*k-i-1)
        # 300000000, 030000000, 003000000,
        # 000300000,            000003000,
        # 000000300, 000000030, 000000003,
        if i < k or i >= k * (k - 1) or i % k == 0 or i % k == (k - 1):
            visible_verticals.append(p)
        #            000030000
        else:
            hidden_verticals.append(p)
    
    if visible:
        return laterals + visible_verticals
    else:
        return laterals + visible_verticals + hidden_verticals


def adjacent_states(state, allowed_placements, symmetry):
    allowed_placements = state_allowed_placements(state, allowed_placements)

    new_states = {}
    for s in powerset(allowed_placements):
        new_state = apply_placements(state, s)
        if new_state:
            if symmetry:
                new_state = min_rotation(new_state)
            if new_state not in new_states:
                new_states[new_state] = 1
            else:
                new_states[new_state] += 1
    return new_states


def state_allowed_placements(state, allowed_placements):
    def allows(state, placement):
        for i in range(len(state)):
            if placement[i] != '0' and state[i] != '0':
                return False
        return True
    return [p for p in allowed_placements if allows(state, p)]


def apply_placements(state, placements):
    state = [int(h) for h in state]
    for p in placements:
        p = [int(h) for h in p]
        for i in range(len(state)):
            if p[i] != 0:
                if state[i] == 0:
                    state[i] += p[i]
                else:
                    return None
    
    if 0 in state:
        return None
    return ''.join(str(h - 1) for h in state)


def min_rotation(state):
    rotations = [state]
    for _ in range(3):
        rotations.append(rotate(rotations[-1]))
    return min(rotations)


def rotate(state):
    k = isqrt(len(state))
    cols = zip(*(state[k*i: k*i+k] for i in range(k)))
    return ''.join(''.join(col)[::-1] for col in cols)


def powerset(s):
    return chain.from_iterable(combinations(s,n) for n in range(len(s) + 1))


def pretty_print_matrix(matrix, states, k, visible, symmetry, noprint):
    n = len(matrix)
    m = sum(sum(1 for w in r if w) for r in matrix)
    w = sum(sum(r) for r in matrix)
    print(f'matrix for k={k}, visible={visible}, symmetry={symmetry}:')
    print(f'{n} nodes, {m} edges, {w} sum')
    if not noprint:
        for i in range(n):
            print(f'{states[i]}: {matrix[i]},')


def serialize_matrix(matrix, path):
    with open(path, 'w', newline='\n') as f:
        print(len(matrix), file=f)
        for row in matrix:
            print(' '.join(str(i) for i in row), file=f)
    print('serialized to', path)


if __name__ == '__main__':
    main()
