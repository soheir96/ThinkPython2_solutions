'''
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?

**ANSWER**
Returned result:
Elapsed time for build_word_list_v1: 0.016004562377929688
Elapsed time for build_word_list_v2: 16.268741846084595

Second method takes a lot longer to run as it's redefining new variable for every iteration. 
'''

import os
import time

def read_file(fname):
    ''' Reads text file and returns it's content. '''
    # Open the file in read mode
    with open(fname, 'r') as file:
        # Read the contents of the file
        return file.read()

def build_word_list_v1(txt):
    ''' Builds and returns list of words from txt input using append method, '''
    t = []
    for w in txt.split():
        t.append(w)
    return t

def build_word_list_v2(txt):
    ''' Builds and returns list of words from txt input using idiom  t = t + [x]'''
    t = []
    for w in txt.split():
        t = t + [w]
    return t

def create_file_path(dir_path,fname):
    ''' Creates file path using given directory path and file name '''
    return os.path.join(dir_path, fname)

def main():
    # Get the current working directory
    current_dir = os.getcwd()
    # create file path
    f_path = create_file_path(current_dir, 'chp10\words.txt') 
    # read file contents
    f_content = read_file(f_path)

    # Time functions 
    # TODO: Could be neater solution to write a loop for this

    # append method test
    start_time_1 = time.time()
    build_word_list_v1(f_content)
    end_time_1 = time.time()
    elapsed_time_1 = end_time_1 - start_time_1
    print("Elapsed time for build_word_list_v1: {}".format(elapsed_time_1))

    #  t = t + [x] method test 
    start_time_2 = time.time()
    build_word_list_v2(f_content)
    end_time_2 = time.time()
    elapsed_time_2 = end_time_2 - start_time_2
    print("Elapsed time for build_word_list_v2: {}".format(elapsed_time_2))


if __name__ == "__main__":
    main()