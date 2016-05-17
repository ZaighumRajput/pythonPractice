#!/usr/bin/python3
import journal

def header(character, lengthOfLines, appName):
    header = character*lengthOfLines + "\n\t" +  appName + "\n" + character*lengthOfLines
    return header


def run_event_loop():
    
    command = None 
    journal_name = 'default'
    print("Loading {0}...".format(journal_name))
    journal_data = journal.load(journal_name)    

    while(command != 'X'):

        command = input('[L]ist entries, [A]dd an entry, E[x]it:')
        command = command.upper().strip()

        if command == 'L':
            list_entries(journal_data)
        elif command == 'A':
            add_entry(journal_data)
        elif command != 'X':
            print("'{}' not found".format(command))
    journal.save(journal_name, journal_data)

def list_entries(data):
    print("JOURNAL ENTRIES:")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)

def journalApp():
    print(header('*', 30, 'JOURNAL APP'))
    run_event_loop()

journalApp()

