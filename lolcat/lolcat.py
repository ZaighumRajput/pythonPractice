#!usr/bin/python3
import os
import cat_service

def main():

    print(header("*", 30, "LOLCAT FACTORY"))
    #get or create output folder
    output_folder = get_or_create_output_folder()

    print("Pictures will be saved to: {}".format(output_folder))
    #download cats
    #Website to download images from:
    url = "http://consuming-python-services-api.azurewebsites.net/content/cats/"
    cat_service.save_images(output_folder, url, number_of_images=3)
    #display cats

def header(character, lengthOfLines, appName):
    header = character*lengthOfLines + "\n\t" +  appName + "\n" + character*lengthOfLines
    return header 


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))
    #print(full_path)
    if not os.path.exists(full_path):
        print("Creating new directory")
        os.mkdir(full_path)
    return(full_path)

def display_cats(folder):
    print("Displaying cats")
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else platform.system() == 'Windows':
        subprocess.call(['explorer', folder])

if __name__ == "__main__":
    main()
