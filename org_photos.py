import os


def make_place_directories(places):
    for place in places:
        os.mkdir(place)


def extract_place(filename):
    return filename.split('_')[1]


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []


    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)
    make_place_directories(places) 
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename,os.path.join(place,filename))
        directory=os.listdir()


if __name__ == "__main__":
    organize_photos("C:\\Users\\Yoshi\\Documents\\UDACITY\\PYTHON2\\org_photos\\Photos")
