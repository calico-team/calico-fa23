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
    "9": ["99 bottles of beer on the wall, 99 bottles of beer.",
"Take one down and pass it around, 98 bottles of beer on the wall.",
"98 bottles of beer on the wall, 98 bottles of beer.",
"Take one down and pass it around, 97 bottles of beer on the wall.",
"97 bottles of beer on the wall, 97 bottles of beer.",
"Take one down and pass it around, 96 bottles of beer on the wall.",
],
}

class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, length, code):
        self.length = length
        self.code = code
        assert self.length == len(self.code.splitlines()), "Lengths do not match"

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
        TestCase(1, '''Hello, world!'''),
        TestCase(3, '''Hello, world!
H++QH
Hello, world!'''),
        TestCase(7, '''99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
Hello, world!'''),
        TestCase(15, '''99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
9Q++9+Q
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
9Q++9+QH
Hello, world!'''),
        TestCase(7, '''QQQQQQQ
QQQQQQQ
QQQQQQQ
QQQQQQQ
QQQQQQQ
QQQQQQQ
QQQQQQQ'''),
    ]
    make_sample_test(main_sample_cases, 'main')
    


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    def single_case(idx):
        if idx < 10:
            maxlines = random.randint(1, 5)
        elif idx < 30:
            maxlines = random.randint(1, 15)
        elif idx < 50:
            maxlines = random.randint(1, 45)
        elif idx < 70:
            maxlines = random.randint(1, 95)
        elif idx < 90:
            maxlines = random.randint(1, 195)
        else:
            maxlines = random.randint(1, 995)


        chars = ["H", "H", "H", "+", "+", "9"]
        if random.randint(1, 2) == 1:
            chars.append("Q")
        
        source = []
        lines = 0
        while lines < maxlines:
            char = random.choice(chars)
            if char == "H":
                lines += 1
            elif char == "9":
                lines += 6
            source.append(char)

        single_string = "".join(source)

        useless_accumulator = 0

        out = []
        for char in source:
            if char == "Q":
                out.append(single_string)
            elif char == "+":
                useless_accumulator += 1
            else:
                out.extend(in_to_out[char])

        return TestCase(len(out), "\n".join(out))

    for i in range(5):
        main_random_cases = [single_case(j) for j in range(100)]
        make_secret_test(main_random_cases, 'main_random')
    

def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(case.length, file=file)
        print(case.code, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    for case in cases:
        print('', file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
