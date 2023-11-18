# add
This is a problem in the CALICO problem package format, a derivative of the [DOMjudge Problem Package Format](https://www.domjudge.org/docs/manual/7.3/problem-format.html) which is itself a derivative of the [ICPC Problem Package Format](https://icpc.io/problem-package-format/).

## Resources
Include resources for your problem here:
- Problem statement: (TODO Copy problem statement link here)
- Editorial: (TODO Copy editorial link here)

## Getting Started
To get started, make a copy of this folder in your branch and rename it with your problem's short name. Then, implement data generation in `make_data.py`. Write your templates in the `template` directory. Write your solutions in the `submissions` directory. Finally, configure `make_zips.py` with your test set
options.

## Building

### Making Data
Run `./make_data.py` or `python3 make_data.py` to make test data files. You can optionally use the `-v` argument to show debug prints.

### Making Zips
Run `./make_zips.py` or `python3 make_zips.py` to make DOMjudge zip files. You can optionally use the following arguments:
- `v` see debug prints
- `d` also make data before zipping
- `r` create release version without * in DOMjudge name

## Testing

### CALICOjudge
The preferred way to test is to make zips, then upload directly to the admin development contest at https://calicojudge.com. If you don't already have access, ask an officer.

### Local
You can also run `./check [submission_path] [test_path_without_extension]` to test a submission against a test file locally. For example, you can do `./check submissions/accepted/add_arbitrary.py data/sample/sample_00_main`

Note that you may need to modify the `check` file if your Python/Java/C++ installation is different.

## Repository Structure
Here's how each problem directory is structured.

Note that problem statements + editorials should NOT be included in this working repo, we'll add them in when we create the public versions of these repos!

### Directory Tree
```
[problem name]
├── calico_lib.py
├── check
├── make_data.py
├── make_zips.py
├── [problem name]_[test set].zip
├── ...
├── data
│   ├── sample
│   │   ├── [test name].in
│   │   ├── [test name].ans
│   │   └── ...
│   └── secret
│       ├── [test name].in
│       ├── [test name].ans
│       └── ...
├── submissions
│   ├── accepted
│   │   ├── [problem name]_[submission_name].[extension]
│   │   └── ...
│   ├── run_time_error
│   │   ├── [problem name]_[submission_name].[extension]
│   │   └── ...
│   ├── time_limit_exceeded
│   │   ├── [problem name]_[submission_name].[extension]
│   │   └── ...
│   └── wrong_answer
│       ├── [problem name]_[submission_name].[extension]
│       └── ...
└── templates
    ├── [problem name]_template.[extension]
    └── ...
```

### Root
The root of the directory includes scripts and is also where zip files are created. These files include:
- `calico_lib.py` contains helper functions used by other scripts
- `make_data.py` used to make test data
- `make_zips.py` used to create zips
- `check` a simple script to test submissions locally

### Data
These are the inputs and outputs we use to test your submission for correctness. Input files have the `.in` extension and corresponding output files have the `.ans` extension with the same file name.

All test files regardless of test set should be placed here. The `make_zips.py` script will determine which files get added to which test set when zips are created.

#### Sample
These are tests whose contents are visible when you upload to the judge. Use these to give the general idea of the problem and hint at edge cases.

#### Secret
These are tests whose contents are not visible until the end of the contest. Use these to thoroughly check a submission for correctness.

### Submissions
Submissions are programs written by us that implement different approaches of varying efficiency in multiple programming languages to solve each problem. As a result, some submissions may pass more test sets than others. Submissions files are named `[problem name]_[submission name].[extension]`, where `[submission_name]` is a keyword that describes the approach, and `[extension]` is the extension used by that language's source files (for example, `.cpp`, `.java`, or `.py`).

All submissions regardless of test set should be placed here. The `make_zips.py` script will determine which files get added to which test set when zips are created.

#### Accepted
These are submissions that should pass without errors.

Generally, we'd like to have at least one accepted submission in each programming language (`.cpp`, `.java`, or `.py`) and at least one submission for each major approach.

#### Run Time Error
These are submissions that should error out during runtime. This can be because of division by zero, going out of bounds, hitting the recursion limit, or similar.

This may not be necessary for all problems, so feel free to delete this folder if you do not need to test any submissions in this category.

#### Time Limit Exceeded
These are submissions that should time out by exceeding the time limit. If your problem has multiple approaches with a slower one being expected to fail a bonus test set for this reason, make a copy of that submission and put it in this folder.

#### Wrong Answer
These are submissions that should fail due to just getting a wrong answer. If your problem has multiple approaches with one that only outputs correct answers for the main but not for the bonus, make a copy of that submission and put it in this folder.

### Templates
Templates provide starter code that handle parsing input in multiple languages, so contestants can jump right into problem solving. They are named `[problem name]_template.[extension]`.

Note that these templates are only guaranteed to apply to the main test set of each problem; completing bonus test sets may require modifying the templates.
