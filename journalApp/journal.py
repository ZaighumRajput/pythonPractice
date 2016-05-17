import os

def get_file_name(name):
    filename = os.path.join(".","SavedFiles", name + ".jrl")
    return filename

def load(name):
    journal_data = []
    filename = get_file_name(name)
    if os.path.exists(filename):
	    with open(filename, 'r') as fin:
		    for entry in fin.readlines():
			    journal_data.append(entry)

    return journal_data

def save(journal_name, journal_data):
    filename = get_file_name(journal_name)
    print("Saving to  : {}".format(filename))

    with open(filename, 'w') as fout:
	    for entry in journal_data:
            	fout.write(entry + '\n')

def add_entry(text, journal_data):
    journal_data.append(text)

