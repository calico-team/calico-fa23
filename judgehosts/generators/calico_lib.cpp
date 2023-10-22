#pragma once
#include <bits/stdc++.h>
#include <filesystem>
using namespace std;

void debug_print(string msg) {
    cerr << msg << endl;
}

string get_path(bool is_secret, string file_name = "", string ext = "") {
    string relative_path;
    relative_path += "data/";
    relative_path += (is_secret ? "secret/" : "sample/");
    if (!file_name.empty()) {
        relative_path += (is_secret ? "secret_" : "sample_");
        relative_path += file_name;
    }
    if (!ext.empty()) {
        relative_path += "." + ext;
    }
    return relative_path;
    // const char* cwd = getcwd(NULL, 0);
    // string path(cwd);
    // return path + relative_path;
}

/**
 * Make input .in and output .ans files using a list of test cases, a flag
 * for if this is sample or secret, and an optional file name. Also keep track
 * of the number of files created so far in order to prepend names with IDs
 * as tests will be run in alphabetical order. The file name is optional but can
 * be nice to mark certain files to be added to certain test sets when zipping.
*/
template <class T>
void make_test_file(T cases, bool is_secret, int id, string file_name) {
    if (!file_name.empty()) {
        file_name = to_string(id) + "_" + file_name;
    }
    string in_path = get_path(is_secret, file_name, "in");
    make_test_in(cases, in_path);
    string ans_path = get_path(is_secret, file_name, "ans");
    make_test_out(cases, ans_path);
}

int _secret_test_id = 0;


/**
 * Make a secret test input file and output file for the given cases and name.
*/
template <class T>
void make_secret_test(T cases, string file_name = "") {
    debug_print("Creating secret test file \"" + file_name + "\"...");
    make_test_file(cases, true, _secret_test_id, file_name);
    ++_secret_test_id;
    debug_print("Done!");
}

int _sample_test_id = 0;

/**
 * Make a sample test input file and output file for the given cases and name.
*/
template <class T>
void make_sample_test(T cases, string file_name = "") {
    debug_print("Creating sample test file \"" + file_name + "\"...");
    make_test_file(cases, false, _sample_test_id, file_name);
    ++_sample_test_id;
    debug_print("Done!");
}

/**
 * Delete old data first so we can start making data with a clean state.
*/
void delete_old_data() {

    // This might work?

    const char* cwd = getcwd(NULL, 0);
    string str(cwd);
    str += "/data/";
    
    std::filesystem::path dir(str+"sample/");

    for (auto const& entry : std::filesystem::directory_iterator(dir))
        std::filesystem::remove_all(entry.path());

    dir = str+"secret/";

    for (auto const& entry : std::filesystem::directory_iterator(dir))
        std::filesystem::remove_all(entry.path());

}

/**
 * Make the sample and secret directories in the data directory if
 * they do not already exist.
*/
void make_dirs() {

    debug_print("Creating directories...");

    string sample_path = get_path(false);
    string secret_path = get_path(true);

    const char* cwd = getcwd(NULL, 0);
    string path(cwd);

    // This might work???
    std::filesystem::create_directory(sample_path.c_str());
    std::filesystem::create_directory(secret_path.c_str());
    
    debug_print("Done!"); 
}

/**
 * Make all data files
 * @param make_sample_tests : function that generates all sample tests
 * @param make_secret_tests : function that generates all secret tests
 * @param make_test_in      : function that prints the test case input
 * @param make_test_out     : function that prints the test case output
 * @param seed              : seed for the random generator
 * @param random            : Merseene random number generator
*/
template <class T, class U>
void make_data(T make_sample_tests, T make_secret_tests, U make_test_in, U make_test_out, long long seed, mt19937_64& random) {

    debug_print("Making data...");
    make_dirs();
    delete_old_data();
    random = mt19937_64(seed);

    debug_print("Creating sample tests...");
    make_sample_tests();
    debug_print("Done creating all sample tests!");
    debug_print("Creating secret tests...");
    make_secret_tests();
    debug_print("Done creating all secret tests!");

    debug_print("Done making all data!");
}

