![CALICO Logo](https://calico.berkeley.edu/images/banner/blocks.png)

# calico-fa23
***Note**: This repo is under construction. Check back occasionally for updates! Last Updated: 11/18*

## Editorial Progress
**Published**: rotate

**Drafted**: berkeleytime, birthday, crosstown, wtds, jenga, plus9qh, subway, judgehosts, boxcars, rescueteam, benga, barbieland 

## Quick Start
This repository contains all contest materials for CALICO Fall '23, including solutions, editorials, tests, templates, and problem statements.

You can explore this repository using GitHub in your browser or download an [archive of all the files](https://github.com/calico-team/calico-fa23/archive/refs/heads/main.zip). If you'd like to see what files participants were given during the contest, you can download the [contest.zip](https://calico.berkeley.edu/files/calico-fa23/contest.zip)!

Although the contest is over, you can still submit solutions to the [judge platform](https://calicojudge.com) under the `calico-fa23-archive` contest. Sign in or register if you don't have an account already. Then change the selected contest to `calico-fa23-archive` on the right side of the navigation bar.

## Repository Structure
Subdirectories are named after problem IDs and contain their solutions, editorials, tests, templates, and problem statements.

### Solutions
Solutions are programs written by us that implement different approaches of varying efficiency in multiple programming languages to solve each problem. As a result, some solutions may pass more test sets than others. Solution files are named `[problem name]_[solution name].[extension]`, where `[solution_name]` is a keyword that describes the solution, and `[extension]` is the extension used by that language's source files (for example, `.cpp`, `.java`, or `.py`).

### Editorials
Editorials describe and thoroughly explain several approaches of varying efficiency to solve each problem. They are named `[problem_name]-editorial.pdf`.

### Tests
These are the inputs and outputs we use to test your program for correctness. Input files have the `.in` extension and corresponding output files have the `.ans` extension with the same file name. Test files are categorized as sample (visible to contestants during the contest) and secret (everything else) under the data folder in each problem subdirectory.

### Templates
Templates provide starter code that handle parsing input in multiple languages, so contestants can jump right into problem solving. They are named `[problem name]_template.[extension]`.

Note that these templates are only guaranteed to apply to the main test set of each problem; completing bonus test sets may require modifying the templates. When this is the case, we make it clear in the problem statement.

### Problem Statements
Problem statements describe the problem contestants need to solve, as well as their input and output format. They are named `[problem name].pdf`.

#### Submissions (All Problems)
|File|Description|
|---|---|
|`submissions/accepted/*`|These are identical to the respective programs in `solutions/*`. For each problem, one of the Python models is used by the generators to generate the reference outputs.|
|`submissions/runtime_error/*`<br>`submissions/time_limit_exceeded/*`<br>`submissions/wrong_answer/*`|These are implementations written by organizers pre-contest that seem perfect at first glance but have small bugs that cause the respective issues when judged. We predicted that most failed in-contest submissions would be categorized under one of these bugs.|

### Directory Tree
```
[contest name]
├── [contest name].pdf
├── [contest name]-editorial.pdf
├── [problem name]
│   ├── [problem name].pdf
│   ├── [problem name]-editorial.pdf
│   ├── solutions
│   │   ├── [problem name]_[solution name].[extension]
│   │   └── ...
│   ├── templates
│   │   ├── [problem name]_template.[extension]
│   │   └── ...
│   └── tests
│       ├── sample
│       │   ├── [test name].in
│       │   ├── [test name].ans
│       │   └── ...
│       └── secret
│           ├── [test name].in
│           ├── [test name].ans
│           └── ...
├── [problem name]
│   └── ...
└── ...
```

## Credits

Under construction!