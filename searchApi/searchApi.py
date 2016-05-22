#!/usr/bin/python3
#encoding=utf8
import requests
import requests.exceptions
from collections import namedtuple

Movie = namedtuple('Movie',['Title', 'Year',
                    'imdbID','Type', 'Poster'])


class MovieClient:
    def __init__(self, search_text):

        if not search_text or not search_text.strip():
            raise ValueError('You must specify a search string')
        
        self.search_text = search_text




    def perform_search(self):
        url = "http://www.omdbapi.com/?s={}&y=&plot=short&r=json".format(self.search_text)

        #can throw connection error
        #should we handle it here or outside?
        response = requests.get(url)
        data = response.json()

        SearchResults = data['Search']
        results = [Movie(**m) for m in SearchResults] 

        return results

    @staticmethod
    def print_results(results):
        print ("{}.results".format(len(results)))
        for movie in results:
            print('{} -- {}'.format(movie.Year, movie.Title)) 
        

def input_loop(cmd: str):
    while cmd != 'q':
        try:
            client = MovieClient(cmd)
            results = client.perform_search()
            client.print_results(results)
            cmd = prompt_for_user_input()
            
        except requests.exceptions.ConnectionError as ce:
            print("ERROR: check connection") 
            
            #poor design for user input
            cmd = prompt_for_user_input()
        except ValueError as ve:
            print("ERROR: Your search string was invalid: {}".format(ve))
            cmd = prompt_for_user_input()

#        except Exception as x:
#            print("ERROR {}".format(x))
            
    return 


def prompt_for_user_input():
    return input('Title search text (q to quit)): ')


def test_perform_search():
    client = MovieClient('Rush')
    assert client.search_text == 'Rush'
    results = client.perform_search()
    assert (results is not None)

def test_input_loop_quit():
    assert input_loop('q') == None

def test_input_loop():
    pass

input_loop(prompt_for_user_input())
