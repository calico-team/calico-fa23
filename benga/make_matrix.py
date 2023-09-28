from itertools import chain, combinations

flat_state = '000000000'
visible_placements = [
    # laterals
    '111000000', '000111000', '000000111',
    '100100100', '010010010', '001001001',
    # verticals
    '300000000', '030000000', '003000000',
    '000300000',              '000003000',
    '000000300', '000000030', '000000003',
]
all_placements = visible_placements + ['000030000']

def main():
    transitions = make_transition_dict(visible_placements)
    matrix, state = make_transition_matrix(transitions)
    print('visible transition matrix:')
    print('[')
    for row in matrix:
        print(f'    {row},')
    print(']')


def make_transition_dict(allowed_placements):
    transition_dict = {}
    state_stack = [flat_state]
    while state_stack:
        state = state_stack.pop()
        if state not in transition_dict:
            transition_dict[state] = adjacent_states(state, allowed_placements)
            for new_state in transition_dict[state]:
                state_stack.append(new_state)
    return transition_dict


def adjacent_states(state, allowed_placements):
    new_states = {}
    for s in powerset(allowed_placements):
        new_state = apply_placements(state, s)
        if new_state:
            if new_state not in new_states:
                new_states[new_state] = 1
            else:
                new_states[new_state] += 1
    return new_states


def powerset(s):
    return chain.from_iterable(combinations(s,n) for n in range(len(s) + 1))


def apply_placements(state, placements):
    state = [int(h) for h in state]
    for p in placements:
        p = [int(h) for h in p]
        for i in range(9):
            if p[i] != 0:
                if state[i] == 0:
                    state[i] += p[i]
                else:
                    return None
    
    if 0 in state:
        return None
    return ''.join(str(h - 1) for h in state)


def make_transition_matrix(transition_dict):
    states = len(transition_dict)
    id_to_state = list(sorted(transition_dict.keys()))
    state_to_id = {s: i for i, s in enumerate(id_to_state)}
    
    matrix = [[0 for j in range(states)] for i in range(states)]
    for from_state, to_dict in transition_dict.items():
        for to_state, ways in to_dict.items():
            matrix[state_to_id[from_state]][state_to_id[to_state]] = ways
    
    return matrix, id_to_state


if __name__ == '__main__':
    main()
