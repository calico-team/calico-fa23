"""
Creates the contest.zip file. This file should be placed in the root of the
contest repository and the contest.zip file is created in the same location.

The contest.zip file has the following format:
contest.zip
├── <problem name>
│   ├── <problem name>.pdf
│   ├── data
│   │   └── sample
│   │       ├── sample_<sample name>.in
│   │       └── sample_<sample name>.ans
│   └── templates
│       ├── <problem name>_template.cpp
│       ├── <problem name>_template.java
│       └── <problem name>_template.py
├── <problem name 2>
│   └── ...
└── ...
"""


from pathlib import Path

import sys
import zipfile


PROBLEMS = [
    'berkeleytime',
    'birthday',
    'crosstown',
    'wtds',
    'jenga',
    'rotate',
    'plus9qh',
    'subway',
    'judgehosts',
    'boxcars',
    'rescueteam',
    'benga',
    'barbieland',
]


def main():
    debug_print(f'Creating contest.zip...')
    
    zip_path = Path(__file__).parents[0] / 'contest.zip'
    for problem_name in PROBLEMS:
        zip_problem(zip_path, problem_name)
    
    debug_print(f'Done creating contest.zip!')


def zip_problem(zip_path, problem_name):
    """
    Add all files for a problem to contest.zip. Each problem consists of sample
    test cases, templates, and the problem PDF.
    """
    debug_print(f'Adding problem {problem_name} to contest.zip...')
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_obj:
        templates_path = Path(problem_name) / 'templates'
        zip_dir(zip_obj, templates_path, ['.py', '.java', '.cpp'], 3)
        
        samples_path = Path(problem_name) / 'data' / 'sample'
        zip_dir(zip_obj, samples_path, ['.in', '.ans'], 2)
        
        pdf_path = Path(problem_name)
        zip_dir(zip_obj, pdf_path, ['.pdf'], 1)
    
    debug_print(f'Added zipping problem {problem_name} to contest.zip!')


def zip_file(zip_obj, file_path):
    """Zip the single file at file_path into zip_obj."""
    debug_print(f'Zipping file {file_path}...')
    
    zip_file_path = file_path
    os_file_path = Path(__file__).parents[0] / zip_file_path
    zip_and_log(zip_obj, os_file_path, zip_file_path)
    
    debug_print(f'Done zipping file {file_path}!')


def zip_dir(zip_obj, dir_path, allowed_extensions, min_file_count=0):
    """Zip all files in dir_path with allowed extensions into zip_obj."""
    debug_print(f'Zipping directory {dir_path}...')
    
    files_zipped = 0
    for path_object in (Path(__file__).parents[0] / dir_path).glob('*'):
        if path_object.is_file():
            zip_file_path = dir_path / path_object.name
            os_file_path = path_object
            if path_object.suffix in allowed_extensions:
                zip_and_log(zip_obj, os_file_path, zip_file_path)
                files_zipped += 1
    assert (
        files_zipped >= min_file_count and
        f'Not enough files. Expected {min_file_count} but got {files_zipped}'
    )
    
    debug_print(f'Done zipping directory {dir_path}!',
                f'Found {files_zipped} files.')


def zip_and_log(zip_obj, os_file_path, zip_file_path):
    """Assert file exists, zip it, and log debug prints."""
    assert os_file_path.is_file(), f'File path {os_file_path} does not exist.'
    debug_print(f'Zipping {zip_file_path}...', end='')
    zip_obj.write(os_file_path, zip_file_path)
    debug_print('Done!')


def debug_print(*args, **kwargs):
    """Only print if the -v argument is passed"""
    if len(sys.argv) > 1 and 'v' in sys.argv[1]:
        print(*args, **kwargs)


if __name__ == '__main__':
    main()
