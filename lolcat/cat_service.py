import os
import requests
import shutil


def open_connection(url):
    '''Connect to API service and open stream'''
    response = requests.get(url, stream=True)
    return response.raw

def stream_to_file(filepath, data_stream):
    with open(filepath, 'wb') as fout:
        shutil.copyfileobj(data_stream, fout)

def save_images(path : str, url : str, number_of_images : int):
    for count in range(1, number_of_images + 1):
        data = open_connection(url) #does the url return one image?
        filename = "lolcat{}.jpg".format(count)
        print("Saving {}...".format(filename))
        filepath = os.path.join(path, filename)
        stream_to_file(filepath, data)

