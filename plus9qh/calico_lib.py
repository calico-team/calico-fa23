"""
A collection of helper functions to make data, zips, and more.

Feel free to modify this file if necessary, although you should not have to.
"""

import glob
import os
import random
import sys
import zipfile

_make_test_in, _make_test_out = None, None


def make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, seed):
    """
    Make all data files.
    """
    global _make_test_in, _make_test_out
    _make_test_in, _make_test_out = make_test_in, make_test_out
    
    debug_print('Making data...')
    
    make_dirs()
    delete_old_data()
    random.seed(seed)
    
    debug_print('Creating sample tests...')
    make_sample_tests()
    debug_print('Done creating all sample tests!')
    debug_print('Creating secret tests...')
    make_secret_tests()
    debug_print('Done creating all secret tests!')
    
    debug_print('Done making all data!')


def make_dirs():
    """
    Make the sample and secret directories in the data directory if they do not
    already exist.
    """
    debug_print('Creating directories', end='...')
    
    sample_path, secret_path = get_path(False), get_path(True)
    if not os.path.exists(sample_path):
        os.makedirs(sample_path)
    if not os.path.exists(secret_path):
        os.makedirs(secret_path)
    
    debug_print('Done!')


def delete_old_data():
    """
    Delete old data first so we can start making data with a clean slate.
    """
    debug_print('Deleting old data', end='...')
    
    deleted = False
    for file in glob.glob(get_path(False, '*')):
        if os.path.exists(file):
            os.remove(file)
        deleted = True
    for file in glob.glob(get_path(True, '*')):
        if os.path.exists(file):
            os.remove(file)
        deleted = True
    
    debug_print('Done!' if deleted else 'Nothing to delete!')


_sample_test_id = 0


def make_sample_test(cases, file_name=''):
    """
    Make a sample test input file and output file for the given cases and name.
    """
    debug_print(f'Creating sample test file "{file_name}"', end='...')
    
    global _sample_test_id
    make_test_file(cases, False, _sample_test_id, file_name)
    _sample_test_id += 1
    
    debug_print('Done!')


_secret_test_id = 0


def make_secret_test(cases, file_name=''):
    """
    Make a secret test input file and output file for the given cases and name.
    """
    debug_print(f'Creating secret test file "{file_name}"', end='...')
    
    global _secret_test_id
    make_test_file(cases, True, _secret_test_id, file_name)
    _secret_test_id += 1
    
    debug_print('Done!')


def make_test_file(cases, is_secret, id, file_name):
    """
    Make input .in and output .ans files using a list of test cases, a flag for
    if this is sample or secret, and an optional file name. Also keep track of
    the number of files created so far in order to prepend names with IDs as
    tests will be run in alphabetic order. The file name is optional but can be
    nice to mark certain files to be added to certain test sets when zipping.
    """
    if file_name:
        file_name = f'{id:02d}_{file_name}'
    else:
        file_name = f'{id:02d}'
    
    in_path = get_path(is_secret, file_name, 'in')
    with open(in_path, 'w', newline='\n') as in_file:
        _make_test_in(cases, in_file)
    ans_path = get_path(is_secret, file_name, 'ans')
    with open(ans_path, 'w', newline='\n') as ans_file:
        _make_test_out(cases, ans_file)


def get_path(is_secret, file_name='', ext=None):
    """
    If file_name is unspecified, makes a path to the root of the sample or
    secret directory depending on is_secret.
    
    Otherwise, get the path for a file in the sample or secret directory. The
    path is absolute based on the location of this file, not relative to the
    execution path.
    """
    relative_path = ''.join([
        'data/',
        'secret/' if is_secret else 'sample/',
        ('secret_' if is_secret else 'sample_') if file_name else '',
        file_name,
        f'.{ext}' if ext else ''
    ])
    return os.path.join(os.path.dirname(__file__), relative_path)


def make_zips(problem_name, time_limit, test_set_names, \
              is_data_in_test_set, is_submission_in_test_set):
    """
    Make zip files for each test set.
    
    If the -d argument is passed, also make data before zipping.
    """
    if len(sys.argv) > 1 and 'd' in sys.argv[1]:
        import make_data
        make_data.main()
    
    debug_print('Making zips...')
    delete_old_zips(problem_name, test_set_names)
    make_actual_zips(problem_name, time_limit, test_set_names, \
              is_data_in_test_set, is_submission_in_test_set)
    debug_print('Done making all zips!')


def delete_old_zips(problem_name, test_set_names):
    """
    Delete old zips if they exist so we can start making with a clean slate.
    """
    debug_print('Deleting old zips', end='...')
    deleted = False
    for test_set_name in test_set_names:
        zip_file_name = get_zip_file_path(problem_name, test_set_name)
        if os.path.exists(zip_file_name):
            os.remove(zip_file_name)
            deleted = True
    debug_print('Done!' if deleted else 'Nothing to delete!')


def make_actual_zips(problem_name, time_limit, test_set_names, \
                     is_data_in_test_set, is_submission_in_test_set):
    """
    Create a zip for each test set. Each test set consists of data, submissions,
    and the DOMjudge metadata file.
    """
    for test_set_name in test_set_names:
        debug_print(f'Creating zip for test set "{test_set_name}"...')
        
        file_path = get_zip_file_path(problem_name, test_set_name)
        with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_path(zip_file, 'data', test_set_name, is_data_in_test_set)
            zip_path(zip_file, 'submissions', test_set_name, is_submission_in_test_set)
            zip_metadata(zip_file, problem_name, test_set_name, time_limit)
        
        debug_print(f'Done creating zip for test set "{test_set_name}"!')


def get_zip_file_path(problem_name, test_set_name):
    """
    Get the path for a zip file given the name of the test set and the DOMjudge
    metadata name. The path is absolute based on the location of this file, not
    the location that ran the command to execute this file.
    """
    relative_path = f'{problem_name}_{test_set_name}.zip'
    return os.path.join(os.path.dirname(__file__), relative_path)


def zip_path(zip_file, relative_path, test_set_name, is_file_in_test_set):
    """
    Add all files in the relative_path relative to this file's path into the
    zip_file with the test_set_name. Only files that is_file_in_test_set says
    are to be added to the current test_set_name will be added.
    """
    debug_print(f'Zipping directory "{relative_path}" for test set "{test_set_name}"', end='...')
    
    path = os.path.join(os.path.dirname(__file__), relative_path)
    for root, dirs, files in os.walk(path):
        for file in files:
            if is_file_in_test_set(file, test_set_name):
                file_path = os.path.join(root, file)
                zip_path = os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
                zip_file.write(file_path, zip_path)
    
    debug_print(f'Done!')


def zip_metadata(zip_file, problem_name, test_set_name, time_limit):
    """
    Add the DOMjudge metadata file to the zip_file with the test_set_name. This
    function creates a temporary file, writes name and timelimit, adds it to
    the zip, then deletes the temporary file.
    """
    debug_print(f'Zipping domjudge-problem.ini for test set "{test_set_name}"', end='...')
    
    meta_path = os.path.join(os.path.dirname(__file__), 'domjudge-problem.ini')
    with open(meta_path, 'w') as meta_file:
        if len(sys.argv) > 1 and 'r' not in sys.argv[1]:
            problem_name = '*' + problem_name
        print(f'name={problem_name}_{test_set_name}', file=meta_file)    
        print(f'timelimit={time_limit}', file=meta_file)
    
    zip_file.write(meta_path, 'domjudge-problem.ini')
    os.remove(meta_path)
    
    debug_print('Done!')


def debug_print(*args, **kwargs):
    """
    Only print if the -v argument is passed
    """
    if len(sys.argv) > 1 and 'v' in sys.argv[1]:
        print(*args, **kwargs)
