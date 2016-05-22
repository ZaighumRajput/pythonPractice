#!/usr/bin/python3
import os
import argparse
from collections import namedtuple


parser = argparse.ArgumentParser()
parser.add_argument("search_text")
parser.add_argument("--folder")
parser.add_argument("-v", "--verbose")

SearchResult = namedtuple('SearchResult', 
                            ['linenumber', 'line', 'file'])

def folder_search(folder, search_text, verbose=True):
    print("DEBUG: Searching in {}".format(folder))
    allchildren = os.listdir(folder)
    print(allchildren)
    for item in allchildren:
        full_item = os.path.join(folder, item)
        print("DEBUG: {} is a dir {}".format(full_item, os.path.isdir(full_item)))
        if os.path.isdir(full_item):
            yield from folder_search(full_item, search_text)
        else:
            yield from file_search(full_item, search_text)
    print(os.listdir(folder))
    

def file_search(filename, search_text):
    print("DEBUG: Opening up {}".format(filename))
    with open(filename, 'r', encoding='utf-8') as fin:
        linenumber = 0
        for line in fin:
            linenumber += 1
            if line.lower().find(search_text) >= 0:
                #print(linenumber,line, filename)
                #capture in search result
                yield SearchResult(linenumber, line.strip(), filename) 

if __name__ == '__main__':
    args = parser.parse_args()
    folder_search(args.folder, args.search_text, args.verbose)


def test_file_search():
    pwd = os.path.dirname(__file__)
    filename = os.path.join(pwd, "tests", "file1.txt")
    result = next(file_search(filename, "kentucky"))
    expected = SearchResult(1, 'there once was a man from kentucky', 
                    "/home/zaighum47/python/pythonPractice/fileSearch/tests/file1.txt")
    assert expected == result
    
def test_folder_search():
    testfolder  = os.path.join(os.path.dirname(__file__), 'tests')
    searchGenerator = folder_search(testfolder, 'kentucky')
    result1 = next(searchGenerator)
    expected1 = SearchResult(1, 'there once was a man from kentucky', 
                    "/home/zaighum47/python/pythonPractice/fileSearch/tests/file1.txt")
    assert expected1 == result1
    
    result2 = next(searchGenerator)
    print(result2)
