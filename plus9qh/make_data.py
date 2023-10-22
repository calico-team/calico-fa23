#!/usr/bin/env python
"""
Make test data for the problem.

To set up this script, do the following:
    - Set the seed to be something different, long, and arbitrary.
    - Set up the TestCase class to hold relevant information for your problem.
    - Write sample and secret tests in their respective functions.
    - Write input and output code in their respective functions.
Everything else will be handled by the make_data function in calico_lib.py.

You can also run this file with the -v argument to see debug prints.
"""

import random
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'this is an esolang created by cliff bliffer'

in_to_out = {
    "H": ["Hello, world!"],
    "9": [
        "99 bottles of beer on the wall, 99 bottles of beer.",
        "Take one down and pass it around, 98 bottles of beer on the wall.",
        "98 bottles of beer on the wall, 98 bottles of beer.",
        "Take one down and pass it around, 97 bottles of beer on the wall.",
        "97 bottles of beer on the wall, 97 bottles of beer.",
        "Take one down and pass it around, 96 bottles of beer on the wall.",
        ],
}

garbage = ["Somebody once told me the world is gonna roll me.",
"I ain't the sharpest tool in the shed.",
"She was looking kinda dumb with her finger and her thumb,",
"In the shape of an L on her forehead.",
"99 bottles of wine on the wall, 99 bottles of wine.",
"Take one down and pass it around, 98 bottles of wine on the wall.",
"49 bottles of beer on the wall, 49 bottles of beer.",
"Take one down and pass it around, 48 bottles of beer on the wall.",
"Hello World",
]

def different_quine(quine):
    new = ""
    for char in quine:
        if char == "+":
            new += char * random.randint(0, 2)
        else:
            new += char
    return new



class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, length, code):
        self.length = length
        self.code = code
        if self.length != len(self.code):
            print(self.length, self.code, len(self.code))
            assert False, "Lengths do not match"

def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    
    TODO Write sample tests. Consider creating cases that help build
    understanding of the problem, help with debugging, or possibly help
    identify edge cases.
    """
    main_sample_cases = [
        TestCase(1, ["Hello, world!",]),

        TestCase(9, ["Hello, world!",
"H++QH9",
"Hello, world!",
"99 bottles of beer on the wall, 99 bottles of beer.",
"Take one down and pass it around, 98 bottles of beer on the wall.",
"98 bottles of beer on the wall, 98 bottles of beer.",
"Take one down and pass it around, 97 bottles of beer on the wall.",
"97 bottles of beer on the wall, 97 bottles of beer.",
"Take one down and pass it around, 96 bottles of beer on the wall.",]),

        TestCase(7, ["69 bottles of beer on the wall, 69 bottles of beer.",
"Take one down and pass it around, 68 bottles of beer on the wall.",
"68 bottles of beer on the wall, 68 bottles of beer.",
"Take one down and pass it around, 67 bottles of beer on the wall.",
"67 bottles of beer on the wall, 67 bottles of beer.",
"Take one down and pass it around, 66 bottles of beer on the wall.",
"Hello, world!",]),

        TestCase(10, ["We're no strangers to love.",
"You know the rules, and so do I.",
"A full commitment's what I'm thinking of.",
"You wouldn't get this from any other guy.",
"I just wanna tell you how I'm feeling.",
"Gotta make you understand.",
"9Q++QHH",
"9Q++QHH",
"Never gonna give you up, never gonna let you down.",
"Never gonna run around and desert you.",]),

        TestCase(7, ["QQQQQQQ",
"QQQQQQQ",
"QQQQQQQ",
"QQQQQQQ",
"QQQQQQQ",
"QQQQQQQ",
"QQQQQQQ",]),

        TestCase(3, ["Hello, world!",
"HQ+Q",
"H+QQ",]),

    ]
    make_sample_test(main_sample_cases, 'main')
    


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """
    def single_case(group, num):
        # group 0 = no quines
        # group 1 = add quines
        # group 2 = add conflicting quines
        # group 3 = add periodic garbage text
        # group 4 = everything, long

        if group == 4:
            maxlines = random.randint(3001, 5995)
        else:
            maxlines = random.randint(1, 2995)


        chars = ["H", "+", "9"]
        if (group in [1, 2] and num % 2 == 0) or (group == 4 and random.randint(1, 2) == 1):
            chars.append("Q")
        
        source = []
        lines = 0
        while lines < maxlines:
            char = random.choice(chars)
            if char in ["H", "Q"]:
                lines += 1
            elif char == "9":
                lines += 6
            source.append(char)

        useless_accumulator = 0

        out = []
        idx = 0
        for char in source:
            if char == "Q":
                if group in [2, 4] and idx % 200 == 0:
                    out.append(different_quine("".join(source)))
                else:
                    out.append("".join(source))
            elif char == "+":
                useless_accumulator += 1
            else:
                if group in [3, 4] and idx % 200 == 0 and char == "H":
                    out.append(random.choice(garbage)) 
                else:
                    out.extend(in_to_out[char])

            idx += 1
            
        return TestCase(len(out), out)

    for group in range(5):
        main_random_cases = [single_case(group, num) for num in range(10)]
        make_secret_test(main_random_cases, 'main_random')
    

def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(case.length, file=file)
        print("\n".join(case.code), file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.plus9qh import solve
    for case in cases:
        print(solve(case.length, case.code), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
