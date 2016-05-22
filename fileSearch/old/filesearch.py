#!/usr/bin/python3
import os

def main():
    folder = get_folder_to_search()
    if not folder:
        print("Sorry, we can't search that folder")
        return 

    text = get_search_text_from_user()

    if not text:
        print("We can't search nothing")

    search_folders(folder, text)
    
def get_folder_to_search():
    pass

def get_search_text():
    pass

def search_folder(folder, text):
    items = os.listdir(folder)
    
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            #use recursion here
            continue
        

def search_file(filename, search_text):
    
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            print(line)

if __name__ = "__main__":
    main()
