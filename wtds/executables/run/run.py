import random
from collections import deque
import heapq

def run():
    class Datamon:
        types = ['queueon', 'stackeon', 'heapeon']
        
        def __init__(self, type):
            if type == 'queueon':
                self.data_struct = deque([])
                self.add = lambda x : self.data_struct.append(x)
                self.remove = lambda : self.data_struct.popleft()
            elif type == 'stackeon':
                self.data_struct = []
                self.add = lambda x : self.data_struct.append(x)
                self.remove = lambda : self.data_struct.pop()
            elif type == 'heapeon':
                self.data_struct = heapq.heapify([])
                self.add = lambda x : heapq.heappush(self.data_struct, x)
                self.remove = lambda : heapq.heappop(self.data_struct)
            else:
                give_IE(f'Initializing invalid Datamon type: f"{type}"')
            
            self.type = type
        
        def feed(self, num):
            self.add(num)

        def poop(self):
            if len(self.data_struct) == 0:
                return None
            return self.remove()

        def guess_correct(self, guess):
            return guess == self.type
    
    def dumpy():
        assert len(query_log) - len(response_log) in [0, 1]

        log('Interaction log for the last test case:')

        for i in range(len(query_log)):
            log(f'{query_log[i]}')
            if i < len(response_log):
                log(f'>>{response_log[i]}')

    log(f'Begin interaction')
    
    T = int(input_test_in())
    print_prog(T)
    
    for case in range(1, T + 1):
        log(f'Begin test case #{case} of {T}')
        
        datamon = Datamon(input_test_in().strip())

        query_log = []
        response_log = []
        
        while True:
            raw_input = input_prog()
            type, arg = parse_query(raw_input)
            query_log.append(raw_input)

            if type == 'feed':
                if not arg.isdigit():
                    give_WA(f'Invalid argument for feed: "{arg}"')
                arg = int(arg)
                if not (0 <= arg <= 100):
                    give_WA(f'Feed argument out of range: "{arg}" is not between 0 and 100')
                datamon.feed(arg)
                
                response_log.append('OK')
                print_prog('OK')
            elif type == 'poop':
                datamon_poop = datamon.poop()
                if datamon_poop is None:
                    give_WA('The Datamon has no numbers inside its stomach to poop out')
                
                response_log.append(datamon_poop)
                print_prog(datamon_poop)
            elif type == 'guess':
                if datamon.guess_correct(arg):
                    print_prog('CORRECT')
                    break
                else:
                    if arg in Datamon.types:
                        dumpy()
                        give_WA(f'Your program guessed {arg}, but the Datamon was actually {datamon}')
                    else:
                        dumpy()
                        give_WA(f'Your program guessed {arg}, which is not a valid Datamon')
            else:
                dumpy()
                give_WA(f'Invalid query format: "{type}"')
    
    log('End interaction')
    give_AC()

def parse_query(query_str):
    query_str = query_str.strip()
    if query_str.startswith('feed') or query_str.startswith('guess'):
        s = query_str.split()
        if s[0] in ['feed', 'guess'] and len(s) == 2:
            return s[0], s[1]
    return query_str, None

################################################################################

import io
import sys

_log = []
_test_in, _prog_out = None, None

def main():
    if len(sys.argv) != 3:
        _print_err('Incorrect number of arguments')
        exit(1)
    
    _log_without_tabs('Judge:\tUser:\tInfo:')
    
    _, test_in_path, prog_out_path = sys.argv
    with open(test_in_path, 'r') as test_in:
        with open(prog_out_path, 'w') as prog_out:
            global _test_in, _prog_out
            _test_in, _prog_out = test_in, prog_out
            run()

def give_AC():
    try:
        temp = ''
        while not temp:
            temp = input().strip()
        give_WA(f'Unexpected trailing output when judge was finished: {temp}')
    except EOFError:
        pass
    
    _print_prog_out('AC')
    exit(0)

def give_WA(reason):
    log('End of log')
    
    _print_prog_out('WA')
    _print_prog_out('Reason:', reason)
    _print_prog_out('Interaction Log:')
    for line in _log:
        _print_prog_out(line)
    
    try:
        print('WRONG_ANSWER', flush=True)
    except BrokenPipeError as e:
        pass
    
    _exhaust_input_prog()
    exit(0)

def give_IE(reason):
    log('End of log')
    
    _print_err('Run executable internal error:', reason)
    
    _print_prog_out('IE')
    _print_prog_out('Run executable internal error:', reason)
    _print_prog_out('Interaction Log:')
    for line in _log:
        _print_prog_out(line)
    
    _exhaust_input_prog()
    exit(1)

def input_test_in():
    try:
        return _test_in.readline().strip()
    except EOFError:
        give_IE('End of test input while judge expected more input')

def input_prog():
    try:
        prog_output = input()
        _log_without_tabs(f'\t{prog_output}')
        return prog_output
    except (EOFError, BrokenPipeError): # TODO check if BrokenPipeError is necessary
        give_WA('User program exited early when judge expected more output')

def _exhaust_input_prog():
    try:
        while True:
            input()
    except:
        pass

def print_prog(*args, **kwargs):
    prog_input = io.StringIO()
    print(*args, **kwargs, file=prog_input, end='')
    try:
        print(*args, **kwargs, flush=True)
        _log_without_tabs(prog_input.getvalue())
    except BrokenPipeError:
        temp = prog_input.getvalue()
        give_WA(f'User program exited early when judge had more output: {temp}')

def _print_prog_out(*args, **kwargs):
    print(*args, **kwargs, file=_prog_out)

def _print_err(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def log(message):
    _log_without_tabs(f'\t\t{message}')

def _log_without_tabs(message):
    if len(message) > 100:
        message = message[:100] + ' (truncated after 50 bytes)'
    _log.append(message)

if __name__ == '__main__':
    main()

