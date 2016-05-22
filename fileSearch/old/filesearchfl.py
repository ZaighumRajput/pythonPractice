#!/usr/bin/python3
#not python3 compatiable...
import click

@click.command()
@click.option('--text')
@click.option('--folder', default=__file__)
def folder_search(folder, text):
    pass

def file_search(filename, search_text):
    pass

@click.command()
@click.option('--count', default=1)
@click.option('--name', prompt='Your name')
def hello(count, name):
    for x in range(count):
        click.echo("Hello {}".format(name))

if __name__ == '__main__':
    folder_search()
